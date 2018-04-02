import maya.cmds as cmds
import pymel.core as pm
import json
import io
import re
import sys

# there's a bug when there's multiple shape nodes in one mesh, can't handle that
# sometimes it takes multiple objects per shader, due to:
# desc_ponytail_left_out
#   "desc_ponytail_left_out_extra_Shape", "desc_ponytail_left_out_stray_Shape", "desc_ponytail_left_outShape", "desc_ponytail_left_out_extra02_Shape"
# name is in every description
# either give unique names


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

    # manually select all ramps, using them in the curve attributes
    ramp_list = cmds.ls("*ramp*")
    cmds.select(ramp_list, ne=True, add=True)
    
    selection = cmds.ls(sl=True)
    if selection:
        filename = cmds.fileDialog2(fileFilter="Maya ASCII (*.ma)", dialogStyle=2)
        cmds.file( filename[0], type='mayaAscii', es=True )


def get_default_arnold_mesh_attributes():
    # create temporary object to write out always-up-to-date arnold attribute list
    default_object = cmds.polyCube(n="tmp_default_cube")
    default_object_shape = str(default_object[0]) + "Shape" 

    default_arnold_attribute_names = cmds.listAttr(default_object_shape, read=True, scalar=True, st=['*ai*'])
    default_arnold_attribute_names.append("castsShadows")
    default_arnold_attribute_names.append("smoothShading")
    default_arnold_attributes = []

    for i in default_arnold_attribute_names:
        default_arnold_attributes.append( (str(i), cmds.getAttr(default_object_shape + "." + i)) )
        
    cmds.delete(default_object)

    return default_arnold_attributes


def get_default_arnold_curve_attributes():
    # create temporary curve to write out always-up-to-date arnold attribute list
    default_object = cmds.curve(n="tmp_default_curve", p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)])
    default_object_shape = str(cmds.listRelatives(default_object, shapes=True)[0])

    default_arnold_attribute_names = cmds.listAttr(default_object_shape, read=True, scalar=True, st=['*ai*'])
    default_arnold_attribute_names.append("castsShadows")

    default_arnold_attributes = []

    for i in default_arnold_attribute_names:
        default_arnold_attributes.append( (str(i), cmds.getAttr(default_object_shape + "." + i)) )

    cmds.delete(default_object)

    return default_arnold_attributes



def get_arnold_attributes(shape_name, default_arnold_attributes):

    arnold_attribute_names = cmds.listAttr(shape_name, read=True, scalar=True, st=['*ai*'])
    # need to append the other attributes too, eg castShadows, smoothShading
    arnold_attribute_names.append("castsShadows")
    arnold_attribute_names.append("smoothShading")

    arnold_attributes = []
    non_default_arnold_attributes = {}
    changed_attributes_count = 0

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
                    changed_attributes_count += 1
                    print "-->> (", arnold_attributes[i][0], ", ", arnold_attributes[i][1], ")"

    if changed_attributes_count == 0:
        print "-->> No adjusted attributes for this shape"

    return non_default_arnold_attributes


def get_arnold_hair_attributes(shape_name):

    arnold_attribute_names = cmds.listAttr(shape_name, read=True, scalar=True, st=['ai*'])
    arnold_attribute_names.append("faceCamera")
    arnold_attribute_names.append("castsShadows")

    arnold_attributes = []
    non_default_arnold_attributes = {}

    for i in arnold_attribute_names:
        arnold_attributes.append( (str(i), cmds.getAttr(shape_name + "." + i)) )
    
    for i in range (0, len(arnold_attributes)):
        non_default_arnold_attributes[str(arnold_attributes[i][0])] = arnold_attributes[i][1]
        print "-->> (", arnold_attributes[i][0], ", ", arnold_attributes[i][1], ")"

    return non_default_arnold_attributes



def get_arnold_curve_attributes(shape_name, default_arnold_attributes):

    arnold_attribute_names = cmds.listAttr(shape_name, read=True, scalar=True, st=['*ai*'])
    arnold_attribute_names.append("castsShadows")
    arnold_attributes = []
    non_default_arnold_attributes = {}
    changed_attributes_count = 0

    # if shader is connected to curvewidth, do not add the aiCurveWidth attribute.. once it is locked can't overwrite it with value
    curve_width_export = False
    if (cmds.listConnections(shape_name + ".aiCurveWidth") == None):
        curve_width_export = True

    for i in arnold_attribute_names:
        arnold_attributes.append( (str(i), cmds.getAttr(shape_name + "." + i)) )
        
    # amount of attributes needs to be equal
    if len(arnold_attribute_names) == len(default_arnold_attributes):
        for i in range (0, len(arnold_attributes)):
            
            # attribute names need to be equal
            if arnold_attributes[i][0] == default_arnold_attributes[i][0]:
                # if attribute value changed
                if arnold_attributes[i][1] != default_arnold_attributes[i][1]:
                    if (arnold_attributes[i][0] != "aiCurveShaderR") and (arnold_attributes[i][0] != "aiCurveShaderG") and (arnold_attributes[i][0] != "aiCurveShaderB"):
                        if (arnold_attributes[i][0] == "aiCurveWidth") and (curve_width_export == False):
                            continue
                        non_default_arnold_attributes[str(arnold_attributes[i][0])] = arnold_attributes[i][1]
                        changed_attributes_count += 1
                        print "-->> (", arnold_attributes[i][0], ", ", arnold_attributes[i][1], ")"

    if changed_attributes_count == 0:
        print "-->> No adjusted attributes for this shape"

    # add curve shader and width
    non_default_arnold_attributes["curve_shader"] = cmds.listConnections(shape_name + ".aiCurveShader")
    non_default_arnold_attributes["curve_width"] = cmds.listConnections(shape_name + ".aiCurveWidth")

    return non_default_arnold_attributes



def get_shaders(shape_name, object_namespace):

    object_name = str(cmds.listRelatives(shape_name, parent=True)[0])
    shader_dict = {}

    print object_name

    shading_groups = cmds.listConnections(shape_name, type='shadingEngine')
    shaders = cmds.ls(cmds.listConnections(shading_groups), materials=1) 

    cleaned_shader_list = list(set(shaders))
    cleaned_shading_groups_list = list(set(shading_groups))

    # remove initialShadingGroup
    for sg in cleaned_shading_groups_list:
        if (sg == "initialShadingGroup") or (object_namespace in sg):
            cleaned_shading_groups_list.remove(sg)


    for i in range (0, len(cleaned_shading_groups_list)):
        current_shader = cmds.ls(cmds.listConnections(cleaned_shading_groups_list[i]), materials=1)
        cmds.select(current_shader)
        cmds.hyperShade(current_shader, objects='')
        face_assignments = cmds.ls(selection=True)
        cleaned_face_assignments = []

        # remove all other shapes that came with the hypershade material selection
        for k in face_assignments:
            # ------------- BUG!
            # possibility of multiple shapes here, this is wrong!!!!
            # the object name can be found in multiple shapes
            if (str(object_name) in k) or (str(shape_name) in k):
                cleaned_face_assignments.append(str(k))
        
        # remove namespace when writing to json
        for f in range (0, len(cleaned_face_assignments)):
            cleaned_face_assignments[f] = cleaned_face_assignments[f].replace(object_namespace, "")

        shader_dict[str(cleaned_shading_groups_list[i])] = cleaned_face_assignments

    return shader_dict


def get_shapes():
    shapes_list = cmds.ls(selection=True, dag=True, geometry=True)
    cleaned_shapes_list = []

    """
    # remove curve and intermediate shapes
    for i in shapes_list:
        if ("curve" not in i) and ("Orig" not in i):
            cleaned_shapes_list.append(i)
    """

    # remove intermediate shapes
    for i in shapes_list:
        if "Orig" not in i:
            cleaned_shapes_list.append(i)

    if len(cleaned_shapes_list) == 0:
        raise Exception("Select at least one valid object")
    else:
        return cleaned_shapes_list


# needs to export without namespaces
def export_shading_json():
    shape_list = get_shapes()
    object_data = {}
    default_arnold_mesh_attributes = get_default_arnold_mesh_attributes()
    default_arnold_curve_attributes = get_default_arnold_curve_attributes()

    namespace_list = []
    for shape in shape_list:
        cmds.select(shape)
        namespace = pm.selected()[0].namespace()

        if namespace not in namespace_list:
            namespace_list.append(namespace)


    for shape in shape_list:
        # strip namespace for writing to json
        for namespace in namespace_list:
            if namespace in shape:
                shape_namespace_stripped = shape.replace(namespace, "")
                current_namespace = namespace

        # query data type
        datatype = str(cmds.objectType(shape))

        print shape + ": "

        if datatype == "mesh":
            object_data[str(shape_namespace_stripped)] = {"shaders": get_shaders(shape, current_namespace), "arnold_attributes": get_arnold_attributes(shape, default_arnold_mesh_attributes)}
        elif datatype == "xgmSplineDescription":
            object_data[str(shape_namespace_stripped)] = {"shaders": get_shaders(shape, current_namespace), "arnold_attributes": get_arnold_hair_attributes(shape)}
        elif datatype == "nurbsCurve":
            object_data[str(shape_namespace_stripped)] = {"arnold_attributes": get_arnold_curve_attributes(shape, default_arnold_curve_attributes)}

    filename = str(cmds.fileDialog2(fileFilter="*.json", dialogStyle=2)[0])

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