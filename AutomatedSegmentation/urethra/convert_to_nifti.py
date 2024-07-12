import SimpleITK as sitk
import os
import nibabel as nib
from sklearn.preprocessing import MinMaxScaler

dir = os.listdir("./Pedro_segmentations_255")
for i in dir:
    img = sitk.ReadImage("./Pedro_segmentations_255/"+i)
    sitk.WriteImage(img, "./Pedro_segmentations_255/"+i[:-4]+"nii.gz")
    nifti_img = nib.load("./Pedro_segmentations_255/"+i[:-4]+"nii.gz")
    # Rescale intensity values to the range [0, 1]
    data = nifti_img.get_fdata()
    data_reshaped = data.reshape(-1, 1) 
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data_reshaped).reshape(data.shape)
    rescaled_img = nib.Nifti1Image(data_scaled, nifti_img.affine)
    # Save the rescaled image to a new file
    output_path = "./Pedro_segmentations_1/"+i[:-4]+"nii.gz"
    nib.save(rescaled_img, output_path)