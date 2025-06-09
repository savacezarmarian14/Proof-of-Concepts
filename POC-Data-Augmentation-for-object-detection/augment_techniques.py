import cv2
import numpy as np

# =============== IMAGE AUGMENTATION FUNCTIONS ===============

def flip_horizontal(img):
    return cv2.flip(img, 1)

def flip_vertical(img):
    return cv2.flip(img, 0)

def rotate_image(img, angle=90):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(img, matrix, (w, h))

def cut_patch(img, x=50, y=50, w=100, h=100):
    patch = img[y:y+h, x:x+w].copy()
    paste_x = min(img.shape[1] - w - 1, x + 40)
    paste_y = min(img.shape[0] - h - 1, y + 40)
    img_copy = img.copy()
    img_copy[paste_y:paste_y+h, paste_x:paste_x+w] = patch
    return img_copy

def blur_image(img, kernel_size=5):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

# =============== LABEL ADJUSTMENT FUNCTIONS (YOLO format) ===============

def adjust_labels_flip(label_lines, mode):
    updated = []
    for line in label_lines:
        cls, x, y, w, h = map(float, line.strip().split())
        if mode == 'h':
            x = 1.0 - x
        elif mode == 'v':
            y = 1.0 - y
        updated.append(f"{int(cls)} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")
    return updated

def adjust_labels_rotate_90(label_lines):
    rotated = []
    for line in label_lines:
        cls, x, y, w, h = map(float, line.strip().split())
        # YOLO format: center x, y => rotate 90 CW: x' = y, y' = 1 - x
        new_x = y
        new_y = 1.0 - x
        rotated.append(f"{int(cls)} {new_x:.6f} {new_y:.6f} {h:.6f} {w:.6f}\n")  # swapped w and h
    return rotated

def passthrough_labels(label_lines):
    return label_lines.copy()  # no change
