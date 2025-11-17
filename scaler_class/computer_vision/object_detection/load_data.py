import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    """Load and preprocess image for the model"""
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        original_shape = image.shape[:2]
        image = cv2.resize(image, target_size)
        image = image.astype(np.float32) / 255.0
        return image, original_shape
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None, None

def parse_annotation(annotation_path):
    """Parse YOLO format annotation file"""
    boxes = []
    classes = []
    
    try:
        if os.path.exists(annotation_path):
            with open(annotation_path, 'r') as f:
                lines = f.readlines()
                
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    class_id = int(parts[0])
                    x_center = float(parts[1])
                    y_center = float(parts[2])
                    width = float(parts[3])
                    height = float(parts[4])
                    
                    # Convert to corner coordinates (still normalized)
                    x1 = x_center - width/2
                    y1 = y_center - height/2
                    x2 = x_center + width/2
                    y2 = y_center + height/2
                    
                    boxes.append([x1, y1, x2, y2])
                    classes.append(class_id)
        
        return np.array(boxes), np.array(classes)
    
    except Exception as e:
        print(f"Error parsing annotation {annotation_path}: {e}")
        return np.array([]), np.array([])

def create_dataset_from_directory(image_dir, annotation_dir, num_classes):
    """Create dataset from images and annotations directory"""
    
    print(f"🔄 Loading dataset from {image_dir}...")
    
    images = []
    boxes = []
    classes = []
    
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    loaded_count = 0
    skipped_count = 0
    
    for filename in image_files:
        image_path = os.path.join(image_dir, filename)
        annotation_path = os.path.join(annotation_dir, filename.rsplit('.', 1)[0] + '.txt')
        
        # Load image
        image, original_shape = load_and_preprocess_image(image_path)
        if image is None:
            skipped_count += 1
            continue
        
        # Load annotations
        box_coords, class_ids = parse_annotation(annotation_path)
        
        if len(box_coords) > 0:  # Only include images with annotations
            images.append(image)
            # For simplicity, take only the first bounding box
            boxes.append(box_coords[0])
            
            # Convert to one-hot encoding
            class_vector = np.zeros(num_classes)
            if len(class_ids) > 0:
                class_vector[class_ids[0]] = 1
            classes.append(class_vector)
            
            loaded_count += 1
        else:
            skipped_count += 1
    
    print(f"   ✅ Loaded: {loaded_count} samples")
    print(f"   ⚠️ Skipped: {skipped_count} samples")
    
    return np.array(images), np.array(boxes), np.array(classes)

