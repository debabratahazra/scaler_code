# Use Synthetic Data to Train a Object Detection Model

import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from generate_syn_dataset import create_synthetic_dataset
from visualize import visualize_synthetic_samples
from split_train_test import split_dataset
from load_data import create_dataset_from_directory
from build_model import create_object_detection_model
from compile_train_model import compile_model, train_model
from viz_train_result import plot_training_history
from model_eval import evaluate_model
from predict import visualize_predictions
from save_model import save_complete_model

# Create project directory structure
def create_project_structure():
    """Create the complete project directory structure"""
    directories = [
        "object_detection_project",
        "object_detection_project/synthetic_dataset",
        "object_detection_project/synthetic_dataset/images",
        "object_detection_project/synthetic_dataset/labels",
        "object_detection_project/dataset",
        "object_detection_project/dataset/train",
        "object_detection_project/dataset/train/images",
        "object_detection_project/dataset/train/labels",
        "object_detection_project/dataset/val",
        "object_detection_project/dataset/val/images",
        "object_detection_project/dataset/val/labels",
        "object_detection_project/models",
        "object_detection_project/results"
    ]
    
    for directory in directories:
        # Check if directory exists, if not create it
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    print("✅ Project structure created successfully!")
    return "object_detection_project"

# Run this first
project_path = create_project_structure()

# Generate the synthetic dataset
# Check if files are already present inside the directory {project_path}/synthetic_dataset/images and {project_path}/synthetic_dataset/labels
    # Define classes
class_names = ["rectangle", "circle", "triangle"]
if not os.path.exists(f"{project_path}/synthetic_dataset/images") or not os.path.exists(f"{project_path}/synthetic_dataset/labels"):
    create_synthetic_dataset(project_path, class_names, 500)
else:
    print("Synthetic dataset already exists")

# Visualize samples
visualize_synthetic_samples(project_path)

# Split the dataset
train_count, val_count = split_dataset(project_path)

# Load the datasets
print("📚 Loading training dataset...")
X_train, y_bbox_train, y_cls_train = create_dataset_from_directory(
    f"{project_path}/dataset/train/images",
    f"{project_path}/dataset/train/labels",
    len(class_names)
)

print("🧪 Loading validation dataset...")
X_val, y_bbox_val, y_cls_val = create_dataset_from_directory(
    f"{project_path}/dataset/val/images",
    f"{project_path}/dataset/val/labels",
    len(class_names)
)

print(f"\n📊 Dataset Summary:")
print(f"   Training samples: {len(X_train)}")
print(f"   Validation samples: {len(X_val)}")
print(f"   Image shape: {X_train[0].shape if len(X_train) > 0 else 'No data'}")
print(f"   Number of classes: {len(class_names)}")
print(f"   Classes: {class_names}")

# Create the model
model = create_object_detection_model(len(class_names))

# Display model summary
print("\n🏗️ Model Architecture:")
model.summary()

# Save model architecture plot
tf.keras.utils.plot_model(
    model, 
    to_file=f'{project_path}/results/model_architecture.png',
    show_shapes=True,
    show_layer_names=True,
    rankdir='TB',
    dpi=150
)

# Compile and train the model
model = compile_model(model)

# Check if we have data before training
if len(X_train) > 0 and len(X_val) > 0:
    print(f"\n🎯 Training Configuration:")
    print(f"   Classes: {class_names}")
    print(f"   Input shape: {X_train.shape[1:]}")
    print(f"   Training samples: {len(X_train)}")
    print(f"   Validation samples: {len(X_val)}")
    
    # Start training
    history = train_model(project_path,
        model, X_train, y_cls_train, y_bbox_train,
        X_val, y_cls_val, y_bbox_val, 
        epochs=30  # Reduced epochs for initial testing
    )
else:
    print("❌ No training data available. Please check dataset creation.")
    

# Plot training history if training was completed
if 'history' in locals():
    plot_training_history(project_path, history)
    
# Evaluate on validation set
if len(X_val) > 0:
    val_accuracy, val_iou = evaluate_model(model, X_val, y_cls_val, y_bbox_val, class_names)
    

# Visualize predictions
visualize_predictions(project_path, class_names, model)

# Save the trained model
save_complete_model(project_path, model, class_names)