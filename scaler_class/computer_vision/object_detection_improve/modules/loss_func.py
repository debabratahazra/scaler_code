import tensorflow as tf
import tensorflow.keras.backend as K

def smooth_l1_loss(y_true, y_pred, delta=1.0):
    """Smooth L1 loss - less sensitive to outliers than MSE"""
    diff = tf.abs(y_true - y_pred)
    less_than_delta = tf.cast(tf.less(diff, delta), tf.float32)
    loss = (less_than_delta * 0.5 * diff**2) + (1 - less_than_delta) * (delta * diff - 0.5 * delta**2)
    return tf.reduce_mean(loss)

def iou_loss(y_true, y_pred):
    """IoU loss for better bounding box overlap"""
    # Ensure tensors are float32
    y_true = tf.cast(y_true, tf.float32)
    y_pred = tf.cast(y_pred, tf.float32)
    
    # Extract coordinates
    x1_true, y1_true, x2_true, y2_true = tf.split(y_true, 4, axis=1)
    x1_pred, y1_pred, x2_pred, y2_pred = tf.split(y_pred, 4, axis=1)
    
    # Calculate intersection
    x1_i = tf.maximum(x1_true, x1_pred)
    y1_i = tf.maximum(y1_true, y1_pred)
    x2_i = tf.minimum(x2_true, x2_pred)
    y2_i = tf.minimum(y2_true, y2_pred)
    
    # Calculate intersection area
    intersection_area = tf.maximum(0.0, x2_i - x1_i) * tf.maximum(0.0, y2_i - y1_i)
    
    # Calculate union area
    area_true = (x2_true - x1_true) * (y2_true - y1_true)
    area_pred = (x2_pred - x1_pred) * (y2_pred - y1_pred)
    union_area = area_true + area_pred - intersection_area
    
    # Calculate IoU
    iou = intersection_area / (union_area + 1e-7)
    
    # Return 1 - IoU as loss
    return tf.reduce_mean(1.0 - iou)

def giou_loss(y_true, y_pred):
    """Generalized IoU loss for even better bounding box regression"""
    y_true = tf.cast(y_true, tf.float32)
    y_pred = tf.cast(y_pred, tf.float32)
    
    # Extract coordinates
    x1_true, y1_true, x2_true, y2_true = tf.split(y_true, 4, axis=1)
    x1_pred, y1_pred, x2_pred, y2_pred = tf.split(y_pred, 4, axis=1)
    
    # Calculate intersection
    x1_i = tf.maximum(x1_true, x1_pred)
    y1_i = tf.maximum(y1_true, y1_pred)
    x2_i = tf.minimum(x2_true, x2_pred)
    y2_i = tf.minimum(y2_true, y2_pred)
    
    intersection_area = tf.maximum(0.0, x2_i - x1_i) * tf.maximum(0.0, y2_i - y1_i)
    
    # Calculate union
    area_true = (x2_true - x1_true) * (y2_true - y1_true)
    area_pred = (x2_pred - x1_pred) * (y2_pred - y1_pred)
    union_area = area_true + area_pred - intersection_area
    
    # Calculate IoU
    iou = intersection_area / (union_area + 1e-7)
    
    # Calculate enclosing box
    x1_c = tf.minimum(x1_true, x1_pred)
    y1_c = tf.minimum(y1_true, y1_pred)
    x2_c = tf.maximum(x2_true, x2_pred)
    y2_c = tf.maximum(y2_true, y2_pred)
    
    enclosing_area = (x2_c - x1_c) * (y2_c - y1_c)
    
    # Calculate GIoU
    giou = iou - (enclosing_area - union_area) / (enclosing_area + 1e-7)
    
    return tf.reduce_mean(1.0 - giou)

def combined_bbox_loss(y_true, y_pred, alpha=0.5, beta=0.3, gamma=0.2):
    """Combined bounding box loss: Smooth L1 + IoU + GIoU"""
    l1_loss = smooth_l1_loss(y_true, y_pred)
    iou_loss_val = iou_loss(y_true, y_pred)
    giou_loss_val = giou_loss(y_true, y_pred)
    
    return alpha * l1_loss + beta * iou_loss_val + gamma * giou_loss_val

def focal_loss(y_true, y_pred, alpha=0.25, gamma=2.0):
    """Focal loss for handling class imbalance"""
    epsilon = tf.keras.backend.epsilon()
    y_pred = tf.clip_by_value(y_pred, epsilon, 1.0 - epsilon)
    
    # Calculate cross entropy
    ce = -y_true * tf.math.log(y_pred)
    
    # Calculate focal weight
    alpha_t = y_true * alpha + (1 - y_true) * (1 - alpha)
    p_t = y_true * y_pred + (1 - y_true) * (1 - y_pred)
    focal_weight = alpha_t * tf.pow((1 - p_t), gamma)
    
    # Calculate focal loss
    fl = focal_weight * ce
    return tf.reduce_mean(tf.reduce_sum(fl, axis=1))

