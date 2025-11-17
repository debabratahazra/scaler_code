import os
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
def compile_model(model):
    """Compile the model with appropriate loss functions and metrics"""
    
    print("⚙️ Compiling model...")
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss={
            'classification': 'categorical_crossentropy',
            'bbox_regression': 'mse'
        },
        loss_weights={
            'classification': 1.0,
            'bbox_regression': 1.0
        },
        metrics={
            'classification': ['accuracy'],
            'bbox_regression': ['mae']
        }
    )
    
    print("✅ Model compiled successfully!")
    return model

def create_callbacks(project_path):
    """Create training callbacks"""
    
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=15,
            restore_best_weights=True,
            verbose=1
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=7,
            min_lr=1e-7,
            verbose=1
        ),
        tf.keras.callbacks.ModelCheckpoint(
            f'{project_path}/models/best_model.h5',
            monitor='val_loss',
            save_best_only=True,
            save_weights_only=False,
            verbose=1
        ),
        tf.keras.callbacks.CSVLogger(
            f'{project_path}/results/training_log.csv'
        )
    ]
    
    return callbacks

def train_model(project_path, model, X_train, y_cls_train, y_bbox_train, 
                X_val, y_cls_val, y_bbox_val, epochs=50):
    """Train the object detection model"""
    
    print("🚀 Starting model training...")
    print(f"   Training samples: {len(X_train)}")
    print(f"   Validation samples: {len(X_val)}")
    print(f"   Epochs: {epochs}")
    
    # Create callbacks
    callbacks = create_callbacks(project_path)
    
    # Train model
    history = model.fit(
        X_train,
        {
            'classification': y_cls_train,
            'bbox_regression': y_bbox_train
        },
        validation_data=(
            X_val,
            {
                'classification': y_cls_val,
                'bbox_regression': y_bbox_val
            }
        ),
        epochs=epochs,
        batch_size=16,  # Smaller batch size for stability
        callbacks=callbacks,
        verbose=1
    )
    
    print("✅ Training completed!")
    return history

