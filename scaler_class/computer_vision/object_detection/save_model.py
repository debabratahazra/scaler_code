import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
def save_complete_model(project_path, model, class_names):
    """Save the complete model and metadata"""
    
    print("💾 Saving complete model...")
    
    # Save model
    model.save(f'{project_path}/models/complete_object_detection_model.h5')
    
    # Save model weights separately
    model.save_weights(f'{project_path}/models/model_weights.h5')
    
    # Save class names
    import json
    model_info = {
        'class_names': class_names,
        'num_classes': len(class_names),
        'input_shape': [224, 224, 3],
        'model_type': 'object_detection_localization'
    }
    
    with open(f'{project_path}/models/model_info.json', 'w') as f:
        json.dump(model_info, f, indent=2)
    
    print("✅ Model saved successfully!")
    print(f"   📁 Model file: {project_path}/models/complete_object_detection_model.h5")
    print(f"   ⚖️ Weights file: {project_path}/models/model_weights.h5")
    print(f"   📄 Info file: {project_path}/models/model_info.json")

def load_complete_model(project_path):
    """Load the complete model and metadata"""
    
    print("📂 Loading model...")
    
    import json
    
    # Load model info
    with open(f'{project_path}/models/model_info.json', 'r') as f:
        model_info = json.load(f)
    
    # Load model
    loaded_model = tf.keras.models.load_model(f'{project_path}/models/complete_object_detection_model.h5')
    
    print("✅ Model loaded successfully!")
    return loaded_model, model_info['class_names']

