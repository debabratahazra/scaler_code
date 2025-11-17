import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import json
def create_high_quality_synthetic_dataset(PROJECT_PATH, classes, num_images=2000, image_size=(224, 224), split_ratios=(0.7, 0.2, 0.1)):
    """Create high-quality synthetic dataset with varied complexity"""
    
    print(f"🎨 Generating {num_images} high-quality synthetic images...")
    
    # Enhanced color palette with better contrast
    color_palettes = {
        'bright': [(255, 100, 100), (100, 255, 100), (100, 100, 255)],
        'warm': [(255, 180, 100), (255, 150, 150), (200, 100, 255)],
        'cool': [(100, 200, 255), (150, 255, 200), (200, 150, 255)],
        'earth': [(139, 69, 19), (107, 142, 35), (160, 82, 45)]
    }
    
    # Track dataset statistics
    stats = {
        'total_images': 0,
        'total_objects': 0,
        'class_distribution': {cls: 0 for cls in classes},
        'size_distribution': {'small': 0, 'medium': 0, 'large': 0},
        'complexity_distribution': {'single': 0, 'multiple': 0}
    }
    
    for i in range(num_images):
        # Create varied backgrounds
        if np.random.random() > 0.7:
            # Gradient background
            background = create_gradient_background(image_size)
        else:
            # Solid background with texture
            bg_color = np.random.randint(200, 256, 3)
            background = np.full((image_size[0], image_size[1], 3), bg_color, dtype=np.uint8)
            # Add subtle texture
            noise = np.random.normal(0, 5, background.shape).astype(np.int16)
            background = np.clip(background.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        
        img = background.copy()
        annotations = []
        
        # Varied object complexity
        complexity_weights = [0.6, 0.25, 0.1, 0.05]  # 1, 2, 3, 4 objects
        num_objects = np.random.choice([1, 2, 3, 4], p=complexity_weights)
        
        if num_objects == 1:
            stats['complexity_distribution']['single'] += 1
        else:
            stats['complexity_distribution']['multiple'] += 1
        
        placed_boxes = []
        successful_placements = 0
        
        for j in range(num_objects):
            class_id = random.randint(0, len(classes)-1)
            stats['class_distribution'][classes[class_id]] += 1
            
            # Enhanced size variation
            size_type = np.random.choice(['small', 'medium', 'large'], p=[0.3, 0.5, 0.2])
            if size_type == 'small':
                base_size = np.random.randint(25, 45)
            elif size_type == 'medium':
                base_size = np.random.randint(45, 80)
            else:  # large
                base_size = np.random.randint(80, 120)
            
            stats['size_distribution'][size_type] += 1
            
            # Aspect ratio variation
            aspect_ratio = np.random.uniform(0.7, 1.4)
            w = int(base_size * np.sqrt(aspect_ratio))
            h = int(base_size / np.sqrt(aspect_ratio))
            
            # Ensure reasonable bounds
            w = max(20, min(140, w))
            h = max(20, min(140, h))
            
            # Smart placement to avoid overlap
            placement_success = False
            max_attempts = 50
            
            for attempt in range(max_attempts):
                margin = 15
                x = random.randint(margin, image_size[1] - w - margin)
                y = random.randint(margin, image_size[0] - h - margin)
                
                current_box = [x, y, x+w, y+h]
                
                # Check overlap with existing objects
                overlap = False
                for existing_box in placed_boxes:
                    if calculate_box_overlap(current_box, existing_box) > 0.15:
                        overlap = True
                        break
                
                if not overlap:
                    placed_boxes.append(current_box)
                    placement_success = True
                    break
            
            if not placement_success:
                continue
            
            successful_placements += 1
            
            # Choose color palette and specific color
            palette_name = np.random.choice(list(color_palettes.keys()))
            base_color = color_palettes[palette_name][class_id % len(color_palettes[palette_name])]
            
            # Add color variation
            color_variation = np.random.randint(-40, 41, 3)
            color = tuple(int(c) for c in np.clip(np.array(base_color) + color_variation, 0, 255))
            
            # Draw enhanced shapes
            if class_id == 0:  # Rectangleuit
                
                draw_enhanced_rectangle(img, (x, y, x+w, y+h), color)
            elif class_id == 1:  # Circle
                draw_enhanced_circle(img, (x, y, x+w, y+h), color)
            else:  # Triangle
                draw_enhanced_triangle(img, (x, y, x+w, y+h), color)
            
            # Convert to normalized YOLO format
            x_center = (x + w/2) / image_size[1]
            y_center = (y + h/2) / image_size[0]
            width = w / image_size[1]
            height = h / image_size[0]
            
            # Ensure valid coordinates
            x_center = max(0, min(1, x_center))
            y_center = max(0, min(1, y_center))
            width = max(0, min(1, width))
            height = max(0, min(1, height))
            
            annotations.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
        
        # Save only if we have successful placements
        if annotations:
            img_filename = f"synth_{i:05d}.jpg"
            cv2.imwrite(f"{PROJECT_PATH}/data/synthetic_raw/images/{img_filename}", img)
            
            ann_filename = f"synth_{i:05d}.txt"
            with open(f"{PROJECT_PATH}/data/synthetic_raw/labels/{ann_filename}", "w") as f:
                f.write("\n".join(annotations))
            
            stats['total_images'] += 1
            stats['total_objects'] += successful_placements
        
        # Progress indicator
        if (i + 1) % 200 == 0:
            print(f"   Generated {i + 1}/{num_images} images...")
    
    # Save dataset statistics
    with open(f"{PROJECT_PATH}/data/dataset_stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    
    print("✅ High-quality synthetic dataset created!")
    print(f"   📊 Total images: {stats['total_images']}")
    print(f"   🎯 Total objects: {stats['total_objects']}")
    print(f"   📈 Avg objects per image: {stats['total_objects']/stats['total_images']:.2f}")
    print(f"   🏷️ Class distribution: {stats['class_distribution']}")
    
    return classes, stats

def create_gradient_background(image_size):
    """Create gradient background for more realistic images"""
    img = np.zeros((image_size[0], image_size[1], 3), dtype=np.uint8)
    
    # Random gradient direction
    gradient_type = np.random.choice(['horizontal', 'vertical', 'diagonal'])
    
    color1 = np.random.randint(180, 256, 3)
    color2 = np.random.randint(200, 256, 3)
    
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            if gradient_type == 'horizontal':
                ratio = j / image_size[1]
            elif gradient_type == 'vertical':
                ratio = i / image_size[0]
            else:  # diagonal
                ratio = (i + j) / (image_size[0] + image_size[1])
            
            color = color1 * (1 - ratio) + color2 * ratio
            img[i, j] = color.astype(np.uint8)
    
    return img

def draw_enhanced_rectangle(img, bbox, color):
    """Draw enhanced rectangle with realistic appearance"""
    x1, y1, x2, y2 = bbox
    
    # Main shape
    cv2.rectangle(img, (x1, y1), (x2, y2), color, -1)
    
    # Add depth with gradient effect
    overlay = img.copy()
    lighter_color = tuple(min(255, c + 30) for c in color)
    cv2.rectangle(overlay, (x1, y1), (x1 + (x2-x1)//3, y1 + (y2-y1)//3), lighter_color, -1)
    
    alpha = 0.3
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
    
    # Border
    border_color = tuple(max(0, c - 60) for c in color)
    cv2.rectangle(img, (x1, y1), (x2, y2), border_color, 2)

def draw_enhanced_circle(img, bbox, color):
    """Draw enhanced circle with realistic appearance"""
    x1, y1, x2, y2 = bbox
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = min(x2 - x1, y2 - y1) // 2
    
    # Main shape
    cv2.circle(img, (center_x, center_y), radius, color, -1)
    
    # Add highlight for 3D effect
    highlight_color = tuple(min(255, c + 40) for c in color)
    highlight_center = (center_x - radius//3, center_y - radius//3)
    cv2.circle(img, highlight_center, radius//3, highlight_color, -1)
    
    # Border
    border_color = tuple(max(0, c - 60) for c in color)
    cv2.circle(img, (center_x, center_y), radius, border_color, 2)

def draw_enhanced_triangle(img, bbox, color):
    """Draw enhanced triangle with realistic appearance"""
    x1, y1, x2, y2 = bbox
    
    # Create varied triangle shapes
    triangle_type = np.random.choice(['equilateral', 'right', 'isosceles'])
    
    if triangle_type == 'equilateral':
        pts = np.array([
            [x1 + (x2-x1)//2, y1],  # Top
            [x1, y2],                # Bottom left
            [x2, y2]                 # Bottom right
        ], np.int32)
    elif triangle_type == 'right':
        pts = np.array([
            [x1, y1],    # Top left
            [x1, y2],    # Bottom left
            [x2, y2]     # Bottom right
        ], np.int32)
    else:  # isosceles
        pts = np.array([
            [x1 + (x2-x1)//2, y1],  # Top center
            [x1 + (x2-x1)//4, y2],  # Bottom left
            [x2 - (x2-x1)//4, y2]   # Bottom right
        ], np.int32)
    
    # Main shape
    cv2.fillPoly(img, [pts], color)
    
    # Border
    border_color = tuple(max(0, c - 60) for c in color)
    cv2.polylines(img, [pts], True, border_color, 2)

def calculate_box_overlap(box1, box2):
    """Calculate overlap ratio between two boxes"""
    x1_1, y1_1, x2_1, y2_1 = box1
    x1_2, y1_2, x2_2, y2_2 = box2
    
    # Calculate intersection
    x1_i = max(x1_1, x1_2)
    y1_i = max(y1_1, y1_2)
    x2_i = min(x2_1, x2_2)
    y2_i = min(y2_1, y2_2)
    
    if x2_i <= x1_i or y2_i <= y1_i:
        return 0.0
    
    intersection = (x2_i - x1_i) * (y2_i - y1_i)
    area1 = (x2_1 - x1_1) * (y2_1 - y1_1)
    area2 = (x2_2 - x1_2) * (y2_2 - y1_2)
    
    smaller_area = min(area1, area2)
    return intersection / smaller_area if smaller_area > 0 else 0.0

