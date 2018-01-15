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
        customAOVlist = ["mask_lips", "mask_lips_smear", "mask_tattoo", "mask_makeup_graphic", "mask_makeup_graphic_sharp", "mask_eyebrows"]
    elif char == "man":
        customAOVlist = []
    elif char == "transvestite":
        customAOVlist = []
    elif char == "manager":
        customAOVlist = []
    
    currentAOVlist = aovs.AOVInterface().getAOVNodes(object_namesmes=True)
        
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

"""
# ISSUE: doesn't work for referenced curves since they can't be re-parented
def create_curvecollectors_boots():

    # BOOT LINES
    shapeName = "aicc_bootLines_back_blueShape"
    cmds.createNode("aiCurveCollector", n=shapeName)
    cmds.setAttr(shapeName + ".aiCurveWidth", 0.0375)

    cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(shapeName + ".aiVisibleInVolume", 0)
    cmds.setAttr(shapeName + ".castsShadows", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(shapeName + ".aiSelfShadows", 0)
    cmds.setAttr(shapeName + ".aiOpaque", 0)

    cmds.connectAttr("*:mat_boots_line_blue.outColor", shapeName + ".aiCurveShader", f=True)

    curveName = ["*:bootBack_blue_r_curve", "*:bootBack_blue_l_curve"]
    for i in curveName:
        cmds.parent(i, shapeName)



    # BOOT LINES
    shapeName = "aicc_bootLines_blackShape"
    cmds.createNode("aiCurveCollector", n=shapeName)
    cmds.setAttr(shapeName + ".aiCurveWidth", 0.02)

    cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(shapeName + ".aiVisibleInVolume", 0)
    cmds.setAttr(shapeName + ".castsShadows", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(shapeName + ".aiSelfShadows", 0)
    cmds.setAttr(shapeName + ".aiOpaque", 0)

    cmds.connectAttr("*:mat_boots_line_black.outColor", shapeName + ".aiCurveShader", f=True)

    curveName = ["*:bootBack_black01_l_curve", "*:bootBack_black02_l_curve", "*:bootBack_black01_r_curve", "*:bootBack_black02_r_curve", "*:bootBack_black03_r_curve"]
    for i in curveName:
        cmds.parent(i, shapeName)



    # BOOT LINES
    shapeName = "aicc_bootLines_black_longShape"
    cmds.createNode("aiCurveCollector", n=shapeName)
    cmds.setAttr(shapeName + ".aiCurveWidth", 0.02)

    cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(shapeName + ".aiVisibleInVolume", 0)
    cmds.setAttr(shapeName + ".castsShadows", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(shapeName + ".aiSelfShadows", 0)
    cmds.setAttr(shapeName + ".aiOpaque", 0)

    cmds.connectAttr("*:mat_boots_line_black_long.outColor", shapeName + ".aiCurveShader", f=True)

    curveName = ["*:bootBackLong_black_r_curve"]
    for i in curveName:
        cmds.parent(i, shapeName)


# ISSUE: doesn't work for referenced curves since they can't be re-parented
def create_curvecollectors_bra():

    # BRA LINES
    shapeName = "aicc_top_strap_longShape"
    cmds.createNode("aiCurveCollector", n=shapeName)
    cmds.setAttr(shapeName + ".aiCurveWidth", 0.1)

    cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(shapeName + ".aiVisibleInVolume", 0)
    cmds.setAttr(shapeName + ".castsShadows", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(shapeName + ".aiSelfShadows", 0)
    cmds.setAttr(shapeName + ".aiOpaque", 0)

    cmds.connectAttr("*:mat_top_strap_long.outColor", shapeName + ".aiCurveShader", f=True)

    curveName = ["*:braStrapShoulder_r_curve"]
    for i in curveName:
        cmds.parent(i, shapeName)



    shapeName = "aicc_top_strap_front_sideShape"
    cmds.createNode("aiCurveCollector", n=shapeName)
    cmds.setAttr(shapeName + ".aiCurveWidth", 0.06)

    cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(shapeName + ".aiVisibleInVolume", 0)
    cmds.setAttr(shapeName + ".castsShadows", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(shapeName + ".aiSelfShadows", 0)
    cmds.setAttr(shapeName + ".aiOpaque", 0)

    cmds.connectAttr("*:mat_top_strap_front_side.outColor", shapeName + ".aiCurveShader", f=True)

    curveName = ["*:braStrapSide_l_curve", "*:braStrapFront_c_curve", "*:braStrapSide_r_curve"]
    for i in curveName:
        cmds.parent(i, shapeName)



    shapeName = "aicc_top_strap_short_backShape"
    cmds.createNode("aiCurveCollector", n=shapeName)
    cmds.setAttr(shapeName + ".aiCurveWidth", 0.06)

    cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(shapeName + ".aiVisibleInVolume", 0)
    cmds.setAttr(shapeName + ".castsShadows", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(shapeName + ".aiSelfShadows", 0)
    cmds.setAttr(shapeName + ".aiOpaque", 0)

    cmds.connectAttr("*:mat_top_strap_short_back.outColor", shapeName + ".aiCurveShader", f=True)

    curveName = ["*:braStrapBack_l_curve", "*:braStrapBack_r_curve", "*:braStrapBackBottom_r_curve", "*:braStrapBackBottom_l_curve"]
    for i in curveName:
        cmds.parent(i, shapeName)



    shapeName = "aicc_top_strap_bottomShape"
    cmds.createNode("aiCurveCollector", n=shapeName)
    cmds.setAttr(shapeName + ".aiCurveWidth", 0.06)

    cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(shapeName + ".aiVisibleInVolume", 0)
    cmds.setAttr(shapeName + ".castsShadows", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(shapeName + ".aiSelfShadows", 0)
    cmds.setAttr(shapeName + ".aiOpaque", 0)

    cmds.connectAttr("*:mat_top_strap_bottom.outColor", shapeName + ".aiCurveShader", f=True)

    curveName = ["*:braStrapBottom_c_curve"]
    for i in curveName:
        cmds.parent(i, shapeName)


    shapeName = "aicc_top_strap_long_var1Shape"
    cmds.createNode("aiCurveCollector", n=shapeName)
    cmds.setAttr(shapeName + ".aiCurveWidth", 0.1)

    cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", 0)
    cmds.setAttr(shapeName + ".aiVisibleInVolume", 0)
    cmds.setAttr(shapeName + ".castsShadows", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", 0)
    cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", 0)
    cmds.setAttr(shapeName + ".aiSelfShadows", 0)
    cmds.setAttr(shapeName + ".aiOpaque", 0)

    cmds.connectAttr("*:mat_top_strap_long_var1.outColor", shapeName + ".aiCurveShader", f=True)

    curveName = ["*:braStrapShoulder_l_curve"]
    for i in curveName:
        cmds.parent(i, shapeName)
"""

def execute():
    if (cmds.checkBox("checkbox_set_render_settings", query = True, value = True)):
        set_render_settings()
        print "RENDER SETTINGS COMPLETED"

    if (cmds.checkBox("checkbox_create_default_aovs", query = True, value = True)):
        create_default_aovs()
        print "DEFAULT AOVS COMPLETE"

    if (cmds.checkBox("checkbox_create_custom_aovs", query = True, value = True)):
        create_custom_aovs("girl")
        print "CUSTOM AOVS COMPLETE"

    """
    if (cmds.checkBox("checkbox_create_curvecollectors_boots", query = True, value = True)):
        create_curvecollectors_boots()
        print "BOOTS CURVECOLLECTORS COMPLETE"

    if (cmds.checkBox("checkbox_create_curvecollectors_bra", query = True, value = True)):
        create_curvecollectors_bra()
        print "BRA CURVECOLLECTORS COMPLETE"
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
    cmds.checkBox("checkbox_create_custom_aovs", height=buttonSize[1], label = "create_custom_aovs", value = 0, parent = "mainColumn")
    # cmds.checkBox("checkbox_create_curvecollectors_boots", height=buttonSize[1], label = "create_curvecollectors_boots", value = 0, parent = "mainColumn")
    # cmds.checkBox("checkbox_create_curvecollectors_bra", height=buttonSize[1], label = "create_curvecollectors_bra", value = 0, parent = "mainColumn")
    cmds.button( label='Execute', height=buttonSize[1], parent = "mainColumn", command=("execute()"))


    cmds.showWindow( windowName )

    gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    cmds.window( windowName, edit=True, widthHeight=(windowSize[0], windowSize[1]) )



window()