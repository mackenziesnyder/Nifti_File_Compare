import nibabel as nib
import numpy as np

# Function to threshold values based on binary range [0, 1]
def threshold_values(arr):
    arr[arr > 1] = 1
    arr[arr < 0] = 0

def calculate_dice_score(laynii_file_path, master_file_path):
    
    # Load the NIfTI image objects
    read_laynii_img = nib.load(laynii_file_path)
    read_master_img = nib.load(master_file_path)

    # Convert the objects to NumPy arrays
    pred_laynii = read_laynii_img.get_fdata()
    ground_truth_master = read_master_img.get_fdata()

    # Apply thresholding to keep values within binary range
    pred_laynii_t = threshold_values(pred_laynii)
    ground_truth_master_t = threshold_values(ground_truth_master)

    # Calculate the area of overlap
    area_overlap = np.sum(pred_laynii_t * ground_truth_master_t)

    # Calculate the total sum
    total_sum = np.sum(pred_laynii_t) + np.sum(ground_truth_master_t)

    # Calculate Dice coefficient
    dice_pred = (2 * area_overlap) / total_sum

    return dice_pred


if __name__ == "__main__":
    
    # File paths to LayNii file and master file (edit to correct location)
    laynii_file_path = "laynii_output_files/sub-01_dir-IO_hemi-L_space-corobl_label-hipp_desc-equivol_coords.nii.gz"
    master_file_path = "master_output_files/sub-01_dir-IO_hemi-L_space-corobl_label-hipp_desc-equivol_coords.nii.gz"

    try:
        # Calculate Dice prediction
        dice_pred = calculate_dice_score(laynii_file_path, master_file_path)

        print(f"Dice score prediction: {dice_pred:.4f}")
    except Exception as e:
        print(f"Error: {e}")
