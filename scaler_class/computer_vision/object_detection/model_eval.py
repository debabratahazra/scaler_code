import numpy as np

def calculate_iou(box1, box2):
    """Calculate Intersection over Union (IoU)"""
    
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

def evaluate_model(model, X_test, y_cls_test, y_bbox_test, class_names):
    """Evaluate model performance"""
    
    print("🧪 Evaluating model performance...")
    
    # Make predictions
    predictions = model.predict(X_test, verbose=0)
    pred_classes = predictions[0]
    pred_boxes = predictions[1]
    
    # Classification metrics
    pred_class_indices = np.argmax(pred_classes, axis=1)
    true_class_indices = np.argmax(y_cls_test, axis=1)
    
    classification_accuracy = np.mean(pred_class_indices == true_class_indices)
    
    # Bounding box metrics (IoU)
    ious = []
    for i in range(len(pred_boxes)):
        iou = calculate_iou(pred_boxes[i], y_bbox_test[i])
        ious.append(iou)
    
    mean_iou = np.mean(ious)
    
    # Print results
    print(f"\n📈 Evaluation Results:")
    print(f"   Classification Accuracy: {classification_accuracy:.3f}")
    print(f"   Mean IoU: {mean_iou:.3f}")
    print(f"   IoU > 0.5: {np.mean(np.array(ious) > 0.5):.3f}")
    
    # Class-wise accuracy
    print(f"\n📊 Class-wise Performance:")
    for i, class_name in enumerate(class_names):
        class_mask = true_class_indices == i
        if np.sum(class_mask) > 0:
            class_acc = np.mean(pred_class_indices[class_mask] == i)
            print(f"   {class_name}: {class_acc:.3f} ({np.sum(class_mask)} samples)")
    
    return classification_accuracy, mean_iou

