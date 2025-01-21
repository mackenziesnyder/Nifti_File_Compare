import nighres
from shutil import copyfile
from nighres_test_data.prep_for_nighres import prep_for_nighres

def apply_nighres(innerbin, outerbin, output_dir):

   nighres_args = {"save_data": True, "output_dir": output_dir, "overwrite": True}

   ## convert binarized edges to levelset surfaces
   levelset_inner = nighres.surface.probability_to_levelset(innerbin, **nighres_args)
   levelset_outer = nighres.surface.probability_to_levelset(outerbin, **nighres_args)

   print("binarized files to levelsets complete")

   ## get isovolume solution
   isovolume = nighres.laminar.volumetric_layering(
       levelset_inner["result"], levelset_outer["result"], **nighres_args
   )

   print("levelset to isovolume complete")

   ## copy to output (volumetric_layering produces multiple files so we need to specify the right one)
   copyfile(isovolume["depth"], output_dir)

if __name__ == '__main__':
   input_nii = '../laynii_test_data/sc_rim.nii.gz'
   output_dir = '../output'
   innerbin, outerbin = prep_for_nighres(input_nii)
   apply_nighres(innerbin, outerbin, output_dir)
