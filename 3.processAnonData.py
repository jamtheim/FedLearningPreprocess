# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Process all Nifti data. Actions like Resampling, cropping, padding and defacing. 
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
    # Process Nifti data and interpolate to chosen spatial resolution. Also cut, pad and deface data. 
    convertData.processNiftiData(patNr, patient, conf.preProcess.outputNiftiPatientDirFinal, conf.preProcess.outputNiftiPatientDirFinalResampled)


# ### SCRIPT STARTS HERE ###
print('Resampling Nifti structures, cropping and padding')
print('This is from the ' + str(conf.preProcess.study) + ' study')

# Remove the folder FinalAndAnonResampled in conf.preProcess.outputNiftiPatientDir if it exists
# This is done so we start with a clean plate every run
if os.path.isdir(conf.preProcess.outputNiftiPatientDirFinalResampled):
    # Remove the folder
    shutil.rmtree(conf.preProcess.outputNiftiPatientDirFinalResampled)

# Loop over all patient folders 
patFolders = os.listdir(conf.preProcess.outputNiftiPatientDirFinal)
# Only include folder
patFolders = [x for x in patFolders if os.path.isdir(os.path.join(conf.preProcess.outputNiftiPatientDirFinal, x))]
# Make sure the output Nifti directory exists
if not os.path.isdir(conf.preProcess.outputNiftiPatientDirFinalResampled):
    # Create dir
    os.makedirs(conf.preProcess.outputNiftiPatientDirFinalResampled, exist_ok=True)

# Set number of CPU threads to use
nrCPU = 1
# Init parallell job for resampling the Nifti data
patInfo = Parallel(n_jobs=nrCPU, verbose=10)(delayed(patLargeDataLoop)(patNr, patient) for patNr, patient in enumerate(patFolders))
     
# Print message
print('Resampling of training data is complete!')

