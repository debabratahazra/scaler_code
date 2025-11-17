import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
def create_object_detection_model(num_classes, input_shape=(224, 224, 3)):
    """Create object detection and localization model using pre-trained backbone"""
    
    print("🔧 Building object detection model...")
    
    # Load pre-trained backbone (MobileNetV2 for faster training)
    backbone = tf.keras.applications.MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=input_shape,
        alpha=1.0  # Width multiplier
    )
    
    # Freeze backbone layers initially
    backbone.trainable = False
    
    # Input layer
    inputs = keras.Input(shape=input_shape, name='input_image')
    
    # Feature extraction
    x = backbone(inputs, training=False)
    x = layers.GlobalAveragePooling2D(name='global_avg_pool')(x)
    x = layers.Dropout(0.2, name='dropout_main')(x)
    
    # Shared dense layer
    shared_dense = layers.Dense(512, activation='relu', name='shared_dense')(x)
    shared_dense = layers.Dropout(0.2, name='dropout_shared')(shared_dense)
    
    # Classification head
    classification_head = layers.Dense(256, activation='relu', name='cls_dense1')(shared_dense)
    classification_head = layers.Dropout(0.2, name='dropout_cls')(classification_head)
    classification_output = layers.Dense(
        num_classes, 
        activation='softmax', 
        name='classification'
    )(classification_head)
    
    # Bounding box regression head
    bbox_head = layers.Dense(256, activation='relu', name='bbox_dense1')(shared_dense)
    bbox_head = layers.Dropout(0.2, name='dropout_bbox')(bbox_head)
    bbox_head = layers.Dense(128, activation='relu', name='bbox_dense2')(bbox_head)
    bbox_output = layers.Dense(4, activation='sigmoid', name='bbox_regression')(bbox_head)
    
    # Create model
    model = keras.Model(inputs, [classification_output, bbox_output], name='ObjectDetectionModel')
    
    print("✅ Model created successfully!")
    return model

