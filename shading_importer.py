import maya.cmds as cmds
import json
import pymel.core as pm

def load_json():

    filename = str(cmds.fileDialog2(fileFilter="*.json", dialogStyle=2)[0])
    return json.load(open(filename))


def apply_attributes(shape_node, shading_json, namespace):

    for i in shading_json[shape_node]["arnold_attributes"]:
        cmds.setAttr(namespace + shape_node + "." + i, shading_json[shape_node]["arnold_attributes"][i])


def apply_shaders(shape_node, shading_json, namespace):
    
    for i in shading_json[shape_node]["shaders"]:
        for j in range(0, len(shading_json[shape_node]["shaders"][i])):
            cmds.select(namespace + str(shading_json[shape_node]["shaders"][i][j]), replace=True)
            cmds.hyperShade(assign = namespace + str(i))




def get_shapes():
    shapes_list = cmds.ls(selection=True, dag=True, geometry=True)
    cleaned_shapes_list = []

    # remove curve and intermediate shapes
    for i in shapes_list:
        if ("curve" not in i) and ("Orig" not in i):
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

    object_namespace_cnt = 1 #replace by slider
    object_namespace = "*:" * object_namespace_cnt
    object_in_namespace = ""

    shaders_namespace_cnt = 1
    shaders_namespace = "*:" * shaders_namespace_cnt

    if (cmds.checkBox("checkbox_apply_attributes", query = True, value = True)):
        bool_apply_arnold_attributes = True
    if (cmds.checkBox("checkbox_apply_shaders", query = True, value = True)):
        bool_apply_shaders = True


    for shape in shapes_list:
        # find shape namespace
        object_in_namespace = shape.rpartition(':')[0]
        # remove shape namespace
        shape_namespace_stripped = shape.replace(object_in_namespace, "")
        # remove colon
        shape_namespace_stripped = shape_namespace_stripped[1:]


        print shape_namespace_stripped
        
        # check if shape in scene exists as shape in json
        if shape_namespace_stripped in shading_json:
            if bool_apply_arnold_attributes:
                apply_attributes(shape_namespace_stripped, shading_json, object_namespace)
                print "SHADING ATTRIBUTES APPLIED"
            
            if bool_apply_shaders:
                apply_shaders(shape_namespace_stripped, shading_json, shaders_namespace)
                print "SHADERS APPLIED"


def window():
    windowName = "shading_importer"
    windowSize = (400, 100)
    buttonSize = (100, 20)

    if (cmds.window(windowName , exists=True)):
        cmds.deleteUI(windowName)
    window = cmds.window( windowName, title= windowName, widthHeight=windowSize, sizeable=0)


    cmds.columnLayout( "mainColumn", adj=True )
    cmds.checkBox("checkbox_apply_attributes", height=buttonSize[1], label = "apply_attributes", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_apply_shaders", height=buttonSize[1], label = "apply_shaders", value = 0, parent = "mainColumn")
    cmds.button( label='Execute', height=buttonSize[1], parent = "mainColumn", command=("execute()"))


    cmds.showWindow( windowName )

    gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    cmds.window( windowName, edit=True, widthHeight=(windowSize[0], windowSize[1]) )



window()