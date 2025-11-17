import cv2
import numpy as np
import os
import random

def create_sample_test_images(num_images=10, save_path="sample_test_images"):
    """Create sample test images for model prediction"""
    
    os.makedirs(save_path, exist_ok=True)
    
    classes = ["rectangle", "circle", "triangle"]
    colors = [
        (255, 100, 100), (100, 255, 100), (100, 100, 255),
        (255, 255, 100), (255, 100, 255), (100, 255, 255)
    ]
    
    image_info = []
    
    for i in range(num_images):
        # Create image with gradient background
        img = np.zeros((416, 416, 3), dtype=np.uint8)
        
        # Add gradient background
        for y in range(416):
            for x in range(416):
                img[y, x] = [200 + int(30 * x/416), 220 + int(20 * y/416), 210 + int(25 * (x+y)/832)]
        
        # Add 1-3 objects
        num_objects = random.randint(1, 3)
        objects_info = []
        
        for j in range(num_objects):
            class_id = random.randint(0, 2)
            color = random.choice(colors)
            
            # Random size and position
            size = random.randint(50, 120)
            x = random.randint(50, 366 - size)
            y = random.randint(50, 366 - size)
            
            if class_id == 0:  # Rectangle
                cv2.rectangle(img, (x, y), (x + size, y + size), color, -1)
                cv2.rectangle(img, (x, y), (x + size, y + size), (0, 0, 0), 3)
                shape_name = "rectangle"
                
            elif class_id == 1:  # Circle
                center = (x + size//2, y + size//2)
                radius = size // 2
                cv2.circle(img, center, radius, color, -1)
                cv2.circle(img, center, radius, (0, 0, 0), 3)
                shape_name = "circle"
                
            else:  # Triangle
                pts = np.array([
                    [x + size//2, y],
                    [x, y + size],
                    [x + size, y + size]
                ], np.int32)
                cv2.fillPoly(img, [pts], color)
                cv2.polylines(img, [pts], True, (0, 0, 0), 3)
                shape_name = "triangle"
            
            objects_info.append({
                'class': shape_name,
                'bbox': [x, y, x + size, y + size]
            })
        
        # Save image
        filename = f"test_image_{i+1:02d}.jpg"
        cv2.imwrite(os.path.join(save_path, filename), img)
        
        image_info.append({
            'filename': filename,
            'objects': objects_info
        })
        
        print(f"Created {filename} with {len(objects_info)} objects: {[obj['class'] for obj in objects_info]}")
    
    print(f"✅ Created {num_images} test images in '{save_path}' directory")
    return image_info

# Create sample test images
sample_info = create_sample_test_images(15, "sample_test_images")