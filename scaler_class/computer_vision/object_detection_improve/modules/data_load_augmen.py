import os
import cv2
import numpy as np
import random

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    """Enhanced image loading with better preprocessing"""
    try:
        # Load image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        original_shape = image.shape[:2]
        
        # Resize with proper aspect ratio handling
        image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
        
        # Enhanced normalization
        image = image.astype(np.float32) / 255.0
        
        # Optional: histogram equalization for better contrast
        # image = enhance_contrast(image)
        
        return image, original_shape
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None, None

def parse_annotation_enhanced(annotation_path):
    """Enhanced annotation parsing with validation"""
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
                    
                    # Validate coordinates
                    if not (0 <= x_center <= 1 and 0 <= y_center <= 1 and 
                           0 < width <= 1 and 0 < height <= 1):
                        continue
                    
                    # Convert to corner coordinates
                    x1 = x_center - width/2
                    y1 = y_center - height/2
                    x2 = x_center + width/2
                    y2 = y_center + height/2
                    
                    # Ensure coordinates are within bounds
                    x1 = max(0, min(1, x1))
                    y1 = max(0, min(1, y1))
                    x2 = max(0, min(1, x2))
                    y2 = max(0, min(1, y2))
                    
                    boxes.append([x1, y1, x2, y2])
                    classes.append(class_id)
        
        return np.array(boxes), np.array(classes)
    
    except Exception as e:
        print(f"Error parsing annotation {annotation_path}: {e}")
        return np.array([]), np.array([])

class AdvancedDataGenerator:
    """Advanced data generator with sophisticated augmentation"""
    
    def __init__(self, image_dir, annotation_dir, num_classes, batch_size=16, 
                 augment=True, shuffle=True):
        self.image_dir = image_dir
        self.annotation_dir = annotation_dir
        self.num_classes = num_classes
        self.batch_size = batch_size
        self.augment = augment
        self.shuffle = shuffle
        
        # Get all valid files
        self.image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
        self.valid_files = []
        
        # Filter files with valid annotations
        for img_file in self.image_files:
            ann_file = img_file.replace('.jpg', '.txt')
            ann_path = os.path.join(annotation_dir, ann_file)
            if os.path.exists(ann_path):
                self.valid_files.append(img_file)
        
        print(f"   Found {len(self.valid_files)} valid files in {image_dir}")
        
        if self.shuffle:
            random.shuffle(self.valid_files)
    
    def __len__(self):
        return len(self.valid_files) // self.batch_size
    
    def __getitem__(self, idx):
        batch_files = self.valid_files[idx * self.batch_size:(idx + 1) * self.batch_size]
        
        batch_images = []
        batch_boxes = []
        batch_classes = []
        
        for file in batch_files:
            img_path = os.path.join(self.image_dir, file)
            ann_path = os.path.join(self.annotation_dir, file.replace('.jpg', '.txt'))
            
            # Load image and annotation
            image, _ = load_and_preprocess_image(img_path)
            boxes, classes = parse_annotation_enhanced(ann_path)
            
            if image is not None and len(boxes) > 0:
                # Apply augmentation if enabled
                if self.augment:
                    image, box = self.augment_sample(image, boxes[0])
                else:
                    box = boxes[0]
                
                # Convert class to one-hot
                class_vector = np.zeros(self.num_classes)
                if len(classes) > 0:
                    class_vector[classes[0]] = 1
                
                batch_images.append(image)
                batch_boxes.append(box)
                batch_classes.append(class_vector)
        
        return (np.array(batch_images), 
                {'classification': np.array(batch_classes),
                 'bbox_regression': np.array(batch_boxes)})
    
    def augment_sample(self, image, bbox):
        """Apply sophisticated augmentation while preserving bbox accuracy"""
        
        # Convert bbox to pixel coordinates for augmentation
        h, w = image.shape[:2]
        x1, y1, x2, y2 = bbox
        
        # Random brightness and contrast
        if np.random.random() > 0.5:
            brightness = np.random.uniform(0.8, 1.2)
            image = np.clip(image * brightness, 0, 1)
        
        if np.random.random() > 0.5:
            contrast = np.random.uniform(0.8, 1.2)
            image = np.clip((image - 0.5) * contrast + 0.5, 0, 1)
        
        # Random horizontal flip
        if np.random.random() > 0.5:
            image = cv2.flip(image, 1)
            # Adjust bbox for flip
            x1_new = 1 - x2
            x2_new = 1 - x1
            x1, x2 = x1_new, x2_new
        
        # Small random translation (preserve bbox relationship)
        if np.random.random() > 0.7:
            tx = np.random.uniform(-0.1, 0.1)
            ty = np.random.uniform(-0.1, 0.1)
            
            # Apply translation to image (simplified)
            # In production, you'd use proper affine transformation
            pass
        
        # Ensure bbox is still valid
        x1 = max(0, min(1, x1))
        y1 = max(0, min(1, y1))
        x2 = max(0, min(1, x2))
        y2 = max(0, min(1, y2))
        
        return image, np.array([x1, y1, x2, y2])
    
    def get_all_data(self):
        """Get all data at once (for smaller datasets)"""
        images = []
        boxes = []
        classes = []
        
        for file in self.valid_files:
            img_path = os.path.join(self.image_dir, file)
            ann_path = os.path.join(self.annotation_dir, file.replace('.jpg', '.txt'))
            
            image, _ = load_and_preprocess_image(img_path)
            box_coords, class_ids = parse_annotation_enhanced(ann_path)
            
            if image is not None and len(box_coords) > 0:
                images.append(image)
                boxes.append(box_coords[0])  # Take first box
                
                class_vector = np.zeros(self.num_classes)
                if len(class_ids) > 0:
                    class_vector[class_ids[0]] = 1
                classes.append(class_vector)
        
        return np.array(images), np.array(boxes), np.array(classes)

