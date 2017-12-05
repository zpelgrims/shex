import maya.cmds as cmds

def select_objects(object_names):
    cmds.select(object_names)
    return cmds.ls(selection=True)

"""
def assign_shading_girl():

    #BODY
    object_names = ["*:body_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSssSetname", "sss_skin", type="string")
        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 4)
        cmds.setAttr(shapeName + ".aiDispAutobump", True)

        cmds.hyperShade(assign="*:mat_mix_skin_head_bodySG")



    #TEETH
    object_names = ["*:teeth_u_hi", "*:teeth_d_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSssSetname", "sss_skin", type="string")
        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_teethSG")


    #GUM
    object_names = ["*:gum_u_hi", "*:gum_d_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSssSetname", "sss_skin", type="string")
        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_gumsSG")


    #TONGUE
    object_names = ["*:tongue_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSssSetname", "sss_skin", type="string")
        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_tongueSG")


    #PUPIL
    object_names = ["*:pupil_r_hi", "*:pupil_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 1)

        cmds.hyperShade(assign="*:mat_eyes_pupilsSG")


    #SCLERA
    object_names = ["*:eyeBall_r_hi", "*:eyeBall_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSssSetname", "sss_skin", type="string")
        cmds.setAttr(shapeName + ".aiSubdivType", 0)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 0)

        cmds.hyperShade(assign="*:mat_mix_eye_sclera_lineSG")


    object_names = ["*:eyeBall_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName + ".f[445:468]")
        cmds.hyperShade(assign="*:mat_iris_baseSG")

    object_names = ["*:eyeBall_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName + ".f[440:463]")
        cmds.hyperShade(assign="*:mat_iris_baseSG")


    # CORNEA
    object_names = ["*:eyeCornea_r_hi", "*:eyeCornea_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".aiSssSetname", "sss_skin", type="string")
        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_eyes_corneaSG")


    # LACRIMAL
    object_names = ["*:lacrimal_l_hi", "*:lacrimal_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".castsShadows", False)

        cmds.hyperShade(assign="*:mat_lacrimal_flatSG")


    # EYELASHES
    object_names = ["*:eyelashes_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_eyelashes_flatSG")


    # BOOTS
    object_names = ["*:bootStrap_l_hi", "*:bootStrap_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_boots_no_sssSG")


    # BOOTS MAIN
    object_names = ["*:boot_l_hi", "*:boot_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_bootsSG")


    # TROUSERS
    object_names = ["*:jeans_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 3)
        cmds.setAttr(shapeName + ".aiDispAutobump", True)

        cmds.hyperShade(assign="*:mat_mix_trousers_linesSG")


    # TROUSER BUTTON BACKPLATE
    object_names = ["*:jeansButtonBackplate_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_trousers_button_backplateSG")


    # TROUSERS LABEL
    object_names = ["*:jeansLabel_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 3)

        cmds.hyperShade(assign="*:mat_trousers_labelSG")


    # CHOKER RING
    object_names = ["*:chokerRingpaper_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_choker_ring_flatSG")


    # CHOKER
    object_names = ["*:chokerMain_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)

        cmds.hyperShade(assign="*:mat_chokerSG")


    # BRA MAIN
    object_names = ["*:bra_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 1)
        cmds.setAttr(shapeName + ".aiOpaque", False)

        cmds.hyperShade(assign="*:mat_mix_top_sequinSG")


    # BRA STRAPS BLACK
    object_names = ["*:braStrapTop_c_hi", "*:braStrapShoulder_r_hi", "*:braStrapShoulder_l_hi", "*:braStrapBottom_r_hi", "*:braStrapBottom_c_hi", "*:braStrapTop_l_hi", "*:braStrapBottom_l_hi", "*:braStrapTop_r_hi", "*:braStrapBottomLoose_l_hi", "*:braStrapBottomLoose_r_hi", "*:braStrapBottomLoose01_c_hi", "*:braStrapBottomLoose02_c_hi", "*:braStrapBottomLoose03_c_hi", "*:braStrapBottomLoose04_c_hi", "*:braStrapBottomLoose05_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)

        cmds.hyperShade(assign="*:mat_viewport_top_strap_black_flatSG")


    # BRA STRAPS GREY
    object_names = ["*:braStrapBottomLoose06_c_hi", "*:braStrapBottomLoose07_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)

        cmds.hyperShade(assign="*:mat_top_strap_grey_flatSG")


    # BRA STRAPS INVISIBLE
    object_names = ["*:braStrapTop_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])

        cmds.select(shapeName + ".f[0:8]")
        cmds.hyperShade(assign="*:mat_top_strap_invisibleSG")

        cmds.select(shapeName + ".f[42:50]")
        cmds.hyperShade(assign="*:mat_top_strap_invisibleSG")


    # BRA RING
    object_names = ["*:braRing_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_top_ring_flatSG")


    # EARRINGS
    object_names = ["*:earRing_l_hi", "*:earRing02_l_hi", "*:earRing_r_hi", "*:earRing02_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 1)

        cmds.hyperShade(assign="*:mat_earrings_flatSG")



    # GLASSES
    object_names = ["*:glassesConnection_r_hi", "*:glassesConnection_l_hi", "*:glassesConnection_c_hi", "*:glassesEar_r_hi", "*:glassesEar_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 3)

        cmds.hyperShade(assign="*:mat_glasses_goldSG")


    # GLASSES GLASS
    object_names = ["*:glassesGlass_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_glasses_glassSG")


    # GLASSES FRAME
    object_names = ["*:glassesFrame_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 2)

        cmds.hyperShade(assign="*:mat_glasses_frameSG")


    # GLASSES EARS
    object_names = ["*:glassesEarBack_r_hi", "*:glassesEarBack_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".aiSubdivType", 1)
        cmds.setAttr(shapeName + ".aiSubdivIterations", 3)

        cmds.hyperShade(assign="*:mat_glasses_earpiecesSG")


    # LINES
    object_names = ["*:noseLine_l_geo", "*:noseLine_r_geo"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_nostrilsSG")


    object_names = ["*:backLine_c_hi", "*:line_arm_l_hi", "*:line_arm_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_hipcrease_rightSG") #this is correct


    object_names = ["*:eyeLine_r_geo"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_eye_leftSG")


    object_names = ["*:eyeLine_l_geo"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_eye_rightSG")


    object_names = ["*:line_hipcrease_left"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_hipcrease_leftSG")


    object_names = ["*:line_hipcrease_right"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_hipcrease_rightSG")


    object_names = ["*:line_belly_side"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_belly_rightSG")


    object_names = ["*:line_clavicle"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_clavicleSG")


    object_names = ["*:line_ribcage_right_02"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_ribcage_right_02SG")


    object_names = ["*:line_ribcage_left_02"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_ribcage_left_02SG")


    object_names = ["*:line_ribcage_right_01"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_ribcage_rightSG")


    object_names = ["*:line_ribcage_left_01"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_ribcage_leftSG")


    object_names = ["*:line_sterno_c_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_line_sternoSG")


    object_names = ["*:backPocketLine_l_hi", "*:backPocketLine_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_trousers_pocket_back_greySG")


    object_names = ["*:backPocketLineBottomGrey_r_hi", "*:backPocketLineBottomGrey_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_trousers_pocket_bottom_greySG")


    object_names = ["*:backPocketLineBottomBlack_r_hi", "*:backPocketLineBottomBlack_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_trousers_pocket_bottom_blackSG")



    object_names = ["*:strapLine_l_hi", "*:strapLine_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_trousers_strap_01SG")


    object_names = ["*:frontPocketLine_r_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_trousers_pocket_01SG")


    object_names = ["*:frontPocketLine_l_hi"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularReflection", False)
        cmds.setAttr(shapeName + ".aiVisibleInDiffuseTransmission", False)
        cmds.setAttr(shapeName + ".aiVisibleInSpecularTransmission", False)
        cmds.setAttr(shapeName + ".doubleSided", False)

        cmds.hyperShade(assign="*:mat_trousers_pocket_02SG")


def assign_shading_girl_hair(namespace_cnt):
    namespace = "*:" * namespace_cnt

    # HAIR
    object_names = [namespace + "desc_sides_baked", namespace + "desc_sidecuts", namespace + "desc_ponytail_left", namespace + "desc_ponytail_right", namespace + "desc_looseback", namespace + "desc_looseback_longer", namespace + "desc_fringe_stray", namespace + "desc_ponytail_left_stray", namespace + "desc_ponytail_right_stray"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_hair_mainSG")


    # HAIR PONYTAIL
    object_names = [namespace + "desc_ponytail_left_out", namespace + "desc_ponytail_right_out", namespace + "desc_ponytail_left_out_stray", namespace + "desc_ponytail_right_out_stray", namespace + "desc_ponytail_right_out_extra", namespace + "desc_ponytail_left_out_extra", namespace + "desc_ponytail_left_out_extra02"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_hair_ponytailsSG")


    # HAIR FRINGE
    object_names = [namespace + "desc_fringe_mirrored"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)

        cmds.hyperShade(assign="*:mat_hair_fringeSG")


    # HAIR FRINGE REFLECTION
    object_names = [namespace + "desc_fringe_top"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)
        cmds.setAttr(shapeName + ".castsShadows", False)

        cmds.hyperShade(assign="*:mat_hair_fringe_topSG")


    # HAIR GRAPHIC
    object_names = [namespace + "desc_mouthHair"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)

        cmds.hyperShade(assign="*:mat_hair_graphicSG")



    # HAIR GRAPHIC
    object_names = [namespace + "desc_graphic_ponytail_right", namespace + "desc_graphic_ponytail_left", namespace + "desc_graphic_scalp", namespace + "desc_graphic_fringe"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.setAttr(shapeName + ".aiOpaque", False)

        cmds.hyperShade(assign="*:mat_hair_graphicSG")



    # PINS PINKS
    object_names = [namespace + "hairclip_geo_01", namespace + "hairclip_geo_04", namespace + "hairclip_geo_05", namespace + "hairclip_geo_06", namespace + "hairclip_geo_07", namespace + "hairclip_geo_08", namespace + "hairclip_geo_09", namespace + "hairclip_geo_022", namespace + "hairclip_geo_023", namespace + "hairband_right_main_geo15", namespace + "hairband_right_main_geo11", namespace + "hairband_right_main_geo10", namespace + "hairband_right_main_geo", namespace + "hairband_left_main_geo"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_hair_clip_pinkSG")


    # PINS ORANGE
    object_names = [namespace + "hairclip_geo_02", namespace + "hairclip_geo_014", namespace + "hairclip_geo_012", namespace + "hairclip_geo_019", namespace + "hairclip_geo_021", namespace + "hairband_right_main_geo13"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_hair_clip_orangeSG")


    # PINS GREEN
    object_names = [namespace + "hairclip_geo_010", namespace + "hairclip_geo_017", namespace + "hairclip_geo_020", namespace + "hairclip_geo_024", namespace + "hairband_right_main_geo8", namespace + "hairband_right_main_geo3"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_hair_clip_greenSG")


    # PINS BLUE
    object_names = [namespace + "hairclip_geo_011", namespace + "hairclip_geo_015", namespace + "hairclip_geo_013", namespace + "hairclip_geo_016", namespace + "hairclip_geo_018", namespace + "hairband_right_main_geo12", namespace + "hairband_right_main_geo9"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_hair_clip_blueSG")


def assign_shading_bag():
    # BAG SHADING ASSIGNMENT
    object_names = ["*:Pattern2D_31959", "*:Pattern2D_31959_1", "*:Pattern2D_31959_2", "*:Pattern2D_31959_3", "*:Pattern2D_31959_4", "*:Pattern2D_38895", "*:Pattern2D_38896"]
    selected_items = select_objects(object_names)
    for i in selected_items:
        shapeName = str(cmds.listRelatives(i, shapes=True)[0])
        cmds.select(shapeName)

        cmds.hyperShade(assign="*:mat_bag_blueSG")
"""

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
    import mtoa.aovs as aovs

    # merge aovs into single exr by default
    cmds.setAttr("defaultArnoldDriver.mergeAOVs", True)

    defaultAOVlist = ["crypto_material", "crypto_object", "P", "N", "Z", "coat", "specular", "diffuse", "direct", "indirect", "sss", "transmission"]
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
    import mtoa.aovs as aovs

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


def execute():
    if (cmds.checkBox("checkbox_set_render_settings", query = True, value = True)):
        set_render_settings()
        print "RENDER SETTINGS COMPLETED"

    if (cmds.checkBox("checkbox_assign_girl_shading", query = True, value = True)):
        assign_shading_girl()
        print "GIRL SHADING ASSIGNMENT COMPLETE"

    if (cmds.checkBox("checkbox_assign_girl_hair_shading", query = True, value = True)):
        assign_shading_girl_hair(2)
        print "GIRL HAIR SHADING ASSIGNMENT COMPLETE"

    if (cmds.checkBox("checkbox_assign_bag_shading", query = True, value = True)):
        assign_shading_bag()
        print "BAG SHADING ASSIGNMENT COMPLETE"

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
    cmds.checkBox("checkbox_assign_girl_shading", height=buttonSize[1], label = "assign_girl_shading", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_assign_girl_hair_shading", height=buttonSize[1], label = "assign_girl_hair_shading", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_assign_bag_shading", height=buttonSize[1], label = "assign_bag_shading", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_create_default_aovs", height=buttonSize[1], label = "create_default_aovs", value = 0, parent = "mainColumn")
    cmds.checkBox("checkbox_create_custom_aovs", height=buttonSize[1], label = "create_custom_aovs", value = 0, parent = "mainColumn")
    # cmds.checkBox("checkbox_create_curvecollectors_boots", height=buttonSize[1], label = "create_curvecollectors_boots", value = 0, parent = "mainColumn")
    # cmds.checkBox("checkbox_create_curvecollectors_bra", height=buttonSize[1], label = "create_curvecollectors_bra", value = 0, parent = "mainColumn")
    cmds.button( label='Execute', height=buttonSize[1], parent = "mainColumn", command=("execute()"))


    cmds.showWindow( windowName )

    gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    cmds.window( windowName, edit=True, widthHeight=(windowSize[0], windowSize[1]) )



window()