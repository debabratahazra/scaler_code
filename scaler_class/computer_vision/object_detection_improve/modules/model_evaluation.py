import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
def calculate_iou_accurate(box1, box2):
    """Accurate IoU calculation"""
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
    
    # Calculate union
    area1 = (x2_1 - x1_1) * (y2_1 - y1_1)
    area2 = (x2_2 - x1_2) * (y2_2 - y1_2)
    union = area1 + area2 - intersection
    
    return intersection / union if union > 0 else 0.0

def comprehensive_evaluation(model, X_test, y_cls_test, y_bbox_test, class_names, model_name):
    """Comprehensive model evaluation with detailed metrics"""
    
    print(f"🧪 Comprehensive evaluation of {model_name}...")
    
    # Make predictions
    predictions = model.predict(X_test, verbose=0)
    pred_classes = predictions[0]
    pred_boxes = predictions[1]
    
    # Classification metrics
    pred_class_indices = np.argmax(pred_classes, axis=1)
    true_class_indices = np.argmax(y_cls_test, axis=1)
    classification_accuracy = np.mean(pred_class_indices == true_class_indices)
    
    # Detailed IoU analysis
    ious = []
    bbox_accuracies = {
        'iou_0_1': 0, 'iou_1_3': 0, 'iou_3_5': 0, 
        'iou_5_7': 0, 'iou_7_9': 0, 'iou_9_1': 0
    }
    
    for i in range(len(pred_boxes)):
        iou = calculate_iou_accurate(pred_boxes[i], y_bbox_test[i])
        ious.append(iou)
        
        # Categorize IoU
        if iou < 0.1:
            bbox_accuracies['iou_0_1'] += 1
        elif iou < 0.3:
            bbox_accuracies['iou_1_3'] += 1
        elif iou < 0.5:
            bbox_accuracies['iou_3_5'] += 1
        elif iou < 0.7:
            bbox_accuracies['iou_5_7'] += 1
        elif iou < 0.9:
            bbox_accuracies['iou_7_9'] += 1
        else:
            bbox_accuracies['iou_9_1'] += 1
    
    # Calculate comprehensive metrics
    mean_iou = np.mean(ious)
    median_iou = np.median(ious)
    std_iou = np.std(ious)
    
    good_predictions = np.sum(np.array(ious) > 0.5)
    excellent_predictions = np.sum(np.array(ious) > 0.7)
    outstanding_predictions = np.sum(np.array(ious) > 0.9)
    
    # Class-wise performance
    class_performance = {}
    for i, class_name in enumerate(class_names):
        class_mask = true_class_indices == i
        if np.sum(class_mask) > 0:
            class_acc = np.mean(pred_class_indices[class_mask] == i)
            class_ious = np.array(ious)[class_mask]
            class_performance[class_name] = {
                'accuracy': class_acc,
                'mean_iou': np.mean(class_ious),
                'samples': np.sum(class_mask)
            }
    
    # Compile results
    results = {
        'model_name': model_name,
        'classification_accuracy': classification_accuracy,
        'mean_iou': mean_iou,
        'median_iou': median_iou,
        'std_iou': std_iou,
        'good_predictions_ratio': good_predictions / len(ious),
        'excellent_predictions_ratio': excellent_predictions / len(ious),
        'outstanding_predictions_ratio': outstanding_predictions / len(ious),
        'bbox_accuracy_distribution': bbox_accuracies,
        'class_performance': class_performance,
        'total_samples': len(ious)
    }
    
    # Print detailed results
    print(f"\n📈 {model_name} Performance Results:")
    print(f"   Classification Accuracy: {classification_accuracy:.4f}")
    print(f"   Mean IoU: {mean_iou:.4f}")
    print(f"   Median IoU: {median_iou:.4f}")
    print(f"   IoU Std Dev: {std_iou:.4f}")
    print(f"   Good Predictions (IoU > 0.5): {good_predictions/len(ious):.4f} ({good_predictions}/{len(ious)})")
    print(f"   Excellent Predictions (IoU > 0.7): {excellent_predictions/len(ious):.4f} ({excellent_predictions}/{len(ious)})")
    print(f"   Outstanding Predictions (IoU > 0.9): {outstanding_predictions/len(ious):.4f} ({outstanding_predictions}/{len(ious)})")
    
    print(f"\n📊 IoU Distribution:")
    total = len(ious)
    for key, count in bbox_accuracies.items():
        percentage = count / total * 100
        range_str = key.replace('_', '.').replace('iou.', 'IoU ').replace('.', '-')
        print(f"   {range_str}: {percentage:.1f}% ({count} samples)")
    
    print(f"\n🏷️ Class-wise Performance:")
    for class_name, perf in class_performance.items():
        print(f"   {class_name}: Acc={perf['accuracy']:.3f}, IoU={perf['mean_iou']:.3f} ({perf['samples']} samples)")
    
    return results

