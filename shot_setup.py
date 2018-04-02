import maya.cmds as cmds
import mtoa.aovs as aovs

def set_render_settings():
    cmds.setAttr("defaultArnoldDriver.halfPrecision", True)
    cmds.setAttr("defaultArnoldDriver.tiled", 1)
    cmds.setAttr("defaultArnoldRenderOptions.textureMaxMemoryMB", 8192)
    cmds.setAttr("defaultArnoldRenderOptions.maxSubdivisions", 5)
    cmds.setAttr("defaultArnoldRenderOptions.subdivFrustumCulling", 1)
    cmds.setAttr("defaultArnoldRenderOptions.enable_swatch_render", 0)
    cmds.setAttr("defaultArnoldRenderOptions.log_verbosity", 1)
    cmds.setAttr("defaultArnoldRenderOptions.autotx", 0)
    cmds.setAttr("defaultArnoldRenderOptions.textureAcceptUntiled", 0)
    cmds.setAttr("defaultArnoldRenderOptions.textureAcceptUnmipped", 0)
    cmds.setAttr("defaultArnoldRenderOptions.autotile", 0)
    cmds.setAttr("defaultArnoldDriver.mergeAOVs", 1)


def create_default_aovs():

    defaultAOVlist = ["P", "N", "Z", "coat", "specular", "diffuse", "direct", "indirect", "sss", "transmission"]
    currentAOVlist = aovs.AOVInterface().getAOVNodes(names=True)

    for i in defaultAOVlist:
        currentAOVlist = aovs.AOVInterface().getAOVNodes(names=True)
        aov_already_created = False

        for j in range (0, len(currentAOVlist)):
            if i in currentAOVlist[j]:
                aov_already_created = True
                print "AOV [" + i + "] has already been created, skipping"
        if aov_already_created == False:
            aovs.AOVInterface().addAOV(i)
            print "AOV [" + i + "] has been added"


def create_custom_aovs(char):

    if char == "girl":
        customAOVlist = ["mask_lips", "mask_lips_smear", "mask_tattoo", "mask_makeup_graphic", "mask_makeup_graphic_sharp", "mask_eyebrows", "mask_facing_ratio"]
    elif char == "man":
        customAOVlist = []
    elif char == "transgender":
        customAOVlist = ["mask_trans_graphic_skirt", "mask_trans_beard", "mask_trans_ears", "mask_trans_glitter", "mask_trans_eyes_red", "mask_trans_lips"]
    elif char == "vladimir":
        customAOVlist = []
    
    currentAOVlist = aovs.AOVInterface().getAOVNodes(names=True)
        
    for i in customAOVlist:
        currentAOVlist = aovs.AOVInterface().getAOVNodes(names=True)
        aov_already_created = False
        
        for j in range (0, len(currentAOVlist)):
            if i in currentAOVlist[j]:
                aov_already_created = True
                print "AOV [" + i + "] has already been created, skipping"
        if aov_already_created == False:
            aovs.AOVInterface().addAOV(i, aovType='rgba')
            print "AOV [" + i + "] has been added"

    # connect facing ratio shader
    if char == "girl":
        cmds.connectAttr("*:mat_aov_facingratio.outColor", "aiAOV_mask_facing_ratio.defaultValue", force=True)



def execute():
    if (cmds.checkBox("checkbox_set_render_settings", query = True, value = True)):
        set_render_settings()
        print "RENDER SETTINGS COMPLETED"

    if (cmds.checkBox("checkbox_create_default_aovs", query = True, value = True)):
        create_default_aovs()
        print "DEFAULT AOVS COMPLETE"

    if (cmds.checkBox("checkbox_create_custom_aovs_girl", query = True, value = True)):
        create_custom_aovs("girl")
        print "CUSTOM AOVS GIRL COMPLETE"

    if (cmds.checkBox("checkbox_create_custom_aovs_transgender", query = True, value = True)):
        create_custom_aovs("transgender")
        print "CUSTOM AOVS TRANSGENDER COMPLETE"

    """
    if (cmds.checkBox("checkbox_create_custom_aovs_man", query = True, value = True)):
        create_custom_aovs("man")
        print "CUSTOM AOVS MAN COMPLETE"
    """


def window():
    windowName = "shading_setup"
    windowSize = (400, 250)
    buttonSize = (100, 20)

    if (cmds.window(windowName , exists=True)):
        cmds.deleteUI(windowName)
    window = cmds.window( windowName, title= windowName, widthHeight=windowSize, sizeable=0)


    cmds.columnLayout( "mainColumn", adj=True )
    cmds.checkBox("checkbox_set_render_settings", height=buttonSize[1], label = "set_render_settings", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_create_default_aovs", height=buttonSize[1], label = "create_default_aovs", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_create_custom_aovs_girl", height=buttonSize[1], label = "create_custom_aovs_girl", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_create_custom_aovs_trans", height=buttonSize[1], label = "create_custom_aovs_trans", value = 0, parent = "mainColumn")
    """cmds.checkBox("checkbox_create_custom_aovs_man", height=buttonSize[1], label = "create_custom_aovs_man", value = 0, parent = "mainColumn")"""
    cmds.button( label='Execute', height=buttonSize[1], parent = "mainColumn", command=("execute()"))


    cmds.showWindow( windowName )

    gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    cmds.window( windowName, edit=True, widthHeight=(windowSize[0], windowSize[1]) )



window()