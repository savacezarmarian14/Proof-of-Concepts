import os
import random
from shutil import copyfile

image_dir = "dataset_original/images/train2017"
label_dir = "dataset_original/labels/train2017"

train_img_out = "dataset_original_split/images/train"
val_img_out   = "dataset_original_split/images/val"
train_lbl_out = "dataset_original_split/labels/train"
val_lbl_out   = "dataset_original_split/labels/val"

os.makedirs(train_img_out, exist_ok=True)
os.makedirs(val_img_out, exist_ok=True)
os.makedirs(train_lbl_out, exist_ok=True)
os.makedirs(val_lbl_out, exist_ok=True)

images = [f for f in os.listdir(image_dir)
          if f.endswith('.jpg') and os.path.exists(os.path.join(label_dir, f.replace('.jpg', '.txt')))]

random.shuffle(images)
split_index = int(0.8 * len(images))
train_images = images[:split_index]
val_images = images[split_index:]

for img in train_images:
    lbl = img.replace('.jpg', '.txt')
    copyfile(os.path.join(image_dir, img), os.path.join(train_img_out, img))
    copyfile(os.path.join(label_dir, lbl), os.path.join(train_lbl_out, lbl))

for img in val_images:
    lbl = img.replace('.jpg', '.txt')
    copyfile(os.path.join(image_dir, img), os.path.join(val_img_out, img))
    copyfile(os.path.join(label_dir, lbl), os.path.join(val_lbl_out, lbl))

print(f"Train: {len(train_images)} imagini\nVal: {len(val_images)} imagini")
