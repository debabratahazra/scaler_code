import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from predict import predict_single_image
def run_complete_test(project_path, class_names, model, X_train, X_val):
    """Run complete test of the object detection pipeline"""
    
    print("🧪 Running complete pipeline test...")
    
    # Test on a few validation images
    val_image_files = os.listdir(f"{project_path}/dataset/val/images")
    val_image_files = [f for f in val_image_files if f.endswith('.jpg')]
    
    if len(val_image_files) == 0:
        print("❌ No validation images found for testing!")
        return
    
    print(f"\n🎯 Testing on {min(3, len(val_image_files))} validation images:")
    
    for i, img_file in enumerate(val_image_files[:3]):
        print(f"\n--- Test Image {i+1}: {img_file} ---")
        
        img_path = f"{project_path}/dataset/val/images/{img_file}"
        
        # Make prediction
        prediction = predict_single_image(model, img_path, class_names, confidence_threshold=0.1)
        
        if prediction:
            print(f"✅ Detection successful!")
            print(f"   Class: {prediction['class']}")
            print(f"   Confidence: {prediction['confidence']:.3f}")
            print(f"   Bounding Box: {prediction['bbox']}")
            print(f"   All class probabilities:")
            for j, prob in enumerate(prediction['class_probs']):
                print(f"      {class_names[j]}: {prob:.3f}")
        else:
            print("❌ No detection (confidence too low)")
    
    print(f"\n📊 Final Summary:")
    print(f"   ✅ Project created: {project_path}")
    print(f"   ✅ Synthetic dataset: {len(X_train) + len(X_val)} images")
    print(f"   ✅ Model trained: {len(class_names)} classes")
    print(f"   ✅ Classes: {class_names}")
    print(f"   ✅ Model saved: complete_object_detection_model.h5")

# Run complete test
run_complete_test(project_path, class_names, model, X_train, X_val)