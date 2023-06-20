# *********************************************************************************
# Author: Christian Jamtheim Gustafsson, PhD, Medical Physcist Expert
# Skåne University Hospital, Lund, Sweden and Lund University, Lund, Sweden
# Description: Configuration file for the data preprocess pipeline. 
# *********************************************************************************

import os
import numpy as np

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
        base.dataFolderMICE = os.path.join(base.workFolder, 'ExtractStructuresData/Mice Batch/20230620/#validation')
    elif preProcess.study == 'Treatment':
        preProcess.inputDicomPatientDir = base.treatmentStudyFolder
        base.dataFolderMICE = os.path.join(base.workFolder, 'ExtractStructuresData/Mice Batch/20230620/#treatment')

    # Define output directory for Nifti data 
    preProcess.outputNiftiPatientDir = os.path.join(base.workFolder, 'ExtractStructuresData', preProcess.study)
    # Corresponding folder for fused final data (used in 2.fuseDataAndAnonomise.py)
    preProcess.outputNiftiPatientDirFinal = os.path.join(base.workFolder, 'ExtractStructuresData', preProcess.study, 'FinalAndAnon')
    # Corresponding folder for fused final and resampled data (used in 3.resampleAnonData.py)
    preProcess.outputNiftiPatientDirFinalResampled = os.path.join(base.workFolder, 'ExtractStructuresData', preProcess.study, 'FinalAndAnonAndResampled')

    
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
    preProcess.structureNameKeywords = ['BODY', 'Brain', 'Stem', 'Chiasm', 'GTV', 'CTV', 'Eye', 'Lens', 'Optic']
    preProcess.structureNameExclude = ['PRV', 'Z_', 'Y_', 'X_', 'dura', 'ben', 'äldre', 'ventricle']

    # Define a list of exactly named structures that are expected to exist after extraction
    # This does not include GTV or CTV, whis is handled separately where the list is used. 
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

    # Set voxel size for resampling
    preProcess.voxelSize = (1.0, 1.0, 2.0) # Most original data is 2 mm in slice thickness
