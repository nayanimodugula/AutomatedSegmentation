import os
import pyigtl
import SimpleITK as sitk
import nibabel as nib
import numpy as np

client = pyigtl.OpenIGTLinkClient("127.0.0.1", 18944)

# the image we are sending
ablationLabelPath = '/home/nayani/Desktop/auto3Dseg/urethra/test.seg.nii.gz'
LabelImage = sitk.ReadImage(ablationLabelPath, sitk.sitkFloat32)
output_path = "/home/nayani/Desktop/auto3Dseg/urethra/new_output_file.nrrd"

while True:
    # receiving an image from 3D Slicer server
    input_image = client.wait_for_message("new_test")
    if input_image:
        spacing = np.ones(3)
        for axis_index in range(3):
            spacing[axis_index] = np.linalg.norm(input_image.ijk_to_world_matrix[:, axis_index])
        origin = input_image.ijk_to_world_matrix[:3,3]
        origin[0] = -origin[0]
        origin[1] = -origin[1]
        sitk_image = sitk.GetImageFromArray(input_image.image)
        sitk_image.SetSpacing(spacing)
        sitk_image.SetOrigin(origin)
        # Save the image to a new file
        sitk.WriteImage(sitk_image, output_path)        
        # sending the image to 3D Slicer server
        output_message = pyigtl.ImageMessage(sitk.GetArrayFromImage(LabelImage), device_name="label_test_image")
        client.send_message(output_message)
