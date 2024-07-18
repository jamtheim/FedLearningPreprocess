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

matplotlib.use("TkAgg")


structure_files = [
    "CTV",
    "PTV",
    "brainstem",
    "optic_chiasm",
    "globe_L",
    "globe_R",
    "optic_nerve_L",
    "optic_nerve_R",
    "body",
]


def read_and_save_matrix(full_path: str, output_path: str, structure: str, dtype: np.dtype):
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
    # Print size
    # print(image_array.shape)

    # The data we want is (Z, Y, X) (slices, rows, columns) But due to the way nibabel reads the nifty file we must transpose it 90 degrees
    # Each slice is then flipped to make sure Anterior and posterior are in the correct direction
    image_array = np.transpose(image_array, (2, 1, 0))
    flipped_array = np.zeros(image_array.shape)
    for n in range(image_array.shape[0]):
        flipped_array[n, :, :] = np.flipud(image_array[n, :, :])
    if structure == "dose":
        pass
    else:
        assert (
            np.max(flipped_array) == 1
        ), f"Error with structure segmentation for {structure}, max value is not 1."
        assert (
            np.min(flipped_array) == 0
        ), f"Error with structure segmentation for {structure}, min value is not 0."
        assert np.all(
            np.logical_or(flipped_array == 0, flipped_array == 1)
        ), f"Error with array for structure: {structure}, contains values not == 1 or 0"

    # Sets the structure arrays to dtype int8 and the dose dtype float32
    flipped_array = flipped_array.astype(dtype=dtype)

    # Checks if the target folder exists: if it doesnt it creates it
    if not os.path.isdir(output_path):
        os.makedirs(os.path.join(output_path))

    npz_file_path = os.path.join(output_path, structure + ".npz")

    np.savez(npz_file_path, image_array=flipped_array)


def read_npz(full_path: str, dtype: np.dtype):
    """
    Loads the structure npz file and returns it as a numpy array with the selected datatype

    Args:
        full_path (string): the full path to the .npz file
        dtype (np.dtype): the selected datatype for the finished array. Defaults to int8

    Returns:
        read_array (np.ndarray): the array containing the npz data as the selected datatype

    """
    read_array = np.load(full_path)
    read_array = read_array["image_array"]

    # double checks the datatype
    assert read_array.dtype == dtype  # Array does not contain the correct dtype

    return read_array


def run_QA(
    all_structs_array: np.ndarray, dose_array: np.ndarray, brain_array: np.ndarray, desired_shape: tuple
):
    """
    Runs a quality assurance check on the loaded arrays

    Args:
        all_structs_array (np.ndarray): the array containing all the structures
        dose_array (np.ndarray): the array containing the dose
        brain_array (np.ndarray): the array containing the brain segmentation
        desired_shape (tuple): the desired shape of the arrays (slices, height, width)

    """

    #  should make sure that PTV > CTV using sum
    CTV_sum = np.sum(all_structs_array[0])
    PTV_sum = np.sum(all_structs_array[1])

    # assert shape is correct size
    assert (
        dose_array.shape == desired_shape
    ), f"Dose array is not the correct shape\n\tDose_array:{dose_array.shape}, desired shape: {desired_shape}"
    assert (
        brain_array.shape == desired_shape
    ), f"Brain array is not the correct shape\n\tBrain_array:{brain_array.shape}, desired shape: {desired_shape}"
    assert (
        all_structs_array.shape[1:] == desired_shape
    ), f"Structures array is not the correct shape \n\tStructures_array:{all_structs_array.shape[1:]}, desired shape: {desired_shape}"

    assert all_structs_array.shape[0] == len(
        structure_files
    ), f"Number of structures is not correct\n\t Number of structures: {all_structs_array.shape[0]}, expected number of structures: {len(structure_files)}"

    assert CTV_sum < PTV_sum, "CTV is larger than PTV"

    #  Should double check datatypes and expected max and mins
    assert all_structs_array.dtype == np.int8, "Structure array does not contain the correct dtype"
    assert dose_array.dtype == np.float32, "Dose array does not contain the correct dtype"
    assert brain_array.dtype == np.int8, "Brain array does not contain the correct dtype"

    #  Should make sure dose and brain is not empty
    assert np.any(dose_array != 0), "Dose array is empty (only zeros)"
    assert np.any(brain_array != 0), "Brain array is empty (only zeros)"

    #  should check that dose is around 60Gy max must be at least 0.95 (maybe)
    #  This might be different from site to site but it makes sure the maxdose is between 57 and 66
    assert (
        0.95 < np.max(dose_array) < 1.1
    ), f"Patient dose might not be 60 Gy. Max Value in Dose array was {np.max(dose_array)*60}"
    # print(f"Max dose values: {np.max(dose_array)}")

    #  should check that Brain array only contains 1 and 0
    assert np.all(
        np.logical_or(brain_array == 0, brain_array == 1)
    ), "Brain array contains values not == 1 or 0"

    for index, structure in enumerate(structure_files):
        #  Should make sure structure arrays are not empty
        assert np.any(
            all_structs_array[index, :, :, :] != 0
        ), f"The array for {structure} is empty (only zeros)"

        #  Should check that max and min data is 1 and 0 for all structures and brain_array
        assert np.max(all_structs_array[index, :, :, :]) == 1, f"The array for {structure} has values above 1"
        assert np.min(all_structs_array[index, :, :, :]) == 0, f"The array for {structure} has values below 0"
        #  Should check that all structures only contain 1 and 0
        assert np.all(
            np.logical_or(all_structs_array[index, :, :, :] == 0, all_structs_array[index, :, :, :] == 1)
        ), f"Error with array for structure: {structure}, contains values not == 1 or 0"


# ---Visualization functions---
# update_image is called for each slice to update the subplot to show the new slice and change the title of the figure
# Should maybe be moved to a different file.
def update_image(
    zslice: int,
    image_stack: np.ndarray,
    axes_list: list,
    structures: list,
    ax: matplotlib.axes.Axes,
    figure: matplotlib.figure.Figure,
    dose_array: np.ndarray,
    brain_array: np.ndarray,
):
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
    for index, axis in enumerate(axes_list):
        if index == 8:
            image_sum = np.sum(image_stack, axis=0)[zslice, :, :] + brain_array[zslice, :, :]
            axis.set_array(image_sum)
            axis.autoscale()
        elif index == 9:
            axis.set_array(dose_array[zslice, :, :])
        elif index == 10:
            axis.set_array(brain_array[zslice, :, :])
        else:
            axis.set_array(image_stack[index, zslice, :, :])
    figure.suptitle(f"Slice Number: {zslice}")
    for i2 in range(4):
        for i1 in range(3):
            # print(f"i2: {i2},   i1:{i1}\ntotal: {i1*4+i2}")
            # if i2*4+i1 > index-1:
            #     pass
            # else:
            if i1 * 4 + i2 > len(structures) - 1:
                pass
            else:
                ax[i1, i2].set_title(f"{structures[i1*4+i2]}")


# The setup for the subplots
def initial_visual_update(
    ax: matplotlib.axes.Axes, image_stack: np.ndarray, dose_array: np.ndarray, brain_array: np.ndarray
):
    """
    Sets up the subplots:

    Args:
        ax: The matplotlib axes for the plot
        image_stack: the npz array that contains all the structures

    Returns:
        axes_list: a list of the axes objects to be used in the animation
    """

    image_CTV = ax[0, 0].imshow(image_stack[0, 0, :, :], vmin=0, vmax=1)
    image_PTV = ax[0, 1].imshow(image_stack[1, 0, :, :], vmin=0, vmax=1)
    image_brainstem = ax[0, 2].imshow(image_stack[2, 0, :, :], vmin=0, vmax=1)
    image_optic_chiasm = ax[0, 3].imshow(image_stack[3, 0, :, :], vmin=0, vmax=1)
    image_globe_l = ax[1, 0].imshow(image_stack[4, 0, :, :], vmin=0, vmax=1)
    image_globe_r = ax[1, 1].imshow(image_stack[5, 0, :, :], vmin=0, vmax=1)
    image_optic_nerve_l = ax[1, 2].imshow(image_stack[6, 0, :, :], vmin=0, vmax=1)
    image_optic_nerve_r = ax[1, 3].imshow(image_stack[7, 0, :, :], vmin=0, vmax=1)
    image_body = ax[2, 0].imshow(image_stack[8, 0, :, :], vmin=0, vmax=6)
    image_dose = ax[2, 1].imshow(dose_array[0, :, :], vmin=0, vmax=1.1)
    image_brain = ax[2, 2].imshow(brain_array[0, :, :], vmin=0, vmax=1)

    axes_list = [
        image_CTV,
        image_PTV,
        image_brainstem,
        image_optic_chiasm,
        image_globe_l,
        image_globe_r,
        image_optic_nerve_l,
        image_optic_nerve_r,
        image_body,
        image_dose,
        image_brain,
    ]

    return axes_list


def visualize_stack(file_location, dose_array, brain_array):
    """
    Creates a grid of subplots with an animation of the different slices of the structure

    Args:
        file_location (string): the path to the file location array_all_structs file
        dose_array (np.ndarray): the dose array
        brain_array (np.ndarray): the brain array

    """
    image_stack = np.load(os.path.join(file_location, "all_structs.npz"))["image_array"]
    array_size = np.shape(image_stack)
    structures = [
        "CTV",
        "PTV",
        "brainstem",
        "optic_chiasm",
        "globe_L",
        "globe_R",
        "optic_nerve_L",
        "optic_nerve_R",
        "body",
    ]

    structures.append("dose")
    structures.append("Brain")

    fig, ax = plt.subplots(3, 4, figsize=(15, 8))
    axes_list = initial_visual_update(
        ax=ax, image_stack=image_stack, dose_array=dose_array, brain_array=brain_array
    )

    # this section creates the animation to be shown
    fig.subplots_adjust(left=0, right=1, top=0.9, bottom=0.05, hspace=0.25, wspace=0.1)
    ani = FuncAnimation(
        fig=fig,
        func=update_image,
        fargs=[image_stack, axes_list, structures, ax, fig, dose_array, brain_array],
        frames=range(array_size[1]),
        interval=100,
        repeat=True,
    )

    plt.show()


def handle_patient(path_to_patient: str, path_to_output: str, desired_shape: tuple):
    """
    runs the script to convert nifty files to npz files and stack them.
    Generates 3 npz files, one combined for all the structures, one for the dose and one for the brain segmentation.

    Args:
        path_to_patient (str): the full path to the location of the patient.
        path_to_output (str): the full path to the output folder
        desired_shape (tuple): the desired shape of the arrays (slices, height, width)
    """

    # This section reads all the nifty files and converts them into npz files
    output_path = path_to_output

    try:
        os.makedirs(output_path, exist_ok=False)
    except:
        print("folders_exist")
        return

    for structure in structure_files:
        full_path = os.path.join(path_to_patient, structure + ".nii.gz")
        read_and_save_matrix(full_path=full_path, output_path=output_path, structure=structure, dtype=np.int8)

    # Dose is seperate as it is not a part of the structure files list
    full_path = os.path.join(path_to_patient, "dose.nii.gz")
    read_and_save_matrix(full_path=full_path, output_path=output_path, structure="dose", dtype=np.float32)

    full_path = os.path.join(path_to_patient, "brain.nii.gz")
    read_and_save_matrix(full_path=full_path, output_path=output_path, structure="brain", dtype=np.int8)

    all_structs = []

    # This section reads in all the individual structure npz files, then stacks them on top of each other in the correct order
    for (
        structure
    ) in (
        structure_files
    ):  # order of structures is important and is given by the order of the structure files list
        structure_data = read_npz(os.path.join(output_path, structure + ".npz"), dtype=np.int8)
        all_structs.append(structure_data)

    array_all_structs = np.stack(all_structs)
    np.savez(os.path.join(output_path, "all_structs.npz"), image_array=array_all_structs)

    # if os.path.exists(os.path.join(output_path,'all_structs.npz')):
    #     for structure in structure_files:
    #         #pass
    #         os.remove(os.path.join(output_path, structure + '.npz'))

    dose_array = np.load(os.path.join(output_path, "dose.npz"))["image_array"]
    brain_array = np.load(os.path.join(output_path, "brain.npz"))["image_array"]
    print("before cropping")
    print(f"\t{array_all_structs.shape}")
    print(f"\t{dose_array.shape}")

    array_all_structs, dose_array, brain_array = crop_array_to_bounding_box(
        array_all_structs=array_all_structs, dose_array=dose_array, brain_array=brain_array
    )
    print("after cropping")
    print(f"\t{array_all_structs.shape}")
    print(f"\t{dose_array.shape}")

    np.savez(os.path.join(output_path, "all_structs.npz"), image_array=array_all_structs)
    np.savez(os.path.join(output_path, "dose.npz"), image_array=dose_array)
    np.savez(os.path.join(output_path, "brain.npz"), image_array=brain_array)

    if os.path.exists(os.path.join(output_path, "all_structs.npz")):
        for structure in structure_files:
            # pass
            os.remove(os.path.join(output_path, structure + ".npz"))

    all_structs = np.load(os.path.join(output_path, "all_structs.npz"))["image_array"]
    dose_array = np.load(os.path.join(output_path, "dose.npz"))["image_array"]
    brain_array = np.load(os.path.join(output_path, "brain.npz"))["image_array"]

    all_structs, dose_array, brain_array = pad_arrays(
        array_all_structs=all_structs,
        dose_array=dose_array,
        brain_array=brain_array,
        array_shape=desired_shape,
    )

    np.savez(os.path.join(output_path, "all_structs.npz"), image_array=all_structs)
    np.savez(os.path.join(output_path, "dose.npz"), image_array=dose_array)
    np.savez(os.path.join(output_path, "brain.npz"), image_array=brain_array)

    all_structs = np.load(os.path.join(output_path, "all_structs.npz"))["image_array"]
    dose_array = np.load(os.path.join(output_path, "dose.npz"))["image_array"]
    brain_array = np.load(os.path.join(output_path, "brain.npz"))["image_array"]


# ______________________________Cropping and padding______________________________________________________
def generate_bounding_box(body_array: np.ndarray):
    """
    creates a bounding box of the head from the body segmentation

    Args:
        body_array (np.ndarray): An array containing the body segmentation.

    Returns:
        a tuple with the bounding box coordinates (z0, z1, y0, y1, x0, x1)
    """

    shape = body_array.shape
    print(shape)
    coords = np.argwhere(body_array)
    # Bounding box coordinates of the box mask
    z0, y0, x0 = coords.min(axis=0)
    z1, y1, x1 = coords.max(axis=0) + 1  # slices are exclusive at the top

    print([z0, z1, y0, y1, x0, x1])

    return (z0, z1, y0, y1, x0, x1)


def crop_array_to_bounding_box(
    array_all_structs: np.ndarray, dose_array: np.ndarray, brain_array: np.ndarray
):
    """
    Crops the arrays to a bounding box.

    Args:
        array_all_structs (np.ndarray): the array containing all the structures
        dose_array (np.ndarray): dose array
        brain_array (np.ndarray): brain array

    Returns:
        the three input arrays cropped to the bounding box based on the body segmentation
    """

    # Generates a bounding box based on the body segmentation, if more structures are added this should be changed to the body segmentation
    bounding_box = generate_bounding_box(body_array=array_all_structs[8, :, :, :])

    # Crop the arrays to the bounding box
    array_all_structs = array_all_structs[
        :,
        bounding_box[0] : bounding_box[1],
        bounding_box[2] : bounding_box[3],
        bounding_box[4] : bounding_box[5],
    ]
    dose_array = dose_array[
        bounding_box[0] : bounding_box[1],
        bounding_box[2] : bounding_box[3],
        bounding_box[4] : bounding_box[5],
    ]
    brain_array = brain_array[
        bounding_box[0] : bounding_box[1],
        bounding_box[2] : bounding_box[3],
        bounding_box[4] : bounding_box[5],
    ]

    return array_all_structs, dose_array, brain_array


def padAroundImageCenter(imageArray, paddedSize, subject):
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
    assert imageArray.shape[0] <= paddedSize[0], (
        "Image size is larger than requested padded size in row: "
        + str(imageArray.shape[0])
        + " vs "
        + str(paddedSize[0])
        + " in subject "
        + str(subject)
    )
    assert imageArray.shape[1] <= paddedSize[1], (
        "Image size is larger than requested padded size in column: "
        + str(imageArray.shape[1])
        + " vs "
        + str(paddedSize[1])
        + " in subject "
        + str(subject)
    )
    assert imageArray.shape[2] <= paddedSize[2], (
        "Image size is larger than requested padded size in slice: "
        + str(imageArray.shape[2])
        + " vs "
        + str(paddedSize[2])
        + " in subject "
        + str(subject)
    )
    # Get shape of the image array
    origShape = imageArray.shape
    # Caluclate half the difference between the desired
    # size and the original shape and round up
    diff = np.round((np.array(paddedSize) - np.array(origShape)) // 2)
    # Calculate padding. Takes care of case when matrix are uneven size.
    extraLeft = diff[0]
    extraRight = paddedSize[0] - origShape[0] - diff[0]
    extraTop = diff[1]
    extraBottom = paddedSize[1] - origShape[1] - diff[1]
    extraFront = diff[2]
    extraBack = paddedSize[2] - origShape[2] - diff[2]

    # Pad the image array with zeros
    paddedImageArray = np.pad(
        imageArray,
        ((extraLeft, extraRight), (extraTop, extraBottom), (extraFront, extraBack)),
        "constant",
        constant_values=0,
    )
    # Assert correct padded size, very important
    assert paddedImageArray.shape[0] == paddedSize[0], "Padded image size is incorrect in row"
    assert paddedImageArray.shape[1] == paddedSize[1], "Padded image size is incorrect in column"
    assert paddedImageArray.shape[2] == paddedSize[2], "Padded image size is incorrect in slice"
    # Return the padded image array
    return paddedImageArray


def pad_arrays(
    array_all_structs: np.ndarray, dose_array: np.ndarray, brain_array: np.ndarray, array_shape: list
):
    """
    Pads a numpy array to the specified dimensions with constant values (0).
    Args:
        array_all_structs: numpy array to be padded
        dose_array: array with the dose data, will also be padded
        brain_array: array brain data will also be padded.
        array_shape: the shape the arrays should be padded to,  (slices, height, width)

    Returns:
        padded_array_all_structs: the padded array of all the structures
        padded_dose_array: the padded dose array
        padded_brain_array: the padded brain array
    """

    padded_structs = []

    for i in range(array_all_structs.shape[0]):
        padded_structs.append(padAroundImageCenter(array_all_structs[i, :, :, :], array_shape, "all_structs"))
    padded_array_all_structs = np.stack(padded_structs)
    padded_dose_array = padAroundImageCenter(dose_array, array_shape, "dose")
    padded_brain_array = padAroundImageCenter(brain_array, array_shape, "brain")

    return padded_array_all_structs, padded_dose_array, padded_brain_array


def main():
    # The current code will work for code that just came out of the mice script, maybe we want to change it a bit
    # How should the output of the script look? folders or files?

    # visualize the structures or not, For QA purposes mostly
    visualize = True

    max_slices = 112
    max_height = 112
    max_width = 168

    # Path to patient dir should lead to the output folder of the mice batch, the folder where the patients are stored.
    path_to_patient_dir = os.path.join("before")

    # This can be whatever path you want, the script will create folders for each patient in a results folder.
    path_to_output_dir = os.path.join("")

    for patient in os.listdir(path_to_patient_dir):
        output_path = os.path.join(path_to_output_dir, "results", patient)
        patient_path = os.path.join(path_to_patient_dir, patient)

        if os.path.isdir(patient_path):

            # This section double checks that there are not 2 registrations for the patient, and asks you to delete them if there are.
            if len(os.listdir(patient_path)) == 1:
                print([patient_path, os.listdir(patient_path)[0]])
                patient_path = os.path.join(patient_path, os.listdir(patient_path)[0])

                # This is where the actual script runs. Set "visualize" to False if you don't want to view every patient.
                # the visualize script is mostly for confirming that the resulting npz files look like the nifty files.
                handle_patient(
                    path_to_patient=patient_path,
                    path_to_output=output_path,
                    desired_shape=(max_slices, max_height, max_width),
                )

            elif len(os.listdir(patient_path)) > 1:
                print("more than one treatment plan exists")
                print(os.listdir(patient_path))
                print("please choose one of them and remove the other")
            else:
                print(f"Patient {patient} has no treatment plan")
        else:
            print("wrong path")

    output_path = os.path.join(path_to_output_dir, "results")

    # print(max_slices, max_height, max_width)

    # This section runs the QA for all the patients
    for array_dir in os.listdir(output_path):

        all_structs = np.load(os.path.join(output_path, array_dir, "all_structs.npz"))["image_array"]
        dose_array = np.load(os.path.join(output_path, array_dir, "dose.npz"))["image_array"]
        brain_array = np.load(os.path.join(output_path, array_dir, "brain.npz"))["image_array"]

        run_QA(all_structs, dose_array, brain_array, desired_shape=(max_slices, max_height, max_width))

        if visualize:
            visualize_stack(os.path.join(output_path, array_dir), dose_array, brain_array=brain_array)

        print(f"QA Passed for patient {array_dir}")


if __name__ == "__main__":
    main()
