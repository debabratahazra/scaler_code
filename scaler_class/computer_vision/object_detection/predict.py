import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from load_data import load_and_preprocess_image
def predict_single_image(model, image_path, class_names, confidence_threshold=0.5):
    """Predict objects in a single image"""
    
    # Load and preprocess image
    image, original_shape = load_and_preprocess_image(image_path)
    if image is None:
        return None
    
    # Make prediction
    image_batch = np.expand_dims(image, axis=0)
    predictions = model.predict(image_batch, verbose=0)
    
    class_probs = predictions[0][0]
    bbox_coords = predictions[1][0]
    
    # Get predicted class
    predicted_class_idx = np.argmax(class_probs)
    confidence = class_probs[predicted_class_idx]
    
    if confidence > confidence_threshold:
        predicted_class = class_names[predicted_class_idx]
        
        # Convert normalized coordinates to pixel coordinates
        h, w = original_shape
        x1 = max(0, min(w, int(bbox_coords[0] * w)))
        y1 = max(0, min(h, int(bbox_coords[1] * h)))
        x2 = max(0, min(w, int(bbox_coords[2] * w)))
        y2 = max(0, min(h, int(bbox_coords[3] * h)))
        
        return {
            'class': predicted_class,
            'confidence': confidence,
            'bbox': [x1, y1, x2, y2],
            'class_probs': class_probs
        }
    
    return None

def visualize_predictions(project_path, class_names, model, num_samples=6):
    """Visualize model predictions on validation samples"""
    
    print("🖼️ Visualizing model predictions...")
    
    # Get validation image files
    val_image_files = os.listdir(f"{project_path}/dataset/val/images")
    val_image_files = [f for f in val_image_files if f.endswith('.jpg')]
    
    if len(val_image_files) == 0:
        print("❌ No validation images found!")
        return
    
    # Select random samples
    sample_files = random.sample(val_image_files, min(num_samples, len(val_image_files)))
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()
    
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # RGB colors for classes
    
    for idx, img_file in enumerate(sample_files):
        img_path = f"{project_path}/dataset/val/images/{img_file}"
        
        # Load original image
        original_img = cv2.imread(img_path)
        original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
        
        # Make prediction
        prediction = predict_single_image(model, img_path, class_names, confidence_threshold=0.3)
        
        # Load ground truth
        ann_file = img_file.replace('.jpg', '.txt')
        ann_path = f"{project_path}/dataset/val/labels/{ann_file}"
        
        h, w = original_img.shape[:2]
        
        # Draw ground truth (green)
        if os.path.exists(ann_path):
            with open(ann_path, 'r') as f:
                lines = f.readlines()
            
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    class_id = int(parts[0])
                    x_center = float(parts[1]) * w
                    y_center = float(parts[2]) * h
                    width = float(parts[3]) * w
                    height = float(parts[4]) * h
                    
                    x1 = int(x_center - width/2)
                    y1 = int(y_center - height/2)
                    x2 = int(x_center + width/2)
                    y2 = int(y_center + height/2)
                    
                    # Draw ground truth box (green)
                    cv2.rectangle(original_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(original_img, f'GT: {class_names[class_id]}', 
                               (x1, y1-25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Draw prediction (red)
        if prediction:
            x1, y1, x2, y2 = prediction['bbox']
            cv2.rectangle(original_img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            label = f"Pred: {prediction['class']} ({prediction['confidence']:.2f})"
            cv2.putText(original_img, label, (x1, y1-5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        
        axes[idx].imshow(original_img)
        axes[idx].set_title(f'Sample {idx+1}')
        axes[idx].axis('off')
    
    plt.tight_layout()
    plt.suptitle('Model Predictions vs Ground Truth\n(Red: Prediction, Green: Ground Truth)', 
                 y=1.02, fontsize=16)
    plt.savefig(f'{project_path}/results/predictions_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Prediction visualization saved!")
