import os
import shutil
import json
from sklearn.model_selection import train_test_split
def smart_dataset_split(PROJECT_PATH, split_ratios=(0.7, 0.2, 0.1)):
    """Intelligently split dataset ensuring balanced distribution"""
    
    print("✂️ Performing smart dataset split...")
    
    # Get all image files
    image_files = [f for f in os.listdir(f"{PROJECT_PATH}/data/synthetic_raw/images") 
                   if f.endswith('.jpg')]
    
    # Analyze class distribution for stratified splitting
    file_class_info = []
    
    for img_file in image_files:
        ann_file = img_file.replace('.jpg', '.txt')
        ann_path = f"{PROJECT_PATH}/data/synthetic_raw/labels/{ann_file}"
        
        if os.path.exists(ann_path):
            with open(ann_path, 'r') as f:
                lines = f.readlines()
            
            # Get primary class (first object in annotation)
            if lines:
                primary_class = int(lines[0].split()[0])
                num_objects = len(lines)
                file_class_info.append((img_file, primary_class, num_objects))
    
    # Convert to structured format for stratified split
    files = [info[0] for info in file_class_info]
    primary_classes = [info[1] for info in file_class_info]
    
    # First split: train vs temp (val + test)
    train_files, temp_files, _, temp_classes = train_test_split(
        files, primary_classes, 
        test_size=(split_ratios[1] + split_ratios[2]), 
        stratify=primary_classes, 
        random_state=42
    )
    
    # Second split: val vs test
    val_size = split_ratios[1] / (split_ratios[1] + split_ratios[2])
    val_files, test_files = train_test_split(
        temp_files,
        test_size=(1 - val_size),
        stratify=temp_classes,
        random_state=42
    )
    
    # Copy files to respective directories
    def copy_files_to_split(file_list, split_name):
        for file in file_list:
            # Copy image
            src_img = f"{PROJECT_PATH}/data/synthetic_raw/images/{file}"
            dst_img = f"{PROJECT_PATH}/data/processed/{split_name}/images/{file}"
            shutil.copy2(src_img, dst_img)
            
            # Copy label
            label_file = file.replace('.jpg', '.txt')
            src_label = f"{PROJECT_PATH}/data/synthetic_raw/labels/{label_file}"
            dst_label = f"{PROJECT_PATH}/data/processed/{split_name}/labels/{label_file}"
            
            if os.path.exists(src_label):
                shutil.copy2(src_label, dst_label)
    
    copy_files_to_split(train_files, 'train')
    copy_files_to_split(val_files, 'val')
    copy_files_to_split(test_files, 'test')
    
    # Save split information
    split_info = {
        'train_count': len(train_files),
        'val_count': len(val_files),
        'test_count': len(test_files),
        'train_files': train_files,
        'val_files': val_files,
        'test_files': test_files,
        'split_ratios': split_ratios
    }
    
    with open(f"{PROJECT_PATH}/data/split_info.json", "w") as f:
        json.dump(split_info, f, indent=2)
    
    print("✅ Smart dataset split completed!")
    print(f"   📚 Training: {len(train_files)} images")
    print(f"   🧪 Validation: {len(val_files)} images")
    print(f"   🔬 Test: {len(test_files)} images")
    
    return split_info

