import torch
model_path = '/home/nayani/Desktop/automated_segmentation/urethra/monai_model.pt'
checkpoint = torch.load(model_path)
print(checkpoint['state_dict'])
epoch = 96
best_metric = 0.8704135894775391

#swinunetr
epoch = 65
best_metric = 0.46413002014160154