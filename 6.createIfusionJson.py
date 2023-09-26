# *********************************************************************************
# Author: Anders Eklund, Lindköping University 

# Modified by Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Create JSON file for Ifusion training
# This script assumes that all Nifti files, for image data and GT annotations, 
# are stored in one directory for all patients, with a unique patient string per patient. 
# *********************************************************************************

# NOT READY YET! 

import os
from joblib import Parallel, delayed
import numpy as np 
import SimpleITK as sitk
import random
import glob
import json

#from ioDataMethods import ioDataMethodsClass
from commonConfig import commonConfigClass
#from convertDataMethods import convertDataMethodsClass

# Init needed class instances
#ioData = ioDataMethodsClass()           # Class for handling and reading data 
conf = commonConfigClass()              # Init config class
#convertData = convertDataMethodsClass() # Functions for converting DICOM to Nifti data


def create_dataset_json_onesite(root_dir, output_file, validation_percent=0.2):
    dataset = {"training": [], "validation": []}
    file_list = []

    # Get one filename per subject
    subject_list = glob.glob(os.path.join(root_dir, 'train', 'images') + '/' + '*.nii.gz') 
    print(subject_list)

    # Loop over subjects
    for file in subject_list:
        print(file)
        file_list.append({
            "image": [
                 file,
                 file.replace("T2_FLAIR", "T1"),
                 file.replace("T2_FLAIR", "T1_GD"),
                 file.replace("T2_FLAIR", "T2_GD")
            ],
            "label": file.replace("MR_T2_FLAIR", "seg")
           })

    print(file_list)

    random.shuffle(file_list)
    # Use subset as validation
    num_validation = int(len(file_list) * validation_percent)
    dataset["training"] = file_list[:-num_validation]
    dataset["validation"] = file_list[-num_validation:]

    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=4)

        
# Example usage
root_directory = conf.preProcess.finalAggregatedDataDir
output_json_file = os.path.join(root_directory, conf.preProcess.site  + ".json")
# Create json file
create_dataset_json_onesite(root_directory, output_json_file)
