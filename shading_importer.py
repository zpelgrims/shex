import maya.cmds as cmds
import json
import pymel.core as pm

def load_json():

    filename = str(cmds.fileDialog2(fileFilter="*.json", dialogStyle=2)[0])
    return json.load(open(filename))


def apply_attributes(shape_node, shading_json, namespace):

    for i in shading_json[shape_node]["arnold_attributes"]:
        cmds.setAttr(namespace + shape_node + "." + i, shading_json[shape_node]["arnold_attributes"][i])


def apply_curve_attributes(shape_node, shading_json, namespace):

    for i in shading_json[shape_node]["arnold_attributes"]:
        if (i == "curve_shader"):
            cmds.connectAttr(namespace + shading_json[shape_node]["arnold_attributes"][i][0] + ".outColor", namespace + shape_node + ".aiCurveShader", force=True)
        elif (i == "curve_width"):
            #print shading_json[shape_node]["arnold_attributes"][i]
            if ( shading_json[shape_node]["arnold_attributes"][i] != None ):
                cmds.connectAttr(namespace + shading_json[shape_node]["arnold_attributes"][i][0] + ".outAlpha", namespace + shape_node + ".aiCurveWidth", force=True)
        else:
            cmds.setAttr(namespace + shape_node + "." + i, shading_json[shape_node]["arnold_attributes"][i])

def apply_shaders(shape_node, shading_json, namespace):
    
    for i in shading_json[shape_node]["shaders"]:
        for j in range(0, len(shading_json[shape_node]["shaders"][i])):
            cmds.select(namespace + str(shading_json[shape_node]["shaders"][i][j]), replace=True)
            cmds.hyperShade(assign = namespace + str(i))




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



def execute():

    shading_json = load_json()
    shapes_list = get_shapes()

    bool_apply_arnold_attributes = False
    bool_apply_shaders = False

    object_namespace_cnt = cmds.intSliderGrp('slider_object_namespaces', query = True, value = True)
    object_namespace = "*:" * object_namespace_cnt
    shaders_namespace_cnt = cmds.intSliderGrp('slider_shaders_namespaces', query = True, value = True)
    shaders_namespace = "*:" * shaders_namespace_cnt

    object_in_namespace = ""

    if (cmds.checkBox('checkbox_apply_attributes', query = True, value = True)):
        bool_apply_arnold_attributes = True
    if (cmds.checkBox('checkbox_apply_shaders', query = True, value = True)):
        bool_apply_shaders = True


    for shape in shapes_list:
        # find shape namespace
        object_in_namespace = shape.rpartition(':')[0]
        # remove shape namespace
        shape_namespace_stripped = shape.replace(object_in_namespace, "")
        # remove colon
        shape_namespace_stripped = shape_namespace_stripped[1:]

        # print shape_namespace_stripped

        # query data type
        datatype = str(cmds.objectType(shape))
        
        # check if shape in scene exists as shape in json
        if shape_namespace_stripped in shading_json:
            if bool_apply_arnold_attributes:
                if (datatype != "nurbsCurve"):
                    apply_attributes(shape_namespace_stripped, shading_json, object_namespace)
                else: #special treatment for nurbs curves
                    apply_curve_attributes(shape_namespace_stripped, shading_json, object_namespace)
                print "SHADING ATTRIBUTES APPLIED >>", shape
            
            if bool_apply_shaders:
                if (datatype != "nurbsCurve"):
                    apply_shaders(shape_namespace_stripped, shading_json, shaders_namespace)
                print "SHADERS APPLIED >>", shape


    # check which objects still have the initialshadinggroup assigned
    for shape in shapes_list:
        datatype = str(cmds.objectType(shape))
        if (datatype != "nurbsCurve"):
            shading_groups = cmds.listConnections(shape, type='shadingEngine')
            shaders = cmds.ls(cmds.listConnections(shading_groups), materials=1)

            for i in shading_groups:
                if (i == "initialShadingGroup"):
                    print "SHADING IMPORT WARNING: initialShadingGroup still assigned to >>", shape



def window():
    windowName = "shading_importer"
    windowSize = (400, 250)
    buttonSize = (100, 30)

    if (cmds.window(windowName , exists=True)):
        cmds.deleteUI(windowName)
    window = cmds.window( windowName, title= windowName, widthHeight=windowSize, sizeable=0)

    cmds.columnLayout( "mainColumn", adj=True )
    cmds.text(label='HOW TO USE:')
    cmds.text(label='1. reference in animation (.abc)')
    cmds.text(label='2. reference in published shading (.ma)')
    cmds.text(label='3. set appropriate amount of namespaces [usually 1]')
    cmds.text(label='4. select top level transform of alembic')

    cmds.separator( height=20, style='double' )
    
    cmds.columnLayout( "mainColumn", adj=True )
    cmds.intSliderGrp('slider_object_namespaces', field=True, label='object_namespaces', minValue=0, maxValue=3, fieldMinValue=0, fieldMaxValue=10, value=1)
    cmds.intSliderGrp('slider_shaders_namespaces', field=True, label='shaders_namespaces', minValue=0, maxValue=3, fieldMinValue=0, fieldMaxValue=10, value=1)

    cmds.separator( height=20, style='double' )

    cmds.checkBox("checkbox_apply_attributes", height=buttonSize[1], label = "apply_attributes", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_apply_shaders", height=buttonSize[1], label = "apply_shaders", value = 0, parent = "mainColumn")
    cmds.button( label='Execute', height=buttonSize[1], parent = "mainColumn", command=("execute()"))


    cmds.showWindow( windowName )

    gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    cmds.window( windowName, edit=True, widthHeight=(windowSize[0], windowSize[1]) )



window()