import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from modules.loss_func import focal_loss, combined_bbox_loss

class IoUMetric(tf.keras.metrics.Metric):
    """Custom IoU metric for monitoring during training"""
    
    def __init__(self, name='iou_metric', **kwargs):
        super().__init__(name=name, **kwargs)
        self.iou_sum = self.add_weight(name='iou_sum', initializer='zeros')
        self.count = self.add_weight(name='count', initializer='zeros')
    
    def update_state(self, y_true, y_pred, sample_weight=None):
        # Calculate IoU for batch
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
        
        self.iou_sum.assign_add(tf.reduce_sum(iou))
        self.count.assign_add(tf.cast(tf.shape(y_true)[0], tf.float32))
    
    def result(self):
        return self.iou_sum / self.count
    
    def reset_state(self):
        self.iou_sum.assign(0.)
        self.count.assign(0.)

def create_advanced_callbacks(PROJECT_PATH, model_name):
    """Create advanced callbacks for better training"""
    
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_bbox_regression_loss',
            patience=25,
            restore_best_weights=True,
            verbose=1,
            mode='min'
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_bbox_regression_loss',
            factor=0.5,
            patience=10,
            min_lr=1e-7,
            verbose=1,
            mode='min'
        ),
        tf.keras.callbacks.ModelCheckpoint(
            f'{PROJECT_PATH}/models/improved/best_{model_name}.h5',
            monitor='val_bbox_regression_loss',
            save_best_only=True,
            save_weights_only=False,
            verbose=1,
            mode='min'
        ),
        tf.keras.callbacks.CSVLogger(
            f'{PROJECT_PATH}/logs/{model_name}_training.csv'
        ),
        tf.keras.callbacks.TensorBoard(
            log_dir=f'{PROJECT_PATH}/logs/tensorboard/{model_name}',
            histogram_freq=1,
            write_graph=True
        )
    ]
    
    return callbacks

def compile_improved_model(model, stage='initial'):
    """Compile model with advanced loss functions"""
    
    if stage == 'initial':
        learning_rate = 0.001
        bbox_weight = 10.0
    else:  # fine-tuning
        learning_rate = 0.0001
        bbox_weight = 15.0
    
    # Use AdamW optimizer with weight decay
    optimizer = tf.keras.optimizers.AdamW(
        learning_rate=learning_rate,
        weight_decay=0.01,
        beta_1=0.9,
        beta_2=0.999
    )
    
    model.compile(
        optimizer=optimizer,
        loss={
            'classification': focal_loss,
            'bbox_regression': combined_bbox_loss
        },
        loss_weights={
            'classification': 1.0,
            'bbox_regression': bbox_weight
        },
        metrics={
            'classification': ['accuracy'],
            'bbox_regression': [IoUMetric(), 'mae']
        }
    )
    
    return model

def train_improved_model_multistage(PROJECT_PATH, model, X_train, y_cls_train, y_bbox_train, 
                                   X_val, y_cls_val, y_bbox_val):
    """Multi-stage training for optimal performance"""
    
    print("🚀 Starting multi-stage improved training...")
    
    # Stage 1: Train heads with frozen backbone
    print("\n📚 Stage 1: Training detection heads (frozen backbone)...")
    
    # Freeze backbone
    model.layers[1].trainable = False
    model = compile_improved_model(model, stage='initial')
    
    callbacks_stage1 = create_advanced_callbacks(PROJECT_PATH,'stage1')
    
    history_stage1 = model.fit(
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
        epochs=60,
        batch_size=16,
        callbacks=callbacks_stage1,
        verbose=1
    )
    
    # Stage 2: Fine-tune with unfrozen backbone
    print("\n🔥 Stage 2: Fine-tuning with unfrozen backbone...")
    
    # Unfreeze backbone
    model.layers[1].trainable = True
    model = compile_improved_model(model, stage='finetune')
    
    callbacks_stage2 = create_advanced_callbacks(PROJECT_PATH, 'stage2')
    
    history_stage2 = model.fit(
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
        epochs=60,
        batch_size=8,  # Smaller batch for fine-tuning
        callbacks=callbacks_stage2,
        verbose=1
    )
    
    # Combine histories
    combined_history = {}
    for key in history_stage1.history.keys():
        combined_history[key] = history_stage1.history[key] + history_stage2.history[key]
    
    class CombinedHistory:
        def __init__(self, history_dict):
            self.history = history_dict
    
    return CombinedHistory(combined_history)

