import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
def create_synthetic_dataset(project_path, classes, num_images=500, image_size=(416, 416)):
    """Create synthetic dataset with geometric shapes"""
    
    print(f"🔄 Generating {num_images} synthetic images...")
    

    class_colors = {
        0: [(255, 0, 0), (200, 0, 0), (150, 0, 0)],      # Red variants for rectangle
        1: [(0, 255, 0), (0, 200, 0), (0, 150, 0)],      # Green variants for circle
        2: [(0, 0, 255), (0, 0, 200), (0, 0, 150)]       # Blue variants for triangle
    }
    
    images_created = 0
    annotations_created = 0
    
    for i in range(num_images):
        # Create blank white image
        img = np.ones((image_size[0], image_size[1], 3), dtype=np.uint8) * 255
        
        annotations = []
        
        # Add random number of objects (1-4 objects per image)
        num_objects = random.randint(1, 4)
        
        for j in range(num_objects):
            class_id = random.randint(0, len(classes)-1)
            
            # Random position and size (ensuring objects don't go out of bounds)
            margin = 50
            max_size = 120
            min_size = 40
            
            w = random.randint(min_size, max_size)
            h = random.randint(min_size, max_size)
            x = random.randint(margin, image_size[1] - w - margin)
            y = random.randint(margin, image_size[0] - h - margin)
            
            # Choose color for the class
            color = random.choice(class_colors[class_id])
            
            # Draw shapes based on class
            if class_id == 0:  # Rectangle
                cv2.rectangle(img, (x, y), (x+w, y+h), color, -1)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)  # Border
                
            elif class_id == 1:  # Circle
                radius = min(w, h) // 2
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(img, (center_x, center_y), radius, color, -1)
                cv2.circle(img, (center_x, center_y), radius, (0, 0, 0), 2)  # Border
                
            else:  # Triangle
                pts = np.array([
                    [x + w//2, y],           # Top point
                    [x, y + h],              # Bottom left
                    [x + w, y + h]           # Bottom right
                ], np.int32)
                cv2.fillPoly(img, [pts], color)
                cv2.polylines(img, [pts], True, (0, 0, 0), 2)  # Border
            
            # Convert to YOLO format (normalized coordinates)
            x_center = (x + w/2) / image_size[1]
            y_center = (y + h/2) / image_size[0]
            width = w / image_size[1]
            height = h / image_size[0]
            
            # Ensure values are between 0 and 1
            x_center = max(0, min(1, x_center))
            y_center = max(0, min(1, y_center))
            width = max(0, min(1, width))
            height = max(0, min(1, height))
            
            annotations.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
        
        # Save image
        img_filename = f"img_{i:04d}.jpg"
        cv2.imwrite(f"{project_path}/synthetic_dataset/images/{img_filename}", img)
        images_created += 1
        
        # Save annotation
        if annotations:  # Only save if there are annotations
            ann_filename = f"img_{i:04d}.txt"
            with open(f"{project_path}/synthetic_dataset/labels/{ann_filename}", "w") as f:
                f.write("\n".join(annotations))
            annotations_created += 1
        
        # Progress indicator
        if (i + 1) % 50 == 0:
            print(f"   Generated {i + 1}/{num_images} images...")
    
    # Create classes file
    with open(f"{project_path}/synthetic_dataset/classes.txt", "w") as f:
        f.write("\n".join(classes))
    
    print(f"✅ Synthetic dataset created successfully!")
    print(f"   📁 Images created: {images_created}")
    print(f"   📄 Annotations created: {annotations_created}")
    print(f"   🏷️ Classes: {classes}")
    
    return classes


