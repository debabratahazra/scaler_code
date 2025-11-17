import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
def plot_training_history(project_path, history):
    """Plot training history"""
    
    print("📊 Plotting training history...")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Classification accuracy
    if 'classification_accuracy' in history.history:
        axes[0, 0].plot(history.history['classification_accuracy'], label='Train')
        axes[0, 0].plot(history.history['val_classification_accuracy'], label='Validation')
        axes[0, 0].set_title('Classification Accuracy')
        axes[0, 0].set_xlabel('Epoch')
        axes[0, 0].set_ylabel('Accuracy')
        axes[0, 0].legend()
        axes[0, 0].grid(True)
    
    # Classification loss
    if 'classification_loss' in history.history:
        axes[0, 1].plot(history.history['classification_loss'], label='Train')
        axes[0, 1].plot(history.history['val_classification_loss'], label='Validation')
        axes[0, 1].set_title('Classification Loss')
        axes[0, 1].set_xlabel('Epoch')
        axes[0, 1].set_ylabel('Loss')
        axes[0, 1].legend()
        axes[0, 1].grid(True)
    
    # Bounding box loss
    if 'bbox_regression_loss' in history.history:
        axes[1, 0].plot(history.history['bbox_regression_loss'], label='Train')
        axes[1, 0].plot(history.history['val_bbox_regression_loss'], label='Validation')
        axes[1, 0].set_title('Bounding Box Loss')
        axes[1, 0].set_xlabel('Epoch')
        axes[1, 0].set_ylabel('Loss')
        axes[1, 0].legend()
        axes[1, 0].grid(True)
    
    # Total loss
    axes[1, 1].plot(history.history['loss'], label='Train')
    axes[1, 1].plot(history.history['val_loss'], label='Validation')
    axes[1, 1].set_title('Total Loss')
    axes[1, 1].set_xlabel('Epoch')
    axes[1, 1].set_ylabel('Loss')
    axes[1, 1].legend()
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.savefig(f'{project_path}/results/training_history.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Training history plots saved!")

