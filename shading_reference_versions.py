import maya.cmds as cmds
import os
from os import listdir
from os.path import isfile, join
import re

    
def get_reference_version(reference_name):
   
    reference_path = str(cmds.referenceQuery(reference_name, filename=True))
    folder_path_list = reference_path.rsplit('/', -1)
    full_folder_path = ""
    
    for k in range(0, len(folder_path_list) - 1):
        full_folder_path += folder_path_list[k] + "/"
    
    reference_name = reference_path.rsplit('/', 1)[-1]
    reference_version_number = reference_name.rsplit("_", -1)[-1]
    
    # strip all non-digits
    reference_stripped_version_number = int(re.sub("\D", "", reference_version_number))

    return [reference_stripped_version_number, full_folder_path]


def get_folder_latest_version(full_folder_path):
    
    # get all .ma files in folder
    folder_maya_files_list = [f for f in listdir(full_folder_path) if isfile(join(full_folder_path, f)) and f.endswith(".ma")]

    folder_latest_file_version = 0
    
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
    
    return folder_latest_file_version


def window():
    
    windowName = "shading_reference_versions"
    windowSize = (600, 300)
    buttonSize = (100, 20)
    spacing = [(1,20), (2,20), (3,20)]


    if (cmds.window(windowName , exists=True)):
        cmds.deleteUI(windowName)
    window = cmds.window( windowName, title= windowName, sizeable=True)
    cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1, 300), (2, 50), (3, 50)], rowSpacing=spacing, columnSpacing=spacing)
    
    
    cmds.text( label="Reference name", align='center' )
    cmds.text( label="Current", align='right' )
    cmds.text( label="Latest", align='right' )
    
    reference_list = cmds.ls(references=True)
    
    for i in reference_list:

        # filter out non-shading references
        if "had" not in i:
            continue

        reference_version = get_reference_version(i)
        folder_latest_version = get_folder_latest_version(reference_version[1])      

            
        if reference_version[0] < folder_latest_version:
            cmds.button( label=i, enable=False, bgc=[1, .2, .2] )
        else:
            cmds.button( label=i, enable=False, bgc=[0, 1, .5])
            
        
        cmds.text( label=reference_version[0], align='right' )
        cmds.text( label=folder_latest_version, align='right' )


    cmds.showWindow( windowName )

    gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    cmds.window( windowName, edit=True )



window()