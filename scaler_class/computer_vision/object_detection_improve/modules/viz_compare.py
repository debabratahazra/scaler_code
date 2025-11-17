import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
from modules.model_evaluation import calculate_iou_accurate
from modules.data_load_augmen import load_and_preprocess_image

def create_detailed_comparison_visualization(PROJECT_PATH, baseline_model, improved_model, class_names, num_samples=12):
    """Create detailed visual comparison between baseline and improved models"""
    
    print("🖼️ Creating detailed comparison visualization...")
    
    # Get test image files
    test_image_files = os.listdir(f"{PROJECT_PATH}/data/processed/test/images")
    test_image_files = [f for f in test_image_files if f.endswith('.jpg')]
    
    if len(test_image_files) == 0:
        print("❌ No test images found!")
        return
    
    # Select diverse samples (different IoU ranges from baseline)
    sample_files = random.sample(test_image_files, min(num_samples, len(test_image_files)))
    
    # Create comprehensive comparison
    fig, axes = plt.subplots(4, 6, figsize=(24, 16))
    
    comparison_data = []
    
    for idx, img_file in enumerate(sample_files):
        if idx >= 12:  # Limit to 12 samples
            break
            
        row = idx // 3
        col = (idx % 3) * 2
        
        img_path = f"{PROJECT_PATH}/data/processed/test/images/{img_file}"
        
        # Load original image
        original_img = cv2.imread(img_path)
        original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
        
        # Make predictions with both models
        baseline_pred = predict_single_image(baseline_model, img_path, class_names, confidence_threshold=0.1)
        improved_pred = predict_single_image(improved_model, img_path, class_names, confidence_threshold=0.1)
        
        # Load ground truth
        ann_file = img_file.replace('.jpg', '.txt')
        ann_path = f"{PROJECT_PATH}/data/processed/test/labels/{ann_file}"
        
        h, w = original_img.shape[:2]
        gt_boxes = []
        gt_classes = []
        
        # Parse ground truth
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
                    
                    gt_boxes.append([x1/w, y1/h, x2/w, y2/h])  # Normalized
                    gt_classes.append(class_id)
        
        # Create baseline visualization
        baseline_img = original_img.copy()
        baseline_iou = 0.0
        
        # Draw ground truth (green)
        if gt_boxes:
            x1, y1, x2, y2 = [int(coord * dim) for coord, dim in zip(gt_boxes[0], [w, h, w, h])]
            cv2.rectangle(baseline_img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(baseline_img, f'GT: {class_names[gt_classes[0]]}', 
                       (x1, y1-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Draw baseline prediction (red)
        if baseline_pred and gt_boxes:
            x1, y1, x2, y2 = baseline_pred['bbox']
            cv2.rectangle(baseline_img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            
            pred_box_norm = [x1/w, y1/h, x2/w, y2/h]
            baseline_iou = calculate_iou_accurate(pred_box_norm, gt_boxes[0])
            
            label = f"Base: {baseline_pred['class']} ({baseline_pred['confidence']:.2f})"
            cv2.putText(baseline_img, label, (x1, y1-5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        
        # Create improved visualization
        improved_img = original_img.copy()
        improved_iou = 0.0
        
        # Draw ground truth (green)
        if gt_boxes:
            x1, y1, x2, y2 = [int(coord * dim) for coord, dim in zip(gt_boxes[0], [w, h, w, h])]
            cv2.rectangle(improved_img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(improved_img, f'GT: {class_names[gt_classes[0]]}', 
                       (x1, y1-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Draw improved prediction (blue)
        if improved_pred and gt_boxes:
            x1, y1, x2, y2 = improved_pred['bbox']
            cv2.rectangle(improved_img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            
            pred_box_norm = [x1/w, y1/h, x2/w, y2/h]
            improved_iou = calculate_iou_accurate(pred_box_norm, gt_boxes[0])
            
            label = f"Improved: {improved_pred['class']} ({improved_pred['confidence']:.2f})"
            cv2.putText(improved_img, label, (x1, y1-5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
        # Add IoU scores
        cv2.putText(baseline_img, f'IoU: {baseline_iou:.3f}', 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(improved_img, f'IoU: {improved_iou:.3f}', 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Color-code borders based on IoU improvement
        improvement = improved_iou - baseline_iou
        if improvement > 0.1:
            border_color = (0, 255, 0)  # Green for significant improvement
        elif improvement > 0:
            border_color = (255, 255, 0)  # Yellow for slight improvement
        else:
            border_color = (255, 0, 0)  # Red for no improvement
        
        cv2.rectangle(baseline_img, (0, 0), (w-1, h-1), border_color, 5)
        cv2.rectangle(improved_img, (0, 0), (w-1, h-1), border_color, 5)
        
        # Store comparison data
        comparison_data.append({
            'image': img_file,
            'baseline_iou': baseline_iou,
            'improved_iou': improved_iou,
            'improvement': improvement,
            'gt_class': class_names[gt_classes[0]] if gt_classes else 'unknown'
        })
        
        # Display images
        axes[row, col].imshow(baseline_img)
        axes[row, col].set_title(f'Baseline - IoU: {baseline_iou:.3f}', fontsize=10)
        axes[row, col].axis('off')
        
        axes[row, col+1].imshow(improved_img)
        axes[row, col+1].set_title(f'Improved - IoU: {improved_iou:.3f}', fontsize=10)
        axes[row, col+1].axis('off')
    
    plt.tight_layout()
    plt.suptitle('Model Comparison: Baseline vs Improved\n(Green: Ground Truth, Red: Baseline, Blue: Improved)', 
                 y=0.98, fontsize=16)
    plt.savefig(f'{PROJECT_PATH}/comparisons/detailed_model_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print improvement statistics
    improvements = [data['improvement'] for data in comparison_data]
    positive_improvements = [imp for imp in improvements if imp > 0]
    
    print(f"\n📊 Visual Comparison Results:")
    print(f"   Samples with IoU improvement: {len(positive_improvements)}/{len(improvements)}")
    print(f"   Average IoU improvement: {np.mean(improvements):.4f}")
    print(f"   Maximum IoU improvement: {max(improvements):.4f}")
    print(f"   Samples with >0.1 IoU improvement: {sum(1 for imp in improvements if imp > 0.1)}")
    
    return comparison_data

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

