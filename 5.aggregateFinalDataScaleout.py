# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Aggregate all final data to the same folder for Scaleout
# *********************************************************************************

import os
from joblib import Parallel, delayed
import numpy as np 
import shutil
import SimpleITK as sitk
import nibabel as nibabel

#from ioDataMethods import ioDataMethodsClass
from commonConfig import commonConfigClass
#from convertDataMethods import convertDataMethodsClass

# Init needed class instances
#ioData = ioDataMethodsClass()           # Class for handling and reading data 
conf = commonConfigClass()              # Init config class
#convertData = convertDataMethodsClass() # Functions for converting DICOM to Nifti data



def convertNiiGzToNii(folderPath):
    """
    Convert all nii.gz files to nii so it will be faster to load them during training and inference
    """    
    # Get list of all nii.gz files in the folder
    niiGzFiles = [f for f in os.listdir(folderPath) if f.endswith('.nii.gz')]
    # Loop over all nii.gz files
    for niiGzFile in niiGzFiles:
        # Get file path
        filePath = os.path.join(folderPath, niiGzFile)
        # Read file
        image = nibabel.load(filePath)
        # Write file to nii without compression
        nibabel.save(image, filePath.replace('.nii.gz', '.nii'))
        # Remove the nii.gz file
        os.remove(filePath)



# ### SCRIPT STARTS HERE ###
print('Aggregating Nifti data to final location for Scaleout')

# Make sure the final data folder  preProcess.finalAggregatedDataDir exists
if not os.path.isdir(conf.preProcess.finalAggregatedDataDirScaleout):
    # Create dir
    os.makedirs(conf.preProcess.finalAggregatedDataDirScaleout, exist_ok=True)
# Copy the folder "train" from conf.preProcess.outputNiftiPatientDirFinalResampledStacked to conf.preProcess.finalAggregatedDataDir
shutil.copytree(os.path.join(conf.preProcess.outputNiftiPatientDirFinalResampledStacked, 'train'), os.path.join(conf.preProcess.finalAggregatedDataDirScaleout, 'train'), dirs_exist_ok=True)

# Convert all nii.gz to nii so it will be faster to load them during training and inference
# Images
convertNiiGzToNii(os.path.join(conf.preProcess.finalAggregatedDataDirScaleout, 'train', 'images'))
# Labels
convertNiiGzToNii(os.path.join(conf.preProcess.finalAggregatedDataDirScaleout, 'train', 'labels'))


# Print message
print('Aggregating and converting final data is complete!')

