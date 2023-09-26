# *********************************************************************************
# Author: Anders Eklund, Lindköping University 
# Modified by Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Create JSON file for Ifusion training
# This script assumes that all nifti files (for T1, T1 GD, T2 GD, T2 FLAIR, seg (annotations)) are stored in one directory for all patients, with a unique patient string per patient, e.g.
# *********************************************************************************

import os
from joblib import Parallel, delayed
import numpy as np 
import SimpleITK as sitk
import random
import glob
import json
import shutil

#from ioDataMethods import ioDataMethodsClass
from commonConfig import commonConfigClass
#from convertDataMethods import convertDataMethodsClass

# Init needed class instances
#ioData = ioDataMethodsClass()           # Class for handling and reading data 
conf = commonConfigClass()              # Init config class
#convertData = convertDataMethodsClass() # Functions for converting DICOM to Nifti data


def create_dataset_json_onesite(root_dir, output_file, validation_percent=0.2):
    """
    Create a JSON file for a dataset with one site
    """
    dataset = {"training": [], "validation": []}
    file_list = []

    # Get one filename per subject
    #subject_list = glob.glob(root_dir + 'MR_T2_FLAIR*defaced*.nii.gz')
    subject_list = glob.glob(root_dir + '/*_seg.nii.gz')

    # Loop over subjects
    for file in subject_list:
        #print(file)
        file_list.append({
            "image": [
                 file.replace("_seg", "_image_T2_tra_flair_fs"),
                 file.replace("_seg", "_image_T1_tra"),
                 file.replace("_seg", "_image_T1_tra_GD"),
                 file.replace("_seg", "_image_T2_tra_GD")
            ],
            "label": file
           })

    # print(file_list)

    random.shuffle(file_list)
    # Use subset as validation
    num_validation = int(len(file_list) * validation_percent)
    dataset["training"] = file_list[:-num_validation]
    dataset["validation"] = file_list[-num_validation:]

    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=4)


# ### SCRIPT STARTS HERE ###
print('Aggregating Nifti data to final location for Ifusion')
# Make sure the final data folder preProcess.finalAggregatedDataDir exists
if not os.path.isdir(conf.preProcess.finalAggregatedDataDirIfusion):
    # Create dir
    os.makedirs(conf.preProcess.finalAggregatedDataDirIfusion, exist_ok=True)

# Loop over all patient folders in conf.preProcess.outputNiftiPatientDirFinalResampledStacked, 'train', 'labels'
# We choose this directory as we know that the patients in that directory is complete 
patFiles = os.listdir(os.path.join(conf.preProcess.outputNiftiPatientDirFinalResampledStacked, 'train', 'labels'))

for fileNr, patFile in enumerate(patFiles):
    # Get patient string
    patient = patFile.split('_')[0]
    # Copy the file to conf.preProcess.finalAggregatedDataDirIfusion
    shutil.copyfile(os.path.join(conf.preProcess.outputNiftiPatientDirFinalResampledStacked, 'train', 'labels', patFile), os.path.join(conf.preProcess.finalAggregatedDataDirIfusion, patFile))
    
    # Access the image files in conf.preProcess.ImageFileNameStack
    # Loop over all image files
    for fileName in conf.preProcess.ImageFileNameStack: 
        # Get full file path
        filePathSource = os.path.join(conf.preProcess.outputNiftiPatientDirFinalResampled, patient, fileName) # Note that we get the files from the image folder
        # Define new file name without spaces 
        newFileName = fileName.replace(' ', '_')
        # Rename file to include patient string and copy to conf.preProcess.finalAggregatedDataDirIfusion
        filePathTarget = os.path.join(conf.preProcess.finalAggregatedDataDirIfusion, patient + '_' + newFileName)
        # Copy the file
        shutil.copyfile(filePathSource, filePathTarget)
        

# Create needed JSON file for Ifusion training       
root_directory = conf.preProcess.finalAggregatedDataDirIfusion
output_json_file = os.path.join(root_directory, conf.preProcess.site  + ".json")
# Create json file if there are X number of files in the finalAggregatedDataDirIfusion directory
if len(os.listdir(root_directory)) == 175: # 175 is the number of files in the directory for the Lund site
    create_dataset_json_onesite(root_directory, output_json_file)
    print('JSON file created!')

    # Test that all file paths in the JSON file exists as QA
    # Load the JSON file
    with open(output_json_file, 'r') as json_file:
        data = json.load(json_file)

    # Function to check if a file path exists
    def file_exists(file_path):
        return os.path.exists(file_path)

    # Iterate through the 'training' and 'validation' sections of the JSON data
    for dataset_type in ['training', 'validation']:
        for entry in data[dataset_type]:
            # Check if label file exists
            if not file_exists(entry['label']):
                print(f"Label file does not exist: {entry['label']}")
            
            # Check if image files exist
            for image_path in entry['image']:
                if not file_exists(image_path):
                    print(f"Image file does not exist: {image_path}")

    # Print a message if all files exist
    print("All file paths in JSON file have been checked.")

else: 
    print('JSON file not created as there are not the expected number of files in the directory!')
    print('Expected number of files: 175')
    print('Actual number of files: ' + str(len(os.listdir(root_directory))))


# Print message
print('Aggregating final data is complete!')