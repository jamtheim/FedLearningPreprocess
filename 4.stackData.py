# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Stack all Nifti data to multi channel format
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

# Function called from parallell loop
def patLargeDataLoop(patNr, patient):
    """
    Arg:
        patNr (int): The current patient number
        patient (str): The current patient name            

    Returns:
        Outputs data to directory         
    
    """
    # Stack Nifti data
    convertData.stackNiftiData(patNr, patient, conf.preProcess.outputNiftiPatientDirFinalResampled, conf.preProcess.outputNiftiPatientDirFinalResampledStacked)


# ### SCRIPT STARTS HERE ###
print('Stacking Nifti structures')
print('This is from the ' + str(conf.preProcess.study) + ' study')

# Remove the folder FinalAndAnonResampledStacked in conf.preProcess.outputNiftiPatientDir if it exists
# This is done so we start with a clean plate every run
if os.path.isdir(conf.preProcess.outputNiftiPatientDirFinalResampledStacked):
    # Remove the folder
    shutil.rmtree(conf.preProcess.outputNiftiPatientDirFinalResampledStacked)

# Loop over all patient folders 
patFolders = os.listdir(conf.preProcess.outputNiftiPatientDirFinal)
# Only include folder
patFolders = [x for x in patFolders if os.path.isdir(os.path.join(conf.preProcess.outputNiftiPatientDirFinal, x))]
# Make sure the output Nifti directory exists
if not os.path.isdir(conf.preProcess.outputNiftiPatientDirFinalResampledStacked):
    # Create dir
    os.makedirs(conf.preProcess.outputNiftiPatientDirFinalResampledStacked, exist_ok=True)

# Set number of CPU threads to use
nrCPU = 20
# Init parallell job for resampling the Nifti data
patInfo = Parallel(n_jobs=nrCPU, verbose=10)(delayed(patLargeDataLoop)(patNr, patient) for patNr, patient in enumerate(patFolders))
     
# Print message
print('Stacking of training data is complete!')

