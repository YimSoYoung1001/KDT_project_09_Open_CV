from torchvision.datasets import ImageFolder
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
import torchvision.transforms as transforms
import cv2
import numpy as np
import pandas as pd
from PIL import Image



def apply_adaptive_threshold(img):
    gray_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    th_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return Image.fromarray(th_img)

def apply_clahe_and_threshold(img):
    img_yuv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2YUV)
    img_clahe = img_yuv.copy()
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    img_clahe[:,:,0] = clahe.apply(img_clahe[:,:,0])
    img_clahe = cv2.cvtColor(img_clahe, cv2.COLOR_YUV2BGR)

    return apply_adaptive_threshold(img_clahe)


class Mob_Dog(nn.Module):
    def __init__(self):
        super(Mob_Dog, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 9 * 9, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 2)
        self.dropout = nn.Dropout(p=0.5)  # Dropout 추가
        self.batchnorm1 = nn.BatchNorm2d(6)  # Batch Normalization 추가
        self.batchnorm2 = nn.BatchNorm2d(16)  # Batch Normalization 추가
        self.batchnorm3 = nn.BatchNorm1d(120)  # Batch Normalization 추가
        self.batchnorm4 = nn.BatchNorm1d(84)  # Batch Normalization 추가
        
    def forward(self, x):
        x = self.pool(F.relu(self.batchnorm1(self.conv1(x))))
        x = self.pool(F.relu(self.batchnorm2(self.conv2(x))))  # Batch Normalization 추가
        
        x = x.view(-1, 16 * 9 * 9)
        x = F.relu(self.batchnorm3(self.fc1(x)))  # Batch Normalization 추가
        x = F.relu(self.batchnorm4(self.fc2(x)))  # Batch Normalization 추가
        x = self.dropout(x)  # Dropout 추가
        x = self.fc3(x)
        return x
    
def get_accuracy(loader, model):
    total=0
    correct=0
    for data in loader:
        images, labels = data
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1) 
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    return correct / total