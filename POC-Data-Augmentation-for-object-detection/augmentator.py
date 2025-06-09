import os
import cv2
from glob import glob
from augment_techniques import (
    flip_horizontal, flip_vertical, rotate_image,
    cut_patch, blur_image,
    adjust_labels_flip, adjust_labels_rotate_90, passthrough_labels
)

def apply_and_save_augmented(img, labels, base_name, out_img_dir, out_lbl_dir, suffix, img_fn, lbl_fn):
    # Save image
    img_path = os.path.join(out_img_dir, base_name + suffix + ".jpg")
    cv2.imwrite(img_path, img_fn(img))
    print(f"[✓] Saved image: {img_path}")

    # Save labels
    lbl_path = os.path.join(out_lbl_dir, base_name + suffix + ".txt")
    with open(lbl_path, 'w') as f:
        f.writelines(lbl_fn(labels))
    print(f"[✓] Saved labels: {lbl_path}")

def augment_images(in_image_dir, in_label_dir, out_image_dir, out_label_dir):
    os.makedirs(out_image_dir, exist_ok=True)
    os.makedirs(out_label_dir, exist_ok=True)

    img_paths = glob(os.path.join(in_image_dir, "*.jpg"))
    print(f"[INFO] Found {len(img_paths)} training images.")

    for img_path in img_paths:
        base = os.path.basename(img_path)
        name = os.path.splitext(base)[0]
        label_path = os.path.join(in_label_dir, name + ".txt")

        if not os.path.exists(label_path):
            print(f"[WARNING] Missing label for {base}, skipping.")
            continue

        img = cv2.imread(img_path)
        if img is None:
            print(f"[ERROR] Could not read image {img_path}, skipping.")
            continue

        with open(label_path, 'r') as f:
            label_lines = f.readlines()

        # Save original
        cv2.imwrite(os.path.join(out_image_dir, name + ".jpg"), img)
        with open(os.path.join(out_label_dir, name + ".txt"), 'w') as f:
            f.writelines(label_lines)
        print(f"[✓] Saved original: {name}.jpg and .txt")

        # Apply augmentations
        apply_and_save_augmented(img, label_lines, name, out_image_dir, out_label_dir, "_h", flip_horizontal, lambda lbls: adjust_labels_flip(lbls, 'h'))
        apply_and_save_augmented(img, label_lines, name, out_image_dir, out_label_dir, "_v", flip_vertical, lambda lbls: adjust_labels_flip(lbls, 'v'))
        apply_and_save_augmented(img, label_lines, name, out_image_dir, out_label_dir, "_rot", rotate_image, adjust_labels_rotate_90)
        apply_and_save_augmented(img, label_lines, name, out_image_dir, out_label_dir, "_cut", cut_patch, passthrough_labels)
        apply_and_save_augmented(img, label_lines, name, out_image_dir, out_label_dir, "_blur", blur_image, passthrough_labels)

    print(f"[INFO] Augmentation completed. Total images processed: {len(img_paths)}")

def copy_validation_set():
    print("\n[INFO] Copying validation set...")
    os.makedirs("dataset_augmented_split/images", exist_ok=True)
    os.makedirs("dataset_augmented_split/labels", exist_ok=True)

    os.system("cp -r dataset_original_split/images/val dataset_augmented_split/images/")
    os.system("cp -r dataset_original_split/labels/val dataset_augmented_split/labels/")

    print("[INFO] Validation set copied without changes.")

if __name__ == "__main__":
    print("[START] Running full dataset augmentation...")
    augment_images(
        in_image_dir="dataset_original_split/images/train",
        in_label_dir="dataset_original_split/labels/train",
        out_image_dir="dataset_augmented_split/images/train",
        out_label_dir="dataset_augmented_split/labels/train"
    )
    copy_validation_set()
    print("[DONE] All images and annotations augmented and saved.")
