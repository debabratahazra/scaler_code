import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def create_improved_model(num_classes, input_shape=(224, 224, 3)):
    """Create improved model with advanced architecture"""
    
    print("🔧 Creating improved model with advanced architecture...")
    
    # Try different EfficientNet versions in order of preference
    backbone = None
    backbone_name = "Unknown"
    
    try:
        # Try EfficientNetV2B0 first (most stable)
        backbone = tf.keras.applications.EfficientNetV2B0(
            weights='imagenet',
            include_top=False,
            input_shape=input_shape,
            include_preprocessing=False
        )
        backbone_name = "EfficientNetV2B0"
        print(f"✅ Using {backbone_name}")
        
    except Exception as e:
        print(f"⚠️ EfficientNetV2B0 failed: {e}")
        try:
            # Try EfficientNetB1 (sometimes more stable than B0)
            backbone = tf.keras.applications.EfficientNetB1(
                weights='imagenet',
                include_top=False,
                input_shape=input_shape
            )
            backbone_name = "EfficientNetB1"
            print(f"✅ Using {backbone_name}")
            
        except Exception as e:
            print(f"⚠️ EfficientNetB1 failed: {e}")
            # Fallback to ResNet50
            backbone = tf.keras.applications.ResNet50(
                weights='imagenet',
                include_top=False,
                input_shape=input_shape
            )
            backbone_name = "ResNet50 (fallback)"
            print(f"✅ Using {backbone_name}")
    
    # Initially freeze backbone
    backbone.trainable = False
    
    inputs = keras.Input(shape=input_shape, name='input_image')
    
    # Extract features at multiple scales
    x = backbone(inputs, training=False)
    
    # Multi-scale feature processing
    # Global features
    global_avg = layers.GlobalAveragePooling2D(name='global_avg_pool')(x)
    global_max = layers.GlobalMaxPooling2D(name='global_max_pool')(x)
    
    # Combine multi-scale features
    combined_features = layers.Concatenate(name='feature_concat')([global_avg, global_max])
    combined_features = layers.BatchNormalization(name='feature_bn')(combined_features)
    combined_features = layers.Dropout(0.3, name='feature_dropout')(combined_features)
    
    # Advanced shared processing
    shared_1 = layers.Dense(512, activation='relu', name='shared_dense1')(combined_features)
    shared_1 = layers.BatchNormalization(name='shared_bn1')(shared_1)
    shared_1 = layers.Dropout(0.3, name='shared_dropout1')(shared_1)
    
    shared_2 = layers.Dense(256, activation='relu', name='shared_dense2')(shared_1)
    shared_2 = layers.BatchNormalization(name='shared_bn2')(shared_2)
    shared_2 = layers.Dropout(0.3, name='shared_dropout2')(shared_2)
    
    # Specialized classification head
    cls_head = layers.Dense(128, activation='relu', name='cls_dense1')(shared_2)
    cls_head = layers.BatchNormalization(name='cls_bn1')(cls_head)
    cls_head = layers.Dropout(0.2, name='cls_dropout1')(cls_head)
    
    cls_head = layers.Dense(64, activation='relu', name='cls_dense2')(cls_head)
    cls_head = layers.BatchNormalization(name='cls_bn2')(cls_head)
    
    classification_output = layers.Dense(
        num_classes, 
        activation='softmax', 
        name='classification'
    )(cls_head)
    
    # Specialized bounding box regression head
    bbox_head = layers.Dense(256, activation='relu', name='bbox_dense1')(shared_2)
    bbox_head = layers.BatchNormalization(name='bbox_bn1')(bbox_head)
    bbox_head = layers.Dropout(0.2, name='bbox_dropout1')(bbox_head)
    
    bbox_head = layers.Dense(128, activation='relu', name='bbox_dense2')(bbox_head)
    bbox_head = layers.BatchNormalization(name='bbox_bn2')(bbox_head)
    bbox_head = layers.Dropout(0.2, name='bbox_dropout2')(bbox_head)
    
    bbox_head = layers.Dense(64, activation='relu', name='bbox_dense3')(bbox_head)
    bbox_head = layers.BatchNormalization(name='bbox_bn3')(bbox_head)
    
    # Bounding box output with better activation
    bbox_output = layers.Dense(4, activation='sigmoid', name='bbox_regression')(bbox_head)
    
    model = keras.Model(inputs, [classification_output, bbox_output], name='ImprovedObjectDetectionModel')
    
    print("✅ Improved model architecture created!")
    return model

