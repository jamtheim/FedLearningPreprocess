# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Pre-process data to export all structures 
# *********************************************************************************

import os
from joblib import Parallel, delayed
import multiprocessing
import numpy as np 
import matplotlib.pyplot as plt
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
    #print(patient)
    # Convert Dicom to Nifti
    convertData.DicomRT2Nifti(patNr, patient, conf.preProcess.inputDicomPatientDir, conf.preProcess.outputNiftiPatientDir)

    


# ### SCRIPT STARTS HERE ###
# Print info
print('Extracting Nifti structures')
print('This is from the ' + str(conf.preProcess.study) + ' study')
# Loop over all patient folders and convert DICOM to Nifti
# List patients
patFolders = os.listdir(conf.preProcess.inputDicomPatientDir)
# Only include folder
patFolders = [x for x in patFolders if os.path.isdir(os.path.join(conf.preProcess.inputDicomPatientDir, x))]
# Make sure the output Nifti directory exists
if not os.path.isdir(conf.preProcess.outputNiftiPatientDir):
    # Create dir
    os.makedirs(conf.preProcess.outputNiftiPatientDir, exist_ok=True)

# Set number of CPU threads to use
#nrCPU = multiprocessing.cpu_count()-2
nrCPU = 20

# Init parallell job for converting DICOM to Nifti 
patInfo = Parallel(n_jobs=nrCPU, verbose=10)(delayed(patLargeDataLoop)(patNr, patient) for patNr, patient in enumerate(patFolders))


     
# Print message
print('Pre-processing for training data is complete!')
