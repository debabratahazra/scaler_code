import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def create_baseline_model(num_classes, input_shape=(224, 224, 3)):
    """Create baseline model (similar to original approach)"""
    
    print("🏗️ Creating baseline model...")
    
    backbone = tf.keras.applications.MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=input_shape
    )
    backbone.trainable = False
    
    inputs = keras.Input(shape=input_shape)
    x = backbone(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.2)(x)
    
    # Simple classification head
    cls_output = layers.Dense(num_classes, activation='softmax', name='classification')(x)
    
    # Simple bbox head
    bbox_output = layers.Dense(4, activation='sigmoid', name='bbox_regression')(x)
    
    model = keras.Model(inputs, [cls_output, bbox_output], name='BaselineModel')
    
    # Compile with basic loss functions
    model.compile(
        optimizer='adam',
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
    
    print("✅ Baseline model created!")
    return model

