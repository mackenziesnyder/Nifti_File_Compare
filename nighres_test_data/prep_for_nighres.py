import numpy as np
import nibabel as nib
import yaml

# Load the YAML configuration file
with open("./config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

def prep_for_nighres(input_file):
    
    # Load labelmap and binarize one edge that includes the inner surf and one edge the outer
    lbl_nib = nib.load(input_file)
    lbl = lbl_nib.get_fdata()

    source = np.zeros(lbl.shape)
    for i in config["laplace_labels"]["src"]:
        source[lbl == i] = 1
    bin_nib = nib.Nifti1Image(source, lbl_nib.affine, lbl_nib.header)
    nib.save(bin_nib, './output_inner.nii')

    sink = np.zeros(lbl.shape)
    sink[lbl > 0] = 1
    bin_nib = nib.Nifti1Image(sink, lbl_nib.affine, lbl_nib.header)
    nib.save(bin_nib, './output_outer.nii')

    return './output_inner.nii', './output_outer.nii'



