import maya.cmds as cmds
import json


def load_json():

    filename = str(cmds.fileDialog2(fileFilter="*.json", dialogStyle=2)[0])
    return json.load(open(filename))


def apply_attributes(shape_node, shading_json):

    for i in shading_json[shape_node]["arnold_attributes"]:
        cmds.setAttr(shape_node + "." + i, shading_json[shape_node]["arnold_attributes"][i])


def apply_shaders(shape_node, shading_json):
    
    for i in shading_json[shape_node]["shaders"]:
        for j in range(0, len(shading_json[shape_node]["shaders"][i])):
            cmds.select(shape_node + ".f" + str(shading_json[shape_node]["shaders"][i][j]), replace=True)
            cmds.hyperShade(assign = "*:" + str(i))


def get_shapes():
    return cmds.listRelatives(cmds.ls(selection=True))



def execute():

    shape_node = "pSphereShape1" 
    shading_json = load_json()
    shapes_list = get_shapes()

    if (cmds.checkBox("checkbox_apply_attributes", query = True, value = True)):
        for shape in shape_list:
            apply_attributes(shape, shading_json)
        print "SHADING NODES EXPORTED"

    if (cmds.checkBox("checkbox_apply_shaders", query = True, value = True)):
        for shape in shape_list:
            apply_shaders(shape, shading_json)
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