import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
def split_dataset(project_path, test_size=0.2):
    """Split synthetic dataset into train and validation sets"""
    
    print("🔄 Splitting dataset into train and validation sets...")
    
    # Get all image files
    image_files = os.listdir(f"{project_path}/synthetic_dataset/images")
    image_files = [f for f in image_files if f.endswith('.jpg')]
    
    # Split files
    train_files, val_files = train_test_split(
        image_files, 
        test_size=test_size, 
        random_state=42,
        shuffle=True
    )
    
    # Copy files to respective directories
    import shutil
    
    # Copy training files
    for file in train_files:
        # Copy image
        src_img = f"{project_path}/synthetic_dataset/images/{file}"
        dst_img = f"{project_path}/dataset/train/images/{file}"
        shutil.copy2(src_img, dst_img)
        
        # Copy label
        label_file = file.replace('.jpg', '.txt')
        src_label = f"{project_path}/synthetic_dataset/labels/{label_file}"
        dst_label = f"{project_path}/dataset/train/labels/{label_file}"
        
        if os.path.exists(src_label):
            shutil.copy2(src_label, dst_label)
    
    # Copy validation files
    for file in val_files:
        # Copy image
        src_img = f"{project_path}/synthetic_dataset/images/{file}"
        dst_img = f"{project_path}/dataset/val/images/{file}"
        shutil.copy2(src_img, dst_img)
        
        # Copy label
        label_file = file.replace('.jpg', '.txt')
        src_label = f"{project_path}/synthetic_dataset/labels/{label_file}"
        dst_label = f"{project_path}/dataset/val/labels/{label_file}"
        
        if os.path.exists(src_label):
            shutil.copy2(src_label, dst_label)
    
    # Copy classes file
    shutil.copy2(f"{project_path}/synthetic_dataset/classes.txt", 
                 f"{project_path}/dataset/classes.txt")
    
    print(f"✅ Dataset split completed!")
    print(f"   📚 Training samples: {len(train_files)}")
    print(f"   🧪 Validation samples: {len(val_files)}")
    
    return len(train_files), len(val_files)

