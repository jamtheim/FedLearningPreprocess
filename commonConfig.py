# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Configuration file for the data preprocess pipeline. 
# *********************************************************************************

import os
import numpy as np
import subprocess

class commonConfigClass():
    """
    Class describing the common configuration used in the project.
    """

    def __init__ (self):
        """
        Init function
        """
        pass
    
    class base:
        """
        Empty class to define base related configuration.
        """
        pass

    class preProcess:
        """
        Empty class to define preProcessing related configuration.
        """
        pass

    class inference:
        """
        Empty class to define inference related configuration.
        """
        pass

    class postProcess:
        """
        Empty class to define postProcess related configuration.
        """
        pass

   
    # Init base configuration classes 
    base = base()
    preProcess = preProcess()
    inference = inference()
    postProcess = postProcess()

    # Set base configuration
    # Get folder where this file is located
    base.baseFolder = os.path.dirname(os.path.abspath(__file__))
    # Working folder 
    base.workFolder = os.path.join('/mnt/WindowsDisk/CJG/MRIOnlyBrain')
    # Specific folders for two study cohorts acquired from Skåne University Hospital, Lund, Sweden
    # Called validation and treatment study
    base.validationStydyFolder = os.path.join(base.workFolder, 'Validation study based on CT')
    base.treatmentStudyFolder = os.path.join(base.workFolder, 'Treatment study based on MRI' )

    # Set pre-processing on selected cohort (comment the other one out)
    preProcess.study = 'Validation' # 'Validation' or 'Treatment'
    #preProcess.study = 'Treatment' # 'Validation' or 'Treatment'
    
    if preProcess.study == 'Validation':
        preProcess.inputDicomPatientDir = base.validationStydyFolder
        base.dataFolderMICE = os.path.join(base.workFolder, 'ExtractStructuresData/Mice Batch/20230918/#Validation')
    elif preProcess.study == 'Treatment':
        preProcess.inputDicomPatientDir = base.treatmentStudyFolder
        base.dataFolderMICE = os.path.join(base.workFolder, 'ExtractStructuresData/Mice Batch/20230918/#Treatment')

    # Define output directory for Nifti data 
    preProcess.outputNiftiPatientDir = os.path.join(base.workFolder, 'ExtractStructuresData', preProcess.study)
    # Corresponding folder for fused final data (used in 2.fuseDataAndAnonomise.py)
    preProcess.outputNiftiPatientDirFinal = os.path.join(base.workFolder, 'ExtractStructuresData', preProcess.study, 'FinalAnon')
    # Corresponding folder for fused final and resampled data (used in 3.resampleAnonData.py)
    preProcess.outputNiftiPatientDirFinalResampled = os.path.join(base.workFolder, 'ExtractStructuresData', preProcess.study, 'FinalAnonResampled')
    # Corresponding folder for fused final, resampled and stacked data (used in 4.stackData.py)
    preProcess.outputNiftiPatientDirFinalResampledStacked = os.path.join(base.workFolder, 'ExtractStructuresData', preProcess.study, 'FinalAnonResampledStacked')
    
    
    # Set folder where DICOM struct file is located
    preProcess.RTstructFolderFirst = 'Structs'
    if preProcess.study == 'Validation':
        preProcess.RTstructFolderSecond = 'CT_StructureSet'
    elif preProcess.study == 'Treatment':
        preProcess.RTstructFolderSecond = 'sCT_StructureSet'

    # Set pssible BODY struct name
    preProcess.bodyStructureName1 = 'BODY'
    preProcess.bodyStructureName2 = 'External'

    # Set keywords for selecting structures to be extracted
    # preProcess.structureNameKeywords = ['BODY', 'Brain', 'Stem', 'Chiasm', 'GTV', 'CTV', 'Eye', 'Lens', 'Optic']
    preProcess.structureNameKeywords = ['BODY', 'Stem', 'GTV', 'CTV']
    preProcess.structureNameExclude = ['PRV', 'Z_', 'Y_', 'X_', 'dura', 'ben', 'äldre', 'ventricle']

    # Define bounding box file name, marginal will be added 
    preProcess.BBFileName = 'mask_Brain.nii.gz'
  
    # Define a list of exactly named structures that are expected to exist after extraction
    # This does not include GTV or CTV, whis is handled separately where the list is used. 
    """
    preProcess.structureFileNameExact = [
    'image.nii.gz',
    'mask_BODY.nii.gz',
    'mask_Brain.nii.gz',
    'mask_BrainStem.nii.gz',
    'mask_Chiasm.nii.gz',
    'mask_Eye_L.nii.gz',
    'mask_Eye_R.nii.gz',
    'mask_Lens_L.nii.gz',
    'mask_Lens_R.nii.gz',
    'mask_OpticNerve_L.nii.gz',
    'mask_OpticNerve_R.nii.gz'
    ]
    """

    preProcess.structureFileNameExact = [
    'mask_BODY.nii.gz',
    'mask_BrainStem.nii.gz',
    'mask_Brain.nii.gz',
    ]

    # Define a list of structures that are going to be stacked together to form a single 4D Nifti file. Order is important!
    preProcess.ImageFileNameStack = [
    'image T2 tra flair fs.nii.gz',
    'image T1 tra.nii.gz',
    'image T1 tra GD.nii.gz',
    'image T2 tra GD.nii.gz',
    ]

    # Create a dictory with the structure names and assign values for the GT Nifti file. Order is important and should be based on hierarki! 
    # As we only have one label map it is not possible to have overlapping structures. Sort below dictioary with this in mind. 
    preProcess.GTStructureFileName = {
    'mask_BrainStem.nii.gz': 4,
    'mask_CTVT.nii.gz': 2,
    'mask_GTVT.nii.gz': 1, # Always smaller than CTV
    }

    # Set voxel size for resampling
    preProcess.voxelSize = (1.0, 1.0, 2.0) # Most original data is 2 mm in slice thickness
    # Set margin for cropping, rowMin, rowMax, colMin, colMax, zMin, zMax. Units in resampled voxel size. 
    # Image is rotated 90 degrees. Hence, row and col are swapped. 
    preProcess.marginCropVoxel = (35, 35, 35, 35, 20, 10) 
    # Set matrix size after resampling and cropping using padding
    preProcess.paddedSize = (256, 256, 140) # Most original data is 256x256 in plane size   
    # Set option for defacing data
    preProcess.defaceData = True
    preProcess.faceMaskAnonDistance = (0, 120, -40) # Number of voxels to move from center to define center of face mask 
    preProcess.faceMaskAnonSize = (256, 70, 50) # Size of face mask in pixels after resampling and cropping
    # row, col, slice in rotated image space for the above two (90 degrees). 
    # Fist parameter of faceMaskAnonSize will set width in tra image, second depth in the tra image, third number of slices. 
    preProcess.faceMaskOrientStructureFileName = 'mask_Brain.nii.gz' # Used for orientation of the face mask

   

