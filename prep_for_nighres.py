import numpy as np
import nibabel as nib

config = "./config.yml"

def prep_for_nighres(input_file):
    
    ## first load labelmap and binarize one edge that includes the inner surf and one edge the outer
    lbl_nib = nib.load(input_file)
    lbl = lbl_nib.get_fdata()

    source = np.zeros(lbl.shape)
    for i in config["laplace_labels"]["src"]:
        source[lbl == i] = 1
    bin_nib = nib.Nifti1Image(source, lbl_nib.affine, lbl_nib.header)
    innerbin = nib.save(bin_nib, './output')

    sink = np.zeros(lbl.shape)
    sink[lbl > 0] = 1
    bin_nib = nib.Nifti1Image(sink, lbl_nib.affine, lbl_nib.header)
    outerbin = nib.save(bin_nib, './output')

    return innerbin, outerbin


