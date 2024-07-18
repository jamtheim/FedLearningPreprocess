
Mice workflow
1. Import Data into mice
2. For each patient you will need:
	- CT image volume in Dicom
	- RT Structure Dicom file
	- RT Registration Dicom file
	- RT Dose Dicom file
2. Check that the structure names correspond with your site's naming conventions, if not change the values in the green column in mice
3. Batch Data in Mice
4. Rename Output folders to remove patient information
5. Note the filepath to the batch-output folder for mice


In Python script nifty_to_npz.py
1. under main() change "path_to_patient_dir" to the batch output folder
2. Then change "path_to_output_dir" to your desired destination folder
3. Please visually verify your files by setting visualize to True (in main()) and compare to the output Nifty
	- pay attention to the geometric correspondence between dose and structures.
	- Make sure the structures are in this order:
		'CTV',
        	'PTV',
        	'brainstem',
        	'optic_chiasm',
        	'globe_L',
        	'globe_R',
        	'optic_nerve_L',
        	'optic_nerve_R',
        	'body'
4. Run the python script.
5. You should now see 3 files in the folder for each patient, "all_structs.npz", "brain.npz" and "dose.npz"
	- all_structs.npz has (Structure, slice, row, column) and is in int8 
	- dose.npz has (slice, row, column) and represents the dose matrix divided by 60, is in float32
    - brain.npz is mostly for potential future use. same structure as the "all_structs" file.
	- Everything is downsampled to 3x3x3 mm voxel size


Note: If the script should fail at some point, identify the problem then delete the whole destination folder and restart it.