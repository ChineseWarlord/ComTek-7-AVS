import os
import pandas as pd
import torch
import cv2 as cv
from glob import glob
from torch.nn.utils.rnn import pad_sequence

class FrameDataset(torch.utils.data.Dataset):
    def __init__(self, root, label_encoder, transform=None, target_transform=None):
        self.root = root
        self.transform = transform
        self.label_encoder = label_encoder
        self.target_transform = target_transform
        self.img_files = sorted(glob(os.path.join(root, 'clips' + '*/*/*/*.jpg')))
        self.columns = ['id', 'class','x1','y1','x2','y2']

    def __len__(self):
        return len(self.img_files)

    def __getitem__(self, idx):
        #Read img and annotation
        img_path = self.img_files[idx]
        annotations_path = img_path.replace('clips', 'annotations').replace('.jpg', '.txt').replace('frame', 'annotations')
        
        #Turn frame to tensor. Ready to return. Might need to change if we need temporal info
        frame = torch.tensor(cv.imread(img_path))

        #Reading annotations as a DataFrame due to strings. Maybe there is a more optimal way
        annos = pd.read_csv(annotations_path, names = self.columns, delimiter=' ', usecols= range(6))

        target = {}
        target['boxes'] = torch.tensor(annos[['x1', 'y1', 'x2', 'y2']].astype(float).to_numpy())
        target['labels'] = torch.tensor(self.label_encoder.transform(annos['class']))
    
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return frame, target
    
def custom_collate(batches):
    # batches is a list of samples, where each sample is a tuple (frame, target)
    frame, _ = zip(*batches)

    # Append each box/label tensor into their own variable
    boxes_list = [target["boxes"] for _, target in batches]
    labels_list = [target["labels"] for _, target in batches]
    # print(f"boxes list: {boxes_list}")
    # print(f"labels list: {labels_list}")

    # For each batch we pad the samples so they match the biggest tensor
    padded_boxes = pad_sequence(boxes_list, True)
    padded_labels = pad_sequence(labels_list, True)
    # print(f"padded_boxes: {padded_boxes}")
    # print(f"padded_labels: {padded_labels}")

    # Pack everything nicely as before
    packed_batch = [frame, {"boxes": padded_boxes, "labels": padded_labels}]
    # print(f"packed_batch: {packed_batch}")

    return packed_batch