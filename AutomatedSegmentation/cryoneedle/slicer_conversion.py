# Create a new .pt file with the structure needed for 3D Slicer Auto3DSeg extension

import torch
# Define the model path
model_path = ''
# Load the model
checkpoint = torch.load(model_path)
# Creating a new dictionary with the structure dict_keys([‘state_dict’, ‘config’, ‘epoch’, ‘best_metric’])
# Modify the parameters based on hyperparameter files in config folders ./work_dir for the specific model
dic = {}
config_dic = {}
config_dic['sigmoid'] = False
network_dic = {}
network_dic['_target_'] = 'SwinUNETR'
network_dic['feature_size'] = 48
network_dic['img_size'] = 96
network_dic['in_channels'] = 1
network_dic['out_channels'] = 2
network_dic['spatial_dims'] = 3
network_dic['use_checkpoint'] = False
network_dic['use_v2'] = False
config_dic['network'] = network_dic
config_dic['orientation_ras'] = True
config_dic['crop_foreground'] = True
config_dic['resample_resolution'] = [1.0, 1.0, 1.0]
config_dic['normalize_mode'] = 'meanstd'
config_dic['intensity_bounds'] = None
config_dic['roi_size'] = [96,96,64]
config_dic['extra_modalities'] = {}
dic['state_dict'] = checkpoint
dic['config'] = config_dic
dic['epoch'] = 65
dic['best_metric'] = 0.46413002014160154
# Define the file path for saving the dictionary
file_path = ''
# Save the dictionary to a .pt file
torch.save(dic, file_path)