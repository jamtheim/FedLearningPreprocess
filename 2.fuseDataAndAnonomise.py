# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Fuses data from MICE and pre-processed data from the Nifti structures
# Outpit is directories with anonymized data in the final data location
# *********************************************************************************

import os
from joblib import Parallel, delayed
import numpy as np 
import shutil
import SimpleITK as sitk

from ioDataMethods import ioDataMethodsClass
from commonConfig import commonConfigClass
from convertDataMethods import convertDataMethodsClass

# Init needed class instances
ioData = ioDataMethodsClass()           # Class for handling and reading data 
conf = commonConfigClass()              # Init config class
convertData = convertDataMethodsClass() # Functions for converting DICOM to Nifti data


# Remove the folder FinalAndAnon in conf.preProcess.outputNiftiPatientDir if it exists
# This is done so we start with a clean plate every run
if os.path.isdir(conf.preProcess.outputNiftiPatientDirFinal):
    # Remove the folder
    shutil.rmtree(conf.preProcess.outputNiftiPatientDirFinal)

# Remove the folder FinalAndAnonResampled in conf.preProcess.outputNiftiPatientDir if it exists
# This is done so we start with a clean plate every run
if os.path.isdir(conf.preProcess.outputNiftiPatientDirFinalResampled):
    # Remove the folder
    shutil.rmtree(conf.preProcess.outputNiftiPatientDirFinalResampled)


# Print info
print('Fusing data from MICE and pre-processed data from the Nifti structures')
print('This is from the ' + str(conf.preProcess.study) + ' study')

# List patients in preProcess.outputNiftiPatientDir 
patFolders = os.listdir(conf.preProcess.outputNiftiPatientDir)
# Only include folders in the listing
patFolders = [x for x in patFolders if os.path.isdir(os.path.join(conf.preProcess.outputNiftiPatientDir, x))]

# Loop over patFolders
for patIndex, patient in enumerate(patFolders):
    # Get the first part of the patient name as this is the anon patient number (study index)
    patStudyIndex = patient.split('_')[0]
    # Get the last part of the patient as this is the real patient ID
    # This is used to match the MICE data down below
    patID = patient.split('_')[-1]
    # Copy the patient folder and change the name to ony include the study index
    shutil.copytree(os.path.join(conf.preProcess.outputNiftiPatientDir, patient), os.path.join(conf.preProcess.outputNiftiPatientDirFinal, patStudyIndex))

    # Change the name of image.nii.gz to sCT_image.nii.gz if we are using treatment study data. For validation change it to Image CT.nii.gz
    if conf.preProcess.study == 'Treatment': 
        shutil.move(os.path.join(conf.preProcess.outputNiftiPatientDirFinal, patStudyIndex, 'image.nii.gz'), os.path.join(conf.preProcess.outputNiftiPatientDirFinal, patStudyIndex, 'image sCT.nii.gz'))
    if conf.preProcess.study == 'Validation': 
        shutil.move(os.path.join(conf.preProcess.outputNiftiPatientDirFinal, patStudyIndex, 'image.nii.gz'), os.path.join(conf.preProcess.outputNiftiPatientDirFinal, patStudyIndex, 'image CT.nii.gz'))

    # Save anon patient folder path in a variable
    patFolderAnon = os.path.join(conf.preProcess.outputNiftiPatientDirFinal, patStudyIndex)

    # Copy over correspoding MICE data to the final data location 
    # Get the MICE patient data folder by matching the patID
    patFolderMICE = [x for x in os.listdir(conf.base.dataFolderMICE) if patID in x]
    # Make sure only one folder is found in the matching
    if len(patFolderMICE) == 0:
        print('Error: No MICE patient folder found for patient: ', patID)
        print('Hence, not copied over to final data location as data is missing')
        # Detele the anonomized patient folder
        shutil.rmtree(patFolderAnon)
    elif len(patFolderMICE) > 1:
        print('Error: More than one MICE patient folder found for patient: ', patID)
        print('Please check why this is the case and remove the extra folder(s)')
        print(patFolderMICE)
        print('Exiting...')
        exit()
    elif len(patFolderMICE) == 1:
        # Define the corresponding patient data folder path in MICE data
        patFolderMICE = os.path.join(conf.base.dataFolderMICE, patFolderMICE[0])
        # List dirs in this folder (there should be one subfolder with date)
        patSubFolderMICE = os.listdir(patFolderMICE)
        # Make sure there are only one folder
        if len(patSubFolderMICE) != 1:
            print('Error: More than one MICE patient subfolder found for patient: ', patID)
            print(patSubFolderMICE)
            print('Exiting...')
            exit()
        # Get path of the only directory
        PATH_patSubFolderMICE = os.path.join(patFolderMICE, patSubFolderMICE[0])
        # Copy all the Nifti files from the MICE data to the final data location
        # Loop over all files in the MICE data folder
        for file in os.listdir(PATH_patSubFolderMICE):
            # Check if file is a Nifti file
            if '.nii.gz' in file:
                # Copy the file to the final data location
                shutil.copy(os.path.join(PATH_patSubFolderMICE, file), os.path.join(patFolderAnon, file))

        # Count number of files in patFolderAnon after copying over MICE data
        numFiles = len(os.listdir(patFolderAnon))
        # Make sure there are X number of files in the folder
        if conf.preProcess.study == 'Treatment': 
            assert numFiles >= 18, 'Error: Number of files in patient folder is bellow 18!' # Can still be mutiple targets 
            if numFiles != 18:
                print('Warning: Number of files in patient folder is not 18!')
                print('Number of files: ', numFiles)
                print('Subject: ', patFolderAnon)
                print('Check for multiple targets and correct if needed')
        
        if conf.preProcess.study == 'Validation': # No sCT here, there fore one less file
            assert numFiles >= 17, 'Error: Number of files in patient folder below 17!' # Can still be mutiple targets 
            if numFiles != 17:
                print('Warning: Number of files in patient folder is not 17!')
                print('Number of files: ', numFiles)
                print('Subject: ', patFolderAnon)
                print('Check for multiple targets and correct if needed')

# Print message
print('Fuse and anomymization of training data is complete!')
