import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
def visualize_synthetic_samples(project_path, num_samples=6):
    """Visualize sample synthetic images with annotations"""
    
    print("🖼️ Visualizing synthetic dataset samples...")
    
    # Get list of image files
    image_files = os.listdir(f"{project_path}/synthetic_dataset/images")
    image_files = sorted([f for f in image_files if f.endswith('.jpg')])
    
    # Select random samples
    sample_files = random.sample(image_files, min(num_samples, len(image_files)))
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    classes = ["rectangle", "circle", "triangle"]
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # BGR format
    
    for idx, img_file in enumerate(sample_files):
        # Load image
        img_path = f"{project_path}/synthetic_dataset/images/{img_file}"
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Load annotations
        ann_file = img_file.replace('.jpg', '.txt')
        ann_path = f"{project_path}/synthetic_dataset/labels/{ann_file}"
        
        if os.path.exists(ann_path):
            with open(ann_path, 'r') as f:
                lines = f.readlines()
            
            h, w = img.shape[:2]
            
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    class_id = int(parts[0])
                    x_center = float(parts[1]) * w
                    y_center = float(parts[2]) * h
                    width = float(parts[3]) * w
                    height = float(parts[4]) * h
                    
                    # Convert to corner coordinates
                    x1 = int(x_center - width/2)
                    y1 = int(y_center - height/2)
                    x2 = int(x_center + width/2)
                    y2 = int(y_center + height/2)
                    
                    # Draw bounding box
                    color = colors[class_id]
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                    
                    # Add label
                    label = classes[class_id]
                    cv2.putText(img, label, (x1, y1-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        axes[idx].imshow(img)
        axes[idx].set_title(f'Sample {idx+1}')
        axes[idx].axis('off')
    
    plt.tight_layout()
    plt.suptitle('Synthetic Dataset Samples with Annotations', y=1.02, fontsize=16)
    plt.savefig(f'{project_path}/results/synthetic_samples.png', dpi=300, bbox_inches='tight')
    plt.show()

