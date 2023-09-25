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
#import pydeface.utils as pdu
import matplotlib.pyplot as plt

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


    def detectNiiFiles(self, folder_path, max_levels=1):
        """
        Detect if folder or its subfolder contains .nii.gz files
        """
        for root, dirs, files in os.walk(folder_path):
            # Calculate the depth of the current directory relative to the starting folder
            depth = root.count(os.path.sep) - folder_path.count(os.path.sep)
            # Check if the depth is within the specified limit
            if depth <= max_levels:
                for file in files:
                    if file.endswith(".nii.gz"):
                        return True  # Return True if at least one .nii file is found
        return False  # Return False if no .nii files are found


    def stackNiftiData(self, i_subject, subject, dataInBasePath, dataOutBasePath):
        """
        Stack Nifti data to multi channel Nifti file. ALso handles GT data. 

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
        # Define output folders
        imagesOutFolderPath = os.path.join(dataOutBasePath, "train", "images")
        GTOutFolderPath = os.path.join(dataOutBasePath, "train", "labels")
        # Make sure output folder exists
        os.makedirs(imagesOutFolderPath, exist_ok=True)
        os.makedirs(GTOutFolderPath, exist_ok=True)

        ### IMAGE VOLUME ###
        # Create the Nifti image stack from subjectFiles
        imageVolumes = []
        # for imageFile in conf.preProcess.ImageFileNameStack:
        for index, imageFile in enumerate(conf.preProcess.ImageFileNameStack):

            # Option for creating nnUnet data 
            if conf.preProcess.createNNUnetData == True:
                # Define folder for nnUnet data
                nnUnetDataOutFolderPathData = os.path.join(dataOutBasePath, "nnUnetData", "imagesTr")
                # Make sure output folder exists
                os.makedirs(nnUnetDataOutFolderPathData, exist_ok=True)
                # Copy the image file to nnUnetDataOutFolderPath with a new name
                # Name is determined by the foor loop index
                shutil.copyfile(os.path.join(subjectFolderPath, imageFile), os.path.join(nnUnetDataOutFolderPathData, subject + "_000" + str(index) + ".nii.gz"))
                # Assert that index < 9
                assert index < 9, 'Index must be less than 9'

            # Read Nifti file
            imageFilePath = os.path.join(subjectFolderPath, imageFile)
            imageData = nibabel.load(imageFilePath)
            # Assert imageData not empty
            assert imageData is not None, 'Input imageData must not be empty'
            # Append to list
            imageVolumes.append(imageData.get_fdata())
        # Stack volumes
        stackedVolume = np.stack(imageVolumes, axis=-1)
        # Create new Nifti volume. Use affine from last image in the stack, should be same for all 
        # they are registered to CT. 
        stackedImage = nibabel.Nifti1Image(stackedVolume, imageData.affine) 
        # Save image to 4D Nifti file 
        outputFilename = os.path.join(imagesOutFolderPath, f"{subject}_4channel.nii.gz")
        nibabel.save(stackedImage, outputFilename)

        ### GT VOLUME ###
        # Create the GT Nifti file in subjectFiles and save it
        # Create an empty variable with same size as stackedVolume
        GTVolume_shape = (stackedVolume.shape[0], stackedVolume.shape[1], stackedVolume.shape[2]) 
        GTVolume = np.zeros(GTVolume_shape, dtype=np.uint8)  # Change dtype as needed
        # Loop through the dictionary of GT structures
        # Order is important to keep the hierarci of the structures correct
        for GTFile in conf.preProcess.GTStructureFileName.keys():
            # Read GT Nifti file
            GTFilePath = os.path.join(subjectFolderPath, GTFile)
            # Make sure the file exists
            if os.path.isfile(GTFilePath) == False: 
                print('File ' + GTFilePath + ' does not exist')
                print('Skipping this file and removing image data for ' + subject + ' from the dataset')
                # Remove corresponding image data
                os.remove(os.path.join(imagesOutFolderPath, f"{subject}_4channel.nii.gz"))
                #return # Do not write GT file at all, abort processing for this patient. 
                # Do the same for nnUnet data
                if conf.preProcess.createNNUnetData == True:
                    # Remove corresponding image data
                    try: 
                        os.remove(os.path.join(nnUnetDataOutFolderPathData, subject + "_0000" + ".nii.gz"))
                        os.remove(os.path.join(nnUnetDataOutFolderPathData, subject + "_0001" + ".nii.gz"))
                        os.remove(os.path.join(nnUnetDataOutFolderPathData, subject + "_0002" + ".nii.gz"))
                        os.remove(os.path.join(nnUnetDataOutFolderPathData, subject + "_0003" + ".nii.gz"))
                    except:
                        print('Could not remove nnUnet data for ' + subject + ' from the dataset')
                # Return 
                return # Do not write GT file at all, abort processing for this patient. 

            GTData = nibabel.load(GTFilePath)
            # Assert GTData is not empty
            assert GTData is not None, 'Input GTData must not be empty'
            # Assert same size as stackedVolume for the first three dimensions
            assert GTData.shape[0] == stackedVolume.shape[0], 'Input GTData must have same size as stackedVolume for the first dimension'
            assert GTData.shape[1] == stackedVolume.shape[1], 'Input GTData must have same size as stackedVolume for the second dimension'
            assert GTData.shape[2] == stackedVolume.shape[2], 'Input GTData must have same size as stackedVolume for the third dimension'
            # Get the value for the structure from the dictionary
            assignedValue = conf.preProcess.GTStructureFileName[GTFile]
            # Multiply the GT data with the assigned value
            GTDataAssigned = GTData.get_fdata() * assignedValue
            # Create a mask for non-zero values in GTDataAssigned
            nonZeroMask = GTDataAssigned != 0
            # Update GTVolumes with non-zero values from nonZeroMask
            GTVolume[nonZeroMask] = GTDataAssigned[nonZeroMask]
        # Create new Nifti volume. Use affine from last image in the stack, should be same for all
        # they are registered to CT.
        GTVolumeCombined = nibabel.Nifti1Image(GTVolume, GTData.affine)
        # Save image to 3D Nifti file
        outputFilename = os.path.join(GTOutFolderPath, f"{subject}_seg.nii.gz")
        nibabel.save(GTVolumeCombined, outputFilename)  

        # Option for creating nnUnet data 
        if conf.preProcess.createNNUnetData == True:
             # Define folder for nnUnet data
            nnUnetDataOutFolderPathLabels = os.path.join(dataOutBasePath, "nnUnetData", "labelsTr")
            # Make sure output folder exists
            os.makedirs(nnUnetDataOutFolderPathLabels, exist_ok=True)
            # Copy the image file to nnUnetDataOutFolderPath with a new name
            shutil.copyfile(outputFilename, os.path.join(nnUnetDataOutFolderPathLabels, subject + ".nii.gz"))

        print(' ')


    def padAroundImageCenter(self, imageArray, paddedSize, subject):
        """
        Pad matrix with zeros to desired shape.
        
        Args:
            imageArray (array): Image array to be padded
            paddedSize (int): Size of matrix after zero padding

        Return:
            paddedImageArray (array): Padded image array
        """
        # Assert tuple and np array
        assert isinstance(paddedSize, tuple), "Padded size is not a tuple"
        assert isinstance(imageArray, np.ndarray), "Image array is not a numpy array"
        # Assert image size is not larger than padded size
        assert imageArray.shape[0] <= paddedSize[0], "Image size is larger than requested padded size in row: " + str(imageArray.shape[0]) + " vs " + str(paddedSize[0]) + " in subject " + str(subject)
        assert imageArray.shape[1] <= paddedSize[1], "Image size is larger than requested padded size in column: " + str(imageArray.shape[1]) + " vs " + str(paddedSize[1]) + " in subject " + str(subject)
        assert imageArray.shape[2] <= paddedSize[2], "Image size is larger than requested padded size in slice: " + str(imageArray.shape[2]) + " vs " + str(paddedSize[2]) + " in subject " + str(subject)
        # Get shape of the image array
        origShape = imageArray.shape
        # Caluclate half the difference between the desired 
        # size and the original shape and round up
        diff = np.round((np.array(paddedSize) - np.array(origShape))//2)
        # Calculate padding. Takes care of case when matrix are uneven size. 
        extraLeft = diff[0]
        extraRight = paddedSize[0] - origShape[0] - diff[0]
        extraTop = diff[1]
        extraBottom = paddedSize[1] - origShape[1] - diff[1]
        extraFront = diff[2]
        extraBack = paddedSize[2] - origShape[2] - diff[2]
        # Pad the image array with zeros
        paddedImageArray = np.pad(imageArray, ((extraLeft,extraRight), (extraTop,extraBottom), (extraFront, extraBack)), 'constant', constant_values=0)
        # Assert correct padded size, very important
        assert paddedImageArray.shape[0] == paddedSize[0], "Padded image size is incorrect in row"
        assert paddedImageArray.shape[1] == paddedSize[1], "Padded image size is incorrect in column"
        assert paddedImageArray.shape[2] == paddedSize[2], "Padded image size is incorrect in slice"
        # Return the padded image array
        return paddedImageArray
    

    def cropImageFromMask(self, image, mask, marginal, subject):
        """
        Crop image from mask and add marginal space in voxels

         Args:
            image (array): 3D image
            mask (array): 3D mask 
            marginal (tuple): Number of voxels to add around the mask

        Return:
            croppedImage (array): Cropped image
        
        """
        assert len(image.shape) == 3, "dim should be 3"
        assert len(mask.shape) == 3, "dim should be 3"
        # Coordinates of non-zero elements in the mask
        coords = np.argwhere(mask)
        # Bounding box coordinates of the box mask
        x0, y0, z0 = coords.min(axis=0)
        x1, y1, z1 = coords.max(axis=0) + 1   # slices are exclusive at the top
        # Add marginal to the bounding box
        x0 = x0 - marginal[0]
        x1 = x1 + marginal[1]
        y0 = y0 - marginal[2]
        y1 = y1 + marginal[3]
        z0 = z0 - marginal[4]
        z1 = z1 + marginal[5]       
        # If the bounding box with margin is outside the image, set it to the image size
        if x0 < 0:
            x0 = 0
        if x1 > image.shape[0]:
            x1 = image.shape[0]
        if y0 < 0:
            y0 = 0
        if y1 > image.shape[1]:
            y1 = image.shape[1]
        if z0 < 0:
            z0 = 0
        if z1 > image.shape[2]:
            z1 = image.shape[2]
        # Get the extracted contents of the box
        croppedImage = image[x0:x1, y0:y1, z0:z1]
        # Return the cropped image
        return croppedImage


    def faceMaskAnon(self, imgData, boundingBoxData, subjectFolderPath, faceMaskAnonDist, faceMaskAnonSize, subject): 
        """
        Apply face mask to image data and set values in mask to zero. 
        This is performed with the help of a orientational structure 
        that is used to define the face mask. From there a distance from this 
        structure is defined and a face mask is created 
        around the end point of that distance.

        Args:
            imgData (array): Image data to be defaced
            boundingBoxData (array): Bounding box data that previosly was applied to the image data. 
                Same operation must be done on the orientational structure to keep geometry.
            subjectFolderPath (str): Path to subject folder
            faceMaskAnonDist (tuple): Distance from center of support structure to center of face mask in voxels
            faceMaskAnonSize (tuple): Size of face mask in pixels
            subject (str): Subject name
            
        Returns:
            Outputs masked image data where masked parts of the face is set to zero
        """
        # Assert input
        assert isinstance(imgData, np.ndarray), 'Input imgData must be a numpy array'
        assert isinstance(boundingBoxData, np.ndarray), 'Input boundingBoxData must be a numpy array'
        assert isinstance(subjectFolderPath, str), 'Input subjectFolderPath must be a string'
        assert isinstance(faceMaskAnonDist, tuple), 'Input faceMaskAnonDist must be a tuple'
        assert isinstance(faceMaskAnonSize, tuple), 'Input faceMaskAnonSize must be a tuple'
        assert isinstance(subject, str), 'Input subject must be a string'
        # Load in the structure used for orientation.
        # In this case use the brain structure as starting point
        orientFilePath = os.path.join(subjectFolderPath, conf.preProcess.faceMaskOrientStructureFileName)
        orientData = nibabel.load(orientFilePath)
        # Resample to chosen spatial resolution, using nearest neighbour interpolation as this is a mask. 
        reSampledOrientData = nibabel.processing.resample_to_output(orientData, voxel_sizes=conf.preProcess.voxelSize, order=0, mode='constant', cval=0.0)
        reSampledOrientData = reSampledOrientData.get_fdata() # This is the brain segmentation map
        # Apply the bounding box to the reSampledOrientData
        reSampledCropOrientData = self.cropImageFromMask(reSampledOrientData, boundingBoxData, conf.preProcess.marginCropVoxel, subject)
        # This must now be the same size as imgData, assert
        assert reSampledCropOrientData.shape == imgData.shape, 'Input reSampledOrientData must have same size as imgData for all dimensions'
        # Get the center of mass of the mask
        centerOfMass = scipy.ndimage.measurements.center_of_mass(reSampledCropOrientData)
        # Round to nearest integer
        centerOfMass = np.round(centerOfMass).astype(int)
        # Take this coordinate and move the coordinate in the image 
        # This is the new center of the face mask. Be aware of the coordinate system, x and y are swapped, and z is flipped. Control in the input. 
        faceMaskCenter = (centerOfMass[0] + faceMaskAnonDist[0], centerOfMass[1] + faceMaskAnonDist[1], centerOfMass[2] + faceMaskAnonDist[2])
        # Create an empty array with ones with the same size as the image data
        faceMask = np.ones(imgData.shape)
        # Calculate the coordinates of the corners of the 3D rectangle in the image space
        x1 = int(faceMaskCenter[0] - faceMaskAnonSize[0] / 2)
        x2 = int(faceMaskCenter[0] + faceMaskAnonSize[0] / 2)
        y1 = int(faceMaskCenter[1] - faceMaskAnonSize[1] / 2)
        y2 = int(faceMaskCenter[1] + faceMaskAnonSize[1] / 2)
        z1 = int(faceMaskCenter[2] - faceMaskAnonSize[2] / 2)
        z2 = int(faceMaskCenter[2] + faceMaskAnonSize[2] / 2)
        # Ensure the coordinates are within the bounds of the faceMask array
        x1 = max(0, x1)
        x2 = min(faceMask.shape[0], x2)
        y1 = max(0, y1)
        y2 = min(faceMask.shape[1], y2)
        z1 = max(0, z1)
        z2 = min(faceMask.shape[2], z2)
        # Create the rectangle by setting the corresponding region in faceMask to 0
        faceMask[x1:x2, y1:y2, z1:z2] = 0   
        # Convert to mask 
        faceMask = faceMask.astype(np.uint8)
        # Apply mask to data and set values to zero
        imgData[faceMask == 0] = 0


        # Return data
        return imgData


    def processNiftiData(self, i_subject, subject, dataInBasePath, dataOutBasePath):
        """
        Process Nifti data to chosen spatial resolution, cut, pad and deface the data 

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

        # Assert that the bounding box structure file exists. Used to define the bouding box. 
        assert conf.preProcess.BBFileName in subjectFiles
        BBFilePath = os.path.join(subjectFolderPath, conf.preProcess.BBFileName)
        BBData = nibabel.load(BBFilePath)
        # Resample to chosen spatial resolution, using nearest neighbour interpolation as this is a mask.
        reSampledBBData = nibabel.processing.resample_to_output(BBData, voxel_sizes=conf.preProcess.voxelSize, order=0, mode='constant', cval=0.0)
        reSampledBBDataNp = reSampledBBData.get_fdata() # This is the brain segmentation map

        # Resample, cut and pad each Nifti file in subjectFiles to chosen spatial resolution and save to subjectOutFolderPath
        for subjectFile in subjectFiles:
            # Read Nifti file
            subjectFilePath = os.path.join(subjectFolderPath, subjectFile)
            subjectData = nibabel.load(subjectFilePath)
            # Resample to chosen spatial resolution
            # Order 0 is nearest neighbour interpolation, used for masks, order 3 is cubic spline interpolation, used for image data. 
            if 'mask' in subjectFile:
                interpolationOrder = 0
            else:
                interpolationOrder = 3
            # Perform resamling
            reSampledSubjectData = nibabel.processing.resample_to_output(subjectData, voxel_sizes=conf.preProcess.voxelSize, order=interpolationOrder, mode='constant', cval=0.0)
            reSampledSubjectData = reSampledSubjectData.get_fdata()
            # Assert same size as bounding box structure for all dimensions
            assert reSampledSubjectData.shape == reSampledBBDataNp.shape, 'Input reSampledSubjectData must have same size as reSampledBBDataNp for all dimensions'
            # Crop volume with respect to the bounding box structure file including marginal space in voxels 
            reSampledCutSubjectData = self.cropImageFromMask(reSampledSubjectData, reSampledBBDataNp, conf.preProcess.marginCropVoxel, subject)
            # Deface the data if option is set and condition is met
            if conf.preProcess.defaceData == True:
                reSampledCutSubjectData = self.faceMaskAnon(reSampledCutSubjectData, reSampledBBDataNp, subjectFolderPath, conf.preProcess.faceMaskAnonDistance, conf.preProcess.faceMaskAnonSize, subject)
            # Zero pad data to desired size
            reSampledCutPadSubjectData = self.padAroundImageCenter(reSampledCutSubjectData, conf.preProcess.paddedSize, subject)
            # Assign final data to be saved
            finalSubjectData = reSampledCutPadSubjectData
            # Create new Nifti volume. Use affine from last image in the stack, should be same for all
            finalImage = nibabel.Nifti1Image(finalSubjectData, reSampledBBData.affine)
            # Save data to subjectOutFolderPath
            subjectOutFilePath = os.path.join(subjectOutFolderPath, subjectFile)
            nibabel.save(finalImage, subjectOutFilePath)
   

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
        


    