# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Aggregate all final data to the same folder
# *********************************************************************************

import os
from joblib import Parallel, delayed
import numpy as np 
import shutil
import SimpleITK as sitk

#from ioDataMethods import ioDataMethodsClass
from commonConfig import commonConfigClass
#from convertDataMethods import convertDataMethodsClass

# Init needed class instances
#ioData = ioDataMethodsClass()           # Class for handling and reading data 
conf = commonConfigClass()              # Init config class
#convertData = convertDataMethodsClass() # Functions for converting DICOM to Nifti data


# ### SCRIPT STARTS HERE ###
print('Aggregating Nifti data to final location')

# Make sure the final data folder  preProcess.finalAggregatedDataDir exists
if not os.path.isdir(conf.preProcess.finalAggregatedDataDir):
    # Create dir
    os.makedirs(conf.preProcess.finalAggregatedDataDir, exist_ok=True)
# Copy the folder "train" from conf.preProcess.outputNiftiPatientDirFinalResampledStacked to conf.preProcess.finalAggregatedDataDir
shutil.copytree(os.path.join(conf.preProcess.outputNiftiPatientDirFinalResampledStacked, 'train'), os.path.join(conf.preProcess.finalAggregatedDataDir, 'train'), dirs_exist_ok=True)

# Print message
print('Aggregating final data is complete!')

