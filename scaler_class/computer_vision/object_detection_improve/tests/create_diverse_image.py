import os
import numpy as np
import cv2
import random

def create_diverse_test_scenarios():
    """Create test images with different difficulty levels"""
    
    scenarios = [
        {"name": "easy", "description": "Large, centered objects"},
        {"name": "medium", "description": "Medium-sized objects with some overlap"},
        {"name": "hard", "description": "Small objects near edges"},
        {"name": "complex", "description": "Multiple objects with occlusion"}
    ]
    
    for scenario in scenarios:
        folder_name = f"test_images_{scenario['name']}"
        os.makedirs(folder_name, exist_ok=True)
        
        print(f"Creating {scenario['name']} test images...")
        
        for i in range(5):
            img = np.ones((416, 416, 3), dtype=np.uint8) * 240
            
            if scenario['name'] == 'easy':
                # Large, centered objects
                class_id = random.randint(0, 2)
                color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                size = random.randint(100, 150)
                x, y = 208 - size//2, 208 - size//2
                
                draw_shape(img, class_id, x, y, size, color)
                
            elif scenario['name'] == 'medium':
                # Medium objects
                for j in range(2):
                    class_id = random.randint(0, 2)
                    color = (random.randint(80, 200), random.randint(80, 200), random.randint(80, 200))
                    size = random.randint(60, 90)
                    x = random.randint(50, 316 - size)
                    y = random.randint(50, 316 - size)
                    
                    draw_shape(img, class_id, x, y, size, color)
                    
            elif scenario['name'] == 'hard':
                # Small objects near edges
                class_id = random.randint(0, 2)
                color = (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))
                size = random.randint(30, 50)
                
                # Place near edge
                edge = random.choice(['top', 'bottom', 'left', 'right'])
                if edge == 'top':
                    x, y = random.randint(50, 366 - size), random.randint(0, 30)
                elif edge == 'bottom':
                    # Ensure valid range: 386 <= y <= 416 - size
                    y_max = max(386, 416 - size)
                    x, y = random.randint(50, 366 - size), random.randint(386, y_max)
                elif edge == 'left':
                    x, y = random.randint(0, 30), random.randint(50, 366 - size)
                else:  # right
                    # Ensure valid range: 386 <= x <= 416 - size
                    x_max = max(386, 416 - size)
                    x, y = random.randint(386, x_max), random.randint(50, 366 - size)
                
                draw_shape(img, class_id, x, y, size, color)
                
            else:  # complex
                # Multiple overlapping objects
                for j in range(3):
                    class_id = random.randint(0, 2)
                    color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                    size = random.randint(50, 80)
                    x = random.randint(50, 336 - size)
                    y = random.randint(50, 336 - size)
                    
                    draw_shape(img, class_id, x, y, size, color)
            
            # Save image
            filename = f"{scenario['name']}_test_{i+1}.jpg"
            cv2.imwrite(os.path.join(folder_name, filename), img)
        
        print(f"✅ Created 5 {scenario['name']} test images in {folder_name}/")

def draw_shape(img, class_id, x, y, size, color):
    """Helper function to draw shapes"""
    if class_id == 0:  # Rectangle
        cv2.rectangle(img, (x, y), (x + size, y + size), color, -1)
        cv2.rectangle(img, (x, y), (x + size, y + size), (0, 0, 0), 2)
    elif class_id == 1:  # Circle
        center = (x + size//2, y + size//2)
        radius = size // 2
        cv2.circle(img, center, radius, color, -1)
        cv2.circle(img, center, radius, (0, 0, 0), 2)
    else:  # Triangle
        pts = np.array([
            [x + size//2, y],
            [x, y + size],
            [x + size, y + size]
        ], np.int32)
        cv2.fillPoly(img, [pts], color)
        cv2.polylines(img, [pts], True, (0, 0, 0), 2)

# Create diverse test scenarios
create_diverse_test_scenarios()