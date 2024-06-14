# *************************************************************
# Author: Pontus Wahlqvist, Biomedical Engineer
# Skåne Universtiy hospital, Lund, Sweden
# *************************************************************

import os
import matplotlib.axes
import matplotlib.figure
import matplotlib.typing
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

matplotlib.use('TkAgg')





structure_files = [
                   'CTV',
                   'PTV',
                   'brainstem',
                   'optic_chiasm',
                   'globe_L',
                   'globe_R',
                   'optic_nerve_L',
                   'optic_nerve_R',
                   'body',
                   ]



def read_and_save_matrix(full_path:str, output_path: str, structure:str, dtype:np.dtype):
    """
    Reads in the nifty image and does some preprocessing (flipping and transposing) then saves it as a npz file in the target path
    
    Args:
        full_path (string): the file path to the npz file
        output_path (string):
        structure (string): the name of the structure
        
    """

    # Add data type handling here as well. add assert for dose specifically (float32) and the structures (int8) 
    # Also assert that max dose value is not greater than 1.1 or 1.2 or something as well as more than 0

    image = nib.load(full_path)
    image_array = image.get_fdata()

    # The data we want is (Z, Y, X) (slices, rows, columns) But due to the way nibabel reads the nifty file we must transpose it 90 degrees
    # Each slice is then flipped to make sure Anterior and posterior are in the correct direction
    image_array = np.transpose(image_array, (2,1,0))
    flipped_array = np.zeros(image_array.shape)
    for n in range(image_array.shape[0]):
        flipped_array[n,:,:] = np.flipud(image_array[n,:,:])
    if structure == 'dose':
        pass
    else:
        assert np.max(flipped_array) == 1, f"Error with structure segmentation for {structure}, max value is not 1."
        assert np.min(flipped_array) == 0, f"Error with structure segmentation for {structure}, min value is not 0."
        assert np.all(np.logical_or(flipped_array==0, flipped_array==1)), f"Error with array for structure: {structure}, contains values not == 1 or 0"


    # Sets the structure arrays to dtype int8 and the dose dtype float32
    flipped_array = flipped_array.astype(dtype=dtype)

    # Checks if the target folder exists: if it doesnt it creates it
    if not os.path.isdir(output_path):
        os.makedirs(os.path.join(output_path))

    npz_file_path = os.path.join(output_path, structure + '.npz')
    

    np.savez(npz_file_path,image_array=flipped_array)

def read_npz(full_path:str, dtype:np.dtype):
    """
    Loads the structure npz file and returns it as a numpy array with the selected datatype
    
    Args:
        full_path (string): the full path to the .npz file
        dtype (np.dtype): the selected datatype for the finished array. Defaults to int8
    """
    read_array = np.load(full_path)
    read_array = read_array['image_array']
    
    # double checks the datatype
    assert read_array.dtype == dtype #Array does not contain the correct dtype

    return read_array


def run_QA(all_structs_array:np.ndarray , dose_array:np.ndarray):
    
    #  should make sure that PTV > CTV using sum
    CTV_sum = np.sum(all_structs_array[0])
    PTV_sum = np.sum(all_structs_array[1])

    assert CTV_sum < PTV_sum, "CTV is larger than PTV"

    #  Should double check datatypes and expected max and mins
    assert all_structs_array.dtype == np.int8
    assert dose_array.dtype == np.float32

    #  Should make sure dose is not empty
    assert np.any(dose_array != 0), "Dose array is empty (only zeros)"
    
    #  should check that dose is around 60gy max must be at least 0.95 (maybe)
    #  This might be different from site to site but it makes sure the maxdose is between 57 and 66
    assert 0.95 < np.max(dose_array) < 1.1, f"Patient dose might not be 60 Gy. Max Value in Dose array was {np.max(dose_array)*60}"
    print(f"Max dose values: {np.max(dose_array)}")

    for index, structure in enumerate(structure_files):
        #  Should make sure structure arrays are not empty
        assert np.any(all_structs_array[index,:,:,:] != 0), f"The array for {structure} is empty (only zeros)"
        #  Should check that max and min data is 1 and 0 for all structures
        assert np.max(all_structs_array[index,:,:,:]) == 1, f"The array for {structure} has values above 1"
        assert np.min(all_structs_array[index,:,:,:]) == 0, f"The array for {structure} has values below 0"
        assert np.all(np.logical_or(all_structs_array==0, all_structs_array==1)), f"Error with array for structure: {structure}, contains values not == 1 or 0"


# ---Visualization functions---
# update_image is called for each slice to update the subplot to show the new slice and change the title of the figure
# Should maybe be moved to a different file.
def update_image(zslice: int, image_stack:np.ndarray, axes_list:list, structures:list, ax:matplotlib.axes.Axes, figure:matplotlib.figure.Figure, dose_array:np.ndarray): 
    """
    Updates the current slice being shown in the plots

    Args:
        zslice (int): the slice to go to
        image_stack (np array): the combined array of structures in the correct order
        axes_list (list): the different axes
        structures (list): a list of structures
        ax (figure axes): The axes object of the figure
        figure (matplotlib figure): The animation figure, used for updating the slice number
    """
    for index,axis in enumerate(axes_list):
        if index == 8:
            image_sum = np.sum(image_stack, axis=0)[zslice,:,:]
            axis.set_array(image_sum)
            axis.autoscale()
        elif index == 9:
            axis.set_array(dose_array[zslice,:,:])
        else:
            axis.set_array(image_stack[index,zslice,:,:])
    figure.suptitle(f"Slice Number: {zslice}")
    for i2 in range(5):
        for i1 in range(2):
            ax[i1,i2].set_title(f"{structures[i1*5+i2]}")


# The setup for the subplots
def initial_visual_update(ax:matplotlib.axes.Axes , image_stack:np.ndarray, dose_array:np.ndarray):
    """
    Sets up the subplots:

    Args:
        ax: The matplotlib axes for the plot
        image_stack: the npz array that contains all the structures
    """
    
    image_CTV = ax[0,0].imshow(image_stack[0,0,:,:], vmin= 0, vmax=1)
    image_PTV = ax[0,1].imshow(image_stack[1,0,:,:], vmin= 0, vmax=1)
    image_brainstem = ax[0,2].imshow(image_stack[2,0,:,:], vmin= 0, vmax=1)
    image_optic_chiasm = ax[0,3].imshow(image_stack[3,0,:,:], vmin= 0, vmax=1)
    image_globe_l = ax[0,4].imshow(image_stack[4,0,:,:], vmin= 0, vmax=1)
    image_globe_r = ax[1,0].imshow(image_stack[5,0,:,:], vmin= 0, vmax=1)
    image_optic_nerve_l = ax[1,1].imshow(image_stack[6,0,:,:], vmin= 0, vmax=1)
    image_optic_nerve_r = ax[1,2].imshow(image_stack[7,0,:,:], vmin= 0, vmax=1)
    image_body = ax[1,3].imshow(image_stack[8,0,:,:], vmin= 0, vmax=5)
    image_dose = ax[1,4].imshow(dose_array[0,:,:], vmin=0, vmax=1.1)

    axes_list = [image_CTV,image_PTV,image_brainstem,image_optic_chiasm,image_globe_l,image_globe_r, image_optic_nerve_l, image_optic_nerve_r, image_body, image_dose]

    return axes_list


def visualize_stack(file_location, dose_array):
    """
    Creates a grid of subplots with an animation of the different slices of the structure
    """
    image_stack = np.load(os.path.join(file_location,'all_structs.npz'))['image_array']
    array_size = np.shape(image_stack)
    structures = [
        'CTV',
        'PTV',
        'brainstem',
        'optic_chiasm',
        'globe_L',
        'globe_R',
        'optic_nerve_L',
        'optic_nerve_R',
        'body'
    ]
    
    structures.append('dose')

    fig, ax = plt.subplots(2,5, figsize = (15,6))
    axes_list = initial_visual_update(ax = ax,image_stack=image_stack, dose_array = dose_array)

    # this section creates the animation to be shown
    fig.subplots_adjust(left=0, right=1, top=0.9, bottom=0.05, hspace=0.25, wspace=0.1)
    ani = FuncAnimation(fig=fig,func=update_image, fargs=[image_stack, axes_list, structures, ax, fig, dose_array], frames=range(array_size[1]), interval = 100, repeat=True)

    plt.show()


def handle_patient(path_to_patient:str, path_to_output:str, visualize = False):
    """
    runs the script to convert nifty files to npz files and stack them.

    Args:
        path_to_patient (str): the full path to the location of the patient.
        visualize (bool): Set to true if you want to see the animation of how the slices look. Defaults to False.     
    """

    # This section reads all the nifty files and converts them into npz files
    output_path = path_to_output

    try:
        os.makedirs(output_path, exist_ok=False)
    except:
        print("folders_exist")
        return


    for structure in structure_files:

        full_path =  os.path.join(path_to_patient,structure + '.nii.gz')
        read_and_save_matrix(full_path=full_path, output_path=output_path, structure=structure, dtype=np.int8 )


    # Dose is seperate as it is not a part of the structure files list
    full_path =  os.path.join(path_to_patient,'dose.nii.gz')
    read_and_save_matrix(full_path=full_path,  output_path=output_path, structure='dose', dtype=np.float32)

    all_structs = []

    # This section reads in all the individual structure npz files, then stacks them on top of each other in the correct order 
    for structure in structure_files:  # order of structures is important and is given by the order of the structure files list
        structure_data = read_npz(os.path.join(output_path, structure + '.npz'), dtype=np.int8)
        all_structs.append(structure_data)
    
    
        

    array_all_structs = np.stack(all_structs)
    np.savez(os.path.join(output_path,'all_structs.npz'), image_array = array_all_structs)

    if os.path.exists(os.path.join(output_path,'all_structs.npz')):
        for structure in structure_files:
            os.remove(os.path.join(output_path, structure + '.npz'))
    
    
    
    dose_array =  np.load(os.path.join(output_path, 'dose.npz'))["image_array"] 
    run_QA(all_structs_array=array_all_structs, dose_array=dose_array)

    

    # Visualize stack generates a 3x3 subplot containing an animation of all the slices of the different structures
    if visualize:
        visualize_stack(file_location= output_path, dose_array=dose_array)

        # -- include dose in visualize at some point 
        #  placed between ptv ctv to make it easier to see

def main(): 
    # The current code will work for code that just came out of the mice script, maybe we want to change it a bit
    # How should the output of the script look? folders or files?

    # visualize the structures or not, For QA purposes mostly
    visualize = False
    
    # Path to patient dir should lead to the output folder of the mice batch, the folder where the patients are stored.
    path_to_patient_dir = os.path.join(r"C:\\","Mice Export", "Mice Batch", "20240613", "treat")

    # This can be whatever path you want, the script will create folders for each patient 
    path_to_output_dir = os.path.join(r"C:\\","Mice Export", "Mice Batch", "20240613")

    for patient in os.listdir(path_to_patient_dir):
        output_path = os.path.join(path_to_output_dir, "results", patient)
        patient_path = os.path.join(path_to_patient_dir, patient)

        if os.path.isdir(patient_path):
           
            # This section double checks that there are not 2 registrations for the patient, and asks you to delete them if there are.
            if len(os.listdir(patient_path)) == 1:
                print([patient_path, os.listdir(patient_path)[0]])
                patient_path=os.path.join(patient_path,os.listdir(patient_path)[0])

                # This is where the actual script runs. Set "visualize" to False if you don't want to view every patient. 
                # the visualize script is mostly for confirming that the resulting npz files look like the nifty files.
                handle_patient(path_to_patient=patient_path, path_to_output=output_path, visualize=visualize)
            elif len(os.listdir(patient_path)) > 1:
                print("more than one treatment plan exists") 
                print(os.listdir(patient_path))
                print("please choose one of them and remove the other")
            else:
                print(f"Patient {patient} has no treatment plan")
        else:
            print("wrong path")
        

if __name__ == "__main__":
    main()