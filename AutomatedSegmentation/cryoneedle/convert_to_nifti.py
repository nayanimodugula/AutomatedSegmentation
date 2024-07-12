import SimpleITK as sitk
import os
import nibabel as nib

dir = os.listdir("./Needlemask")
for i in dir:
    img = sitk.ReadImage("./Needlemask/"+i)
    sitk.WriteImage(img, "./Needlemask/"+i[:-4]+"nii.gz")
    nifti_img = nib.load("./Needlemask/"+i[:-4]+"nii.gz")
    # Convert values greater than 1 to 1
    data = nifti_img.get_fdata()
    data[data>1] = 1
    rescaled_img = nib.Nifti1Image(data, nifti_img.affine)
    # Save the rescaled image to a new file
    output_path = "./Needlemask1/"+i[:-4]+"nii.gz"
    nib.save(rescaled_img, output_path)
