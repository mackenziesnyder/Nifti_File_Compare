import nibabel as nib
import numpy as np

def invert_nii_colors(input_nii, output_nii):
    
    # load the NIfTI file
    img = nib.load(input_nii)
    
    # get the image data as a numpy array
    img_data = img.get_fdata()
    
    # invert the image data (assuming the image is in the range 0-255)
    inverted_data = np.max(img_data) - img_data
    
    # create a new NIfTI image with the inverted data
    inverted_img = nib.Nifti1Image(inverted_data, img.affine)
    
    # save the inverted image to a new file
    nib.save(inverted_img, output_nii)

if __name__ in "__main__":

    input_nii = 'data/'
    output_nii = 'output/'

    invert_nii_colors(input_nii, output_nii)