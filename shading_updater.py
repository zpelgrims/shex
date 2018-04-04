import maya.cmds as cmds
import pymel.core as pm

import os
from os import listdir
from os.path import isfile, join

import re
import json
from functools import partial




def get_top_level_grp(reference_name):

    return cmds.textField("textfield_name_" + reference_name, query=True, text=True)


def load_json():

    filename = str(cmds.fileDialog2(fileFilter="*.json", fileMode=1, dialogStyle=1)[0])
    return json.load(open(filename))


def apply_attributes(shape_node, shading_json, namespace):

    for i in shading_json[shape_node]["arnold_attributes"]:
        cmds.setAttr(namespace + shape_node + "." + i, shading_json[shape_node]["arnold_attributes"][i])


def apply_curve_attributes(shape_node, shading_json, shape_namespace, shaders_namespace):

    for i in shading_json[shape_node]["arnold_attributes"]:
        if (i == "curve_shader"):
            cmds.connectAttr(shaders_namespace + shading_json[shape_node]["arnold_attributes"][i][0] + ".outColor", shape_namespace + shape_node + ".aiCurveShader", force=True)
        elif (i == "curve_width"):
            if ( shading_json[shape_node]["arnold_attributes"][i] != None ):
                cmds.connectAttr(shaders_namespace + shading_json[shape_node]["arnold_attributes"][i][0] + ".outAlpha", shape_namespace + shape_node + ".aiCurveWidth", force=True)
        else:
            cmds.setAttr(shape_namespace + shape_node + "." + i, shading_json[shape_node]["arnold_attributes"][i])


def apply_shaders(shape_node, shading_json, object_namespace, shader_namespace):

    for i in shading_json[shape_node]["shaders"]:
        for j in range(0, len(shading_json[shape_node]["shaders"][i])):
            cmds.select(object_namespace + str(shading_json[shape_node]["shaders"][i][j]), replace=True)
            cmds.hyperShade(assign = shader_namespace + str(i))



def get_shapes(top_level_group):

    shapes_list = cmds.ls(top_level_group, dag=True, geometry=True)
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


def apply_json(shaders_namespace, top_level_group):

    shading_json = load_json()
    shapes_list = get_shapes(top_level_group)

    bool_apply_arnold_attributes = True
    bool_apply_shaders = True

    shaders_namespace = shaders_namespace[:-2] + str(":")

    object_in_namespace = ""


    for shape in shapes_list:
        
        # find object namespace
        cmds.select(shape)
        object_namespace = pm.selected()[0].namespace()

        # find shape namespace
        object_in_namespace = shape.rpartition(':')[0]
        # remove shape namespace
        shape_namespace_stripped = shape.replace(object_in_namespace, "")
        # remove colon
        shape_namespace_stripped = shape_namespace_stripped[1:]


        # query data type
        datatype = str(cmds.objectType(shape))
        
        # check if shape in scene exists as shape in json
        if shape_namespace_stripped in shading_json:
            if bool_apply_arnold_attributes:
                if (datatype != "nurbsCurve"):
                    apply_attributes(shape_namespace_stripped, shading_json, object_namespace)
                else: #special treatment for nurbs curves
                    apply_curve_attributes(shape_namespace_stripped, shading_json, object_namespace, shaders_namespace)
                print "SHADING ATTRIBUTES APPLIED >>", shape
            
            if bool_apply_shaders:
                if (datatype != "nurbsCurve"):
                    apply_shaders(shape_namespace_stripped, shading_json, object_namespace, shaders_namespace)
                print "SHADERS APPLIED >>", shape

    """
    # check which objects still have the initialshadinggroup assigned
    for shape in shapes_list:
        datatype = str(cmds.objectType(shape))
        if (datatype != "nurbsCurve"):
            shading_groups = cmds.listConnections(shape, type='shadingEngine')
            shaders = cmds.ls(cmds.listConnections(shading_groups), materials=1)

            for i in shading_groups:
                if (i == "initialShadingGroup"):
                    print "SHADING IMPORT WARNING: initialShadingGroup still assigned to >>", shape
    """

    print "ALL SHADERS APPLIED"




    
def get_reference_version(reference_name):
   
    reference_path = str(cmds.referenceQuery(reference_name, filename=True, withoutCopyNumber=True))
    folder_path_list = reference_path.rsplit('/', -1)
    full_folder_path = ""
    
    for k in range(0, len(folder_path_list) - 1):
        full_folder_path += folder_path_list[k] + "/"
    
    reference_name = reference_path.rsplit('/', 1)[-1]
    reference_version_number = reference_name.rsplit("_", -1)[-1]
    
    # strip all non-digits
    reference_stripped_version_number = int(re.sub("\D", "", reference_version_number))

    return [reference_stripped_version_number, full_folder_path]


def get_folder_latest_version(full_folder_path, filetype):
    
    # get all .ma files in folder
    folder_maya_files_list = [f for f in listdir(full_folder_path) if isfile(join(full_folder_path, f)) and f.endswith(filetype)]

    folder_latest_file_version = 0
    folder_latest_file_path = ""

    for j in folder_maya_files_list:
        version_number = j.rsplit("_", -1)[-1]
        
        # catch e.g v003_test.ma exceptions
        try:
            # strip all non-digits
            stripped_version_number = int(re.sub("\D", "", version_number))
        except ValueError:
            continue
        
        if stripped_version_number > folder_latest_file_version:
            folder_latest_file_version = stripped_version_number
            folder_latest_file_path = full_folder_path + j
    
    return [folder_latest_file_version, folder_latest_file_path]




def reload_reference(reference_name, latest_version_path, *args):

    cmds.file(unloadReference=reference_name)
    cmds.file(cleanReference=reference_name)
    cmds.file(latest_version_path, loadReference=reference_name)
    
    # assign json
    apply_json(reference_name, get_top_level_grp(reference_name))

    # update window
    window()


def replace_reference(reference_name, latest_version_path, *args):

    cmds.file(latest_version_path, loadReference=reference_name)

    # assign json
    apply_json(reference_name, get_top_level_grp(reference_name))

    # update window
    window()



def window():
    
    windowName = "shading_reference_versions"
    windowSize = (600, 300)
    buttonSize = (100, 20)
    spacing = [(1,20), (2,20), (3,20), (4,20), (5,20), (6,20)]


    if (cmds.window(windowName , exists=True)):
        cmds.deleteUI(windowName)
    window = cmds.window( windowName, title= windowName, sizeable=True)
    cmds.rowColumnLayout( numberOfColumns=6, columnWidth=[(1, 200), (2, 300), (3, 50), (4, 50), (5, 150), (6, 150)], rowSpacing=spacing, columnSpacing=spacing)
    
    
    cmds.text( label="Alembic cache top level node", align='center' )
    cmds.text( label="Reference name", align='center' )
    cmds.text( label="Current", align='right' )
    cmds.text( label="Latest", align='right' )
    cmds.text( label="Keep edits", align='center' )
    cmds.text( label="Lose edits", align='center' )
    
    reference_list = cmds.ls(references=True)
    
    for i in reference_list:

        # filter out non-shading references
        if "had" not in i:
            continue

        reference_version = get_reference_version(i)
        folder_latest_version = get_folder_latest_version(reference_version[1], ".ma")

        textfield_name = "textfield_name_" + str(i)
        cmds.textField(textfield_name, text='')

        out_of_date = False
        if reference_version[0] < folder_latest_version[0]:
            out_of_date = True
        
        if out_of_date:
            cmds.button( label=i, enable=False, bgc=[1, .2, .2] )
        else:
            cmds.button( label=i, enable=False, bgc=[0, 1, .5])
        
        cmds.text( label=reference_version[0], align='right' )
        cmds.text( label=folder_latest_version[0], align='right' )

        cmds.button( label="Replace and Update", enable=True, command=partial(replace_reference, i, folder_latest_version[1]))
        cmds.button( label="Reload and Update", enable=True, command=partial(reload_reference, i, folder_latest_version[1]))





    cmds.showWindow( windowName )

    gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    cmds.window( windowName, edit=True )



window()
