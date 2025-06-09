# 📦 Data Augmentation for Object Detection (YOLOv5 + COCO128)

This project demonstrates how simple data augmentation techniques (flip, rotate, blur, cut) can impact object detection performance using the YOLOv5 model on a limited dataset (COCO128).

---

## 🚀 Training

Train the YOLOv5 model on the **original dataset**:

**python3 train_original.py --epochs 30 --batch 16 --data dataset_original.yaml --name train_original --project results**

Train on the **augmented dataset**:

**python3 train_augmented.py --epochs 30 --batch 16 --data dataset_augmented.yaml --name train_aug --project results**

Optional arguments:
- **--epochs**: Number of epochs to train
- **--batch**: Batch size
- **--data**: Path to the YOLOv5 `.yaml` dataset file
- **--name**: Experiment name (used for folder name)
- **--project**: Output folder for training results

---

## 🧪 Evaluation

After training, evaluate the result logs using:

**python3 evaluate.py --csv results/train_original/exp/results.csv**

This will:
- Generate `metrics_plot.png` with precision, recall, and mAP
- Print maximum values for each metric

---

## 🔁 Data Augmentation

To apply augmentations (horizontal flip, vertical flip) on the training set:

**python3 augmentator.py**

This script will:
- Read images and YOLO labels from `dataset_original_split`
- Save the augmented dataset in `dataset_augmented_split`
- Automatically copy the validation set unmodified

You can edit `augment_techniques.py` to add more transformations like **blur**, **rotate**, or **cut-paste**.

---

## ✅ Requirements

- Python 3.8+
- OpenCV
- NumPy
- Matplotlib
- SciPy
- YOLOv5 requirements (install with `pip install -r yolov5/requirements.txt`)



## Common commands

python3 train_original.py \
  --epochs 30 \
  --batch 8 \
  --name model_orig_ep30 \
  --project /root/projects/CV-proiect/yolov5-results \
  --data ./dataset_original.yaml


python3 train_original.py \
  --epochs 100 \
  --batch 16 \
  --img 640 \
  --data dataset_original.yaml \
  --weights yolov5s.pt \
  --name model_ep100 \
  --project /root/projects/CV-proiect/yolov5-results




python3 train_augmented.py \
  --epochs 30 \
  --batch 8 \
  --name model_aug_ep30 \
  --data ./dataset_original.yaml

  --project /root/projects/CV-proiect/yolov5-results