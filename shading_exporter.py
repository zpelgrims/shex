import maya.cmds as cmds
import json
import io
import re
import sys

try:
    to_unicode = unicode
except NameError:
    to_unicode = str



def export_shading_nodes():
    # "*" to only select nodes without namespace
    material_list = cmds.ls("*", materials=True)
    cmds.select(material_list)
    
    sg_list = cmds.ls("*", sets=True)
    cmds.select(sg_list, ne=True, add=True)
    
    # remove default sets since they get picked up automatically with the shading groups
    cmds.select("defaultLightSet", ne=True, deselect=True)
    cmds.select("defaultObjectSet", ne=True, deselect=True)
    
    selection = cmds.ls(sl=True)
    if selection:
        filename = cmds.fileDialog2(fileFilter="Maya ASCII (*.ma)", dialogStyle=2)
        cmds.file( filename[0], type='mayaAscii', es=True )


def get_default_arnold_attributes():
    # create temporary object to write out always-up-to-date arnold attribute list
    default_object = cmds.polyCube(n="tmp_default_cube")
    default_object_shape = str(default_object[0]) + "Shape" 

    default_arnold_attribute_names = cmds.listAttr(default_object_shape, read=True, scalar=True, st=['*ai*'])
    default_arnold_attributes = []

    for i in default_arnold_attribute_names:
        default_arnold_attributes.append( (str(i), cmds.getAttr(default_object_shape + "." + i)) )
        
    cmds.delete(default_object)

    return default_arnold_attributes


def get_arnold_attributes(shape_name, default_arnold_attributes):

    arnold_attribute_names = cmds.listAttr(shape_name, read=True, scalar=True, st=['*ai*'])
    arnold_attributes = []
    non_default_arnold_attributes = {}

    for i in arnold_attribute_names:
        arnold_attributes.append( (str(i), cmds.getAttr(shape_name + "." + i)) )
        
    # amount of attributes needs to be equal
    if len(arnold_attribute_names) == len(default_arnold_attributes):
        for i in range (0, len(arnold_attributes)):
            
            # attribute names need to be equal
            if arnold_attributes[i][0] == default_arnold_attributes[i][0]:
                # if attribute value changed
                if arnold_attributes[i][1] != default_arnold_attributes[i][1]:
                    non_default_arnold_attributes[str(arnold_attributes[i][0])] = arnold_attributes[i][1]
                    print shape_name, " >> (", arnold_attributes[i][0], ", ", arnold_attributes[i][1], ")"

    return non_default_arnold_attributes


def get_shaders(shape_name):

    object_name = str(cmds.listRelatives(shape_name, parent=True)[0])
    shader_dict = {}


    shading_groups = cmds.listConnections(shape_name, type='shadingEngine')
    shaders = cmds.ls(cmds.listConnections(shading_groups), materials=1) 

    cleaned_shader_list = list(set(shaders))
    cleaned_shading_groups_list = list(set(shading_groups))


    for i in range (0, len(cleaned_shading_groups_list)):
        current_shader = cmds.ls(cmds.listConnections(cleaned_shading_groups_list[i]), materials=1)
        cmds.select(current_shader)
        cmds.hyperShade(current_shader, objects='')
        # WRONG_ need to only select faces within shape_name, not all objects
        face_assignments = cmds.ls(selection=True)
        
        print face_assignments

        for j in range (0, len(face_assignments)):
            face_assignments[j] = str(face_assignments[j])
            face_assignments[j] = re.sub(object_name + ".f", '', face_assignments[j])
        
        # only want current object here, not multiple objects, and without namespace
        # return faces even if the it covers whole body, makes code easier later on
        shader_dict[str(cleaned_shading_groups_list[i])] = face_assignments

    return shader_dict


def get_shapes():
    shapes_list = cmds.ls(selection=True, dag=True, geometry=True)
    cleaned_shapes_list = []

    # remove curve shapes
    for i in shapes_list:
        if ("curve" not in i) and ("Orig" not in i):
            cleaned_shapes_list.append(i)

    if len(cleaned_shapes_list) == 0:
        raise Exception("Select at least one object")
    else:
        print cleaned_shapes_list
        return cleaned_shapes_list


# needs to export without namespaces
def export_shading_json():
    shape_list = get_shapes()
    object_data = {}
    default_arnold_attributes = get_default_arnold_attributes()

    for shape in shape_list:
        # find shape namespace
        object_in_namespace = shape.rpartition(':')[0]
        # remove shape namespace
        shape_namespace_stripped = shape.replace(object_in_namespace, "")
        # remove colon
        shape_namespace_stripped = shape_namespace_stripped[1:]

        print shape
        object_data[str(shape_namespace_stripped)] = {"shaders": get_shaders(shape), "arnold_attributes": get_arnold_attributes(shape, default_arnold_attributes)}

    filename = str(cmds.fileDialog2(fileFilter="*.json", dialogStyle=2)[0])
    print "filename: ", filename

    # Write JSON file
    with io.open(filename, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(object_data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))


def execute():
    if (cmds.checkBox("checkbox_export_shading_nodes", query = True, value = True)):
        export_shading_nodes()
        print "SHADING NODES EXPORTED"

    if (cmds.checkBox("checkbox_export_shading_json", query = True, value = True)):
        export_shading_json()
        print "SHADING JSON EXPORTED"


def window():
    windowName = "shading_exporter"
    windowSize = (400, 100)
    buttonSize = (100, 20)

    if (cmds.window(windowName , exists=True)):
        cmds.deleteUI(windowName)
    window = cmds.window( windowName, title= windowName, widthHeight=windowSize, sizeable=0)


    cmds.columnLayout( "mainColumn", adj=True )
    cmds.checkBox("checkbox_export_shading_nodes", height=buttonSize[1], label = "export_shading_nodes", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_export_shading_json", height=buttonSize[1], label = "export_shading_json", value = 0, parent = "mainColumn")
    cmds.button( label='Execute', height=buttonSize[1], parent = "mainColumn", command=("execute()"))


    cmds.showWindow( windowName )

    gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    cmds.window( windowName, edit=True, widthHeight=(windowSize[0], windowSize[1]) )



window()