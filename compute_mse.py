import nibabel as nib
from sklearn.metrics import mean_squared_error 

# compute the mean squared error between 2 nii files
def compute_mse(laynii_file_path, master_file_path):
    
    # Load the NIfTI image objects
    read_laynii_img = nib.load(laynii_file_path)
    read_master_img = nib.load(master_file_path)

    # Convert the objects to NumPy arrays
    pred_laynii = read_laynii_img.get_fdata()
    truth_master = read_master_img.get_fdata()

    print("got to here")
    # flatten arrays for mean_squared_error function
    mse = mean_squared_error(truth_master.flatten(), pred_laynii.flatten())
    
    return mse

if __name__ == "__main__":
    
    # File paths to LayNii file and master file (edit to correct location)
    laynii_file_path = "laynii_test_data/sub-01_dir-IO_hemi-R_space-corobl_label-hipp_desc-equidist_coords.nii.gz"
    master_file_path = "master_test_data/sub-01_dir-IO_hemi-R_space-corobl_label-hipp_desc-equivol_coords.nii.gz"

    try:
        # Calculate mse
        mse = compute_mse(laynii_file_path, master_file_path)

        print(f"mse: {mse:.4f}")
    except Exception as e:
        print(f"Error: {e}")
