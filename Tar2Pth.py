import os 
import utils
import datetime
import pickle as pkl
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import transforms as T

from torch.optim import lr_scheduler
from torchvision import datasets, models, transforms
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

def initializeModel(pretrained, num_classes):
    """
    Loads the Faster RCNN ResNet50 model from torchvision, and sets whether it is COCO pretrained, and adjustes the heds box predictor to our number of classes.

    Input:
        pretrained: Whether to use a CoCo pretrained model
        num_classes: How many classes we have:

    Output:
        model: THe initialized PyTorch model
    """
    
    # Load model
    model = models.detection.fasterrcnn_resnet50_fpn(pretrained=pretrained)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model

pretrained = False
num_classes = 2
model = initializeModel(pretrained, num_classes)
device = 'cuda'
device = torch.device(device if torch.cuda.is_available() else "cpu")
print(device)
save_files={}
checkpoint = torch.load("D:\\bishe\\FasterRCNN\\front_full_faster_RCNN_resnet50_30epochs.tar", map_location=device)
model.load_state_dict(checkpoint['model_state_dict'])
save_files['model'] = model.state_dict()
torch.save(save_files, "front_full_faster_RCNN_resnet50_30epochs.pth")
print("Done")

checkpoint = torch.load("D:\\bishe\\FasterRCNN\\front_head_faster_RCNN_resnet50_30epochs.tar", map_location=device)
model.load_state_dict(checkpoint['model_state_dict'])
save_files['model'] = model.state_dict()
torch.save(save_files, "front_head_faster_RCNN_resnet50_30epochs.pth")
print("Done")

checkpoint = torch.load("D:\\bishe\\FasterRCNN\\top_full_faster_RCNN_resnet50_30epochs.tar", map_location=device)
model.load_state_dict(checkpoint['model_state_dict'])
save_files['model'] = model.state_dict()
torch.save(save_files, "top_full_faster_RCNN_resnet50_30epochs.pth")
print("Done")

checkpoint = torch.load("D:\\bishe\\FasterRCNN\\top_head_faster_RCNN_resnet50_30epochs.tar", map_location=device)
model.load_state_dict(checkpoint['model_state_dict'])
save_files['model'] = model.state_dict()
torch.save(save_files, "top_head_faster_RCNN_resnet50_30epochs.pth")
print("Done")