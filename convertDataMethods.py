# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Class for converting data from DICOM to Nifti format
# *********************************************************************************

import os
import cv2
import numpy as np
import os.path
import nibabel
import nibabel.processing
import SimpleITK as sitk
import pydicom
import scipy
from dcmrtstruct2nii import dcmrtstruct2nii, list_rt_structs
import shutil
from datetime import datetime, timedelta
from joblib import Parallel, delayed
from commonConfig import commonConfigClass
# Load configuration
conf = commonConfigClass() 


class convertDataMethodsClass:
    """
    Class describing functions needed for converting DICOM data to Nifti data
    """

    def __init__ (self):
        """
        Init function
        """
        pass


    def selectSubfolder_CT(self, root_folder, target_name, forbidden_word):
        """
        Select CT subfolder based on target name and forbidden word
        """
        selectedFolder = []
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for folder in dirnames:
                if target_name in folder and forbidden_word not in folder:
                    selectedFolder.append(os.path.join(dirpath, folder))
        
        # Make sure there is only one folder selected
        assert len(selectedFolder) == 1, 'There should only be one folder selected'
        selectedFolder = selectedFolder[0]
        return selectedFolder


    def selectSubfolder_sCT(self, root_folder, target_name):
        """
        Select sCT subfolder based on target name 
        """
        selectedFolder = []
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for folder in dirnames:
                if target_name in folder:
                    selectedFolder.append(os.path.join(dirpath, folder))
        
        # Make sure there is only one folder selected
        assert len(selectedFolder) == 1, 'There should only be one folder selected'
        # Count number of folders in this folder
        subfolderInSelected = [f.path for f in os.scandir(selectedFolder[0]) if f.is_dir()]
        assert len(subfolderInSelected) == 1, 'There should only be one subfolder in selected folder'
        # Set path to subfolder
        selectedFolder = subfolderInSelected[0]      
        return selectedFolder


    def resampleNiftiData(self, i_subject, subject, dataInBasePath, dataOutBasePath):
        """
        Resample Nifti data to chosen spatial resolution

        Args:
            i_subject (int): The current subject number
            subject (str): The current subject name
            dataInBasePath (str): The base path to the input dataset
            dataOutBasePath (str): The base path to the output dataset
            
        Returns:
            Outputs data to directory 
        """
        # Assess input
        assert isinstance(i_subject, int), 'Input i_subject must be an integer'
        assert isinstance(subject, str), 'Input subject must be a string'
        assert isinstance(dataInBasePath, str), 'Input dataInBasePath must be a string'
        assert isinstance(dataOutBasePath, str), 'Input dataInBasePath must be a string'
        # Assert existing directories
        assert os.path.isdir(dataInBasePath), 'Input dataInBasePath must be a directory'
        assert os.path.isdir(dataOutBasePath), 'Input dataOutBasePath must be a directory'
        # Get the subject folder path 
        subjectFolderPath = os.path.join(dataInBasePath, subject)
        # List all files and make sure they are all Nifti
        subjectFiles = [f for f in os.listdir(subjectFolderPath) if os.path.isfile(os.path.join(subjectFolderPath, f))]
        for subjectFile in subjectFiles:
            assert subjectFile.endswith('.nii.gz'), 'All files in subject folder must be Nifti'
        # Define subject output folder
        subjectOutFolderPath = os.path.join(dataOutBasePath, subject)
        # Make sure output folder exists
        os.makedirs(subjectOutFolderPath, exist_ok=True)
        # Resample each Nifti file in subjectFiles to chosen spatial resolution and save to subjectOutFolderPath
        for subjectFile in subjectFiles:
            # Read Nifti file
            subjectFilePath = os.path.join(subjectFolderPath, subjectFile)
            subjectData = nibabel.load(subjectFilePath)
            # Resample to chosen spatial resolution
            reSampledSubjectData = nibabel.processing.resample_to_output(subjectData, voxel_sizes=conf.preProcess.voxelSize, order=3, mode='constant', cval=0.0)
            # Save data to subjectOutFolderPath
            subjectOutFilePath = os.path.join(subjectOutFolderPath, subjectFile)
            nibabel.save(reSampledSubjectData, subjectOutFilePath)
            

    def DicomRT2Nifti(self, i_subject, subject, dataInBasePath, dataOutBasePath):
        """
        Convert subject DICOM CT and struct data to Nifty format

        Args:
            i_subject (int): The current subject number
            subject (str): The current subject name
            dataInBasePath (str): The base path to the DICOM dataset
            dataOutBasePath (str): The base path to the Nifti dataset
            
        Returns:
            Outputs data to directory 
            
        """
        # Assess input
        assert isinstance(i_subject, int), 'Input i_subject must be an integer'
        assert isinstance(subject, str), 'Input subject must be a string'
        assert isinstance(dataInBasePath, str), 'Input dataInBasePath must be a string'
        assert isinstance(dataOutBasePath, str), 'Input dataInBasePath must be a string'
        # Assert existing directories
        assert os.path.isdir(dataInBasePath), 'Input dataInBasePath must be a directory'
        os.makedirs(dataOutBasePath, exist_ok=True)
        assert os.path.isdir(dataOutBasePath), 'Input dataOutBasePath must be a directory'
        # Get the CT and RT struct file and path 
        subjectFolderPath = os.path.join(dataInBasePath, subject)
        # Find subjectCTFolderPath
        if conf.preProcess.study == 'Validation':
            subjectCTFolderPath = self.selectSubfolder_CT(os.path.join(subjectFolderPath, 'CT'), 'Skalle__2_0__H30s', 'iMAR')
        elif conf.preProcess.study == 'Treatment':
            subjectCTFolderPath = self.selectSubfolder_sCT(os.path.join(subjectFolderPath, 'CT'), 'sCT')

        #print(subjectCTFolderPath)
        # Find subject RT struct File
        subjectStructFile = self.getRTStructFile(os.path.join(subjectFolderPath, conf.preProcess.RTstructFolderFirst, conf.preProcess.RTstructFolderSecond))
        subjectStructFilePath = os.path.join(subjectFolderPath, conf.preProcess.RTstructFolderFirst, conf.preProcess.RTstructFolderSecond, subjectStructFile)
        #print(subjectStructFilePath)
        # Define subject output folder
        subjectOutFolderPath = os.path.join(dataOutBasePath, subject)
        os.makedirs(subjectOutFolderPath, exist_ok=True)
        # Get list of all structures present in the DICOM structure file 
        subjectStructList = list_rt_structs(subjectStructFilePath)
        #print(subjectStructList)
        # Count number of structures
        #nrStructsinList = len(subjectStructList)

        # Lopp through each structure and check if the name contains any of the keywords defined 
        # in the config file. If so, add the structure to the list of structures to be converted.
        # This is done to be flexible in the naming of the structures.
        subjectStructList = [x for x in subjectStructList if any(word.lower() in x.lower() for word in conf.preProcess.structureNameKeywords)]
        # Run the list again but this time to exclude any structures that contain any of the keywords defined in exclude list
        subjectStructList = [x for x in subjectStructList if not any(word.lower() in x.lower() for word in conf.preProcess.structureNameExclude)]
        #print(subjectStructList)

        # Convert the RT structs to Nifty format 
        # This is performed by targeting each individual structure at a time in a loop. 
        # This is slower but safer. 
        # In this way we can isolate exceptions to individual structures and not break 
        # the process of dcmrtstruc2nii which happens otherwise. This avoids modification of the 
        # dcmrtstruc2nii source code and allows us in retrospect to see if missing data was important or not.
        # Failed objects are due to the fact that the structures are not completed or simply empty in Eclipse. 
        for structNr, currStruct in enumerate(subjectStructList):
            try:
                # Extract the structure and convert to Nifty
                # We do not want convert_original_dicom=True for all structures as this will add a lot of compute time. 
                # Do this only for BODY as this structure is always present. It has nothing to do with the structure itself for enabling convert_original_dicom=True. 
                if currStruct in conf.preProcess.bodyStructureName1 or currStruct in conf.preProcess.bodyStructureName2:
                    #print(subject)
                    dcmrtstruct2nii(subjectStructFilePath, subjectCTFolderPath, subjectOutFolderPath, structures=currStruct, gzip=True, mask_background_value=0, mask_foreground_value=1, convert_original_dicom=True)
                else:
                    # pass
                    #print(currStruct)
                    dcmrtstruct2nii(subjectStructFilePath, subjectCTFolderPath, subjectOutFolderPath, structures=currStruct, gzip=True, mask_background_value=0, mask_foreground_value=1, convert_original_dicom=True)
                
            except:
                print("Exception when extracting " + currStruct + ' for ' + subject )
        
        """
        # Get total number of files outputted
        nrFiles = len(os.listdir(subjectOutFolderPath))
        # If number of output files and in the list differ
        # -1 becuase of the image file that is created by dcmrtstruct2nii
        if nrFiles -1 != nrStructsinList:
            # Throw message   
            print('Number of output files and in the list differ for patient ' + subject )
            print(str(int(nrStructsinList-(nrFiles -1))) + ' structures were not extracted')
            print(subjectStructList)
            print(os.listdir(subjectOutFolderPath))
        """

        # Get content of output folder
        subjectOutFolderContent = os.listdir(subjectOutFolderPath)
        # For each item in the list of expected files check if the file is existing in the output folder
        # Set flags for presense of GTV and CTV
        # If any files are missing delete the subject folder and throw a message
        GTVpresent = False
        CTVpresent = False
        patDelete = False

        for currFile in conf.preProcess.structureFileNameExact:
            # Check if the file is in the output folder
            if currFile not in subjectOutFolderContent:
                # Throw message   
                #print('Structure ' + currFile + ' is missing for the ' + subject )
                # Set flag to delete the patient folder
                patDelete = True

        for currFile in subjectOutFolderContent:
            # Test readability of the Nifti file by loading it using simpleITK 
            data = sitk.ReadImage(os.path.join(subjectOutFolderPath, currFile))

            # Check that GTV and CTV are present
            if 'GTVT' in currFile:
                GTVpresent = True
            if 'CTVT' in currFile:
                CTVpresent = True


        # If GTV or CTV is not present (flag not changed)
        if GTVpresent == False: 
            # Throw message   
            #print('GTV is missing for the ' + subject )
             # Set flag to delete the patient folder
            patDelete = True
        if CTVpresent == False:
            # Throw message   
            #print('CTV is missing for the ' + subject )
            # Set flag to delete the patient folder
            patDelete = True


        # Delete patient if any files are missing
        if patDelete == True:
            # Delete patient folder
            shutil.rmtree(subjectOutFolderPath)
            # Throw message   
            print('Data for patient ' + subject + ' was deleted due to missing required files')
            #print(' ')
        else: 
            # Count number of GTVT files in the output folder
            nrGTVT = len([x for x in subjectOutFolderContent if 'GTVT' in x])
            # Count number of CTVT files in the output folder
            nrCTVT = len([x for x in subjectOutFolderContent if 'CTVT' in x])
            # If only one GTVT or CTVT file is present rename it to GTVT and CTVT
            if nrGTVT == 1:
                #print('Renaming GTVT for ' + subject + ' to mask_GTVT.nii.gz')
                os.rename(os.path.join(subjectOutFolderPath, [x for x in subjectOutFolderContent if 'GTVT' in x][0]), os.path.join(subjectOutFolderPath, 'mask_GTVT.nii.gz'))
            else: 
                # Throw message   
                print('Multiple GTVT files are present for the ' + subject )
                print('Manually resolve this!')
                print(' ')
            if nrCTVT == 1:
                #print('Renaming CTVT for ' + subject + ' to mask_CTVT.nii.gz')
                os.rename(os.path.join(subjectOutFolderPath, [x for x in subjectOutFolderContent if 'CTVT' in x][0]), os.path.join(subjectOutFolderPath, 'mask_CTVT.nii.gz'))
            else:
                # Throw message   
                print('Multiple CTVT files are present for the ' + subject )
                print('Manually resolve this!')
                print(' ')

        
        
    def getRTStructFile(self, path):
        """
        Search a given path for a RT structure DICOM file
        Inputs:
            path (str): Path to the DICOM file directory
        Returns:
            The RT file name
        """
        # Assert input
        assert isinstance(path, str), 'Input path must be a string'
        # Assert directory
        assert os.path.isdir(path), 'Input path must be a directory'
        # List files 
        files = os.listdir(path)
        # Get only the RS struct dicom file 
        structFile = [f for f in files if ".dcm" in f]
        #structFile = [f for f in files if "RS" in f]
        # Check that there is only one 
        if len(structFile) == 0:
            raise Exception('No RT structure file could be located. Make sure the file is located in the specified folder...')
        assert len(structFile) == 1
        # Return data 
        return structFile[0]
        


    