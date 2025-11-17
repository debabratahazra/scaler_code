# Chat link: https://gpt4ifx-ui.icp.infineon.com/s/fbf0e493-d340-48b2-952e-6760bb157b32

import warnings
# Suppress Protobuf version warning
warnings.filterwarnings('ignore', message='.*Protobuf gencode version.*')

# Import all required libraries
import tensorflow as tf
import json
import numpy as np

from modules.folder_structure import create_improved_project_structure
from modules.generate_synthetic_data import create_high_quality_synthetic_dataset
from modules.split_data import smart_dataset_split
from modules.data_load_augmen import AdvancedDataGenerator
from modules.baseline_model import create_baseline_model
from modules.improve_model import create_improved_model
from modules.advance_train_model import train_improved_model_multistage
from modules.model_evaluation import comprehensive_evaluation
from modules.viz_compare import create_detailed_comparison_visualization
from modules.performance_metrics import create_performance_comparison_charts
from modules.model_test_validation import final_model_validation, generate_final_report
from prediction import predict_image

def convert_to_serializable(obj):
    """Convert NumPy types to Python native types for JSON serialization"""
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {key: convert_to_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    else:
        return obj

# Check TensorFlow version and GPU availability

print("TensorFlow version:", tf.__version__)
print("GPU Available:", tf.config.list_physical_devices('GPU'))

# Create project structure
PROJECT_PATH = create_improved_project_structure()
print(f"Working in: {PROJECT_PATH}")

# Generate the enhanced synthetic dataset
classes = ["rectangle", "circle", "triangle"]
print("🚀 Step 2: Creating Enhanced Synthetic Dataset")
class_names, dataset_stats = create_high_quality_synthetic_dataset(PROJECT_PATH, classes, 2000)

# Perform smart dataset split
print("🚀 Step 3: Smart Dataset Splitting")
split_info = smart_dataset_split(PROJECT_PATH)

# Create data generators
print("🚀 Step 4: Creating Advanced Data Loaders")

train_generator = AdvancedDataGenerator(
    f"{PROJECT_PATH}/data/processed/train/images",
    f"{PROJECT_PATH}/data/processed/train/labels",
    len(class_names),
    batch_size=16,
    augment=True
)

val_generator = AdvancedDataGenerator(
    f"{PROJECT_PATH}/data/processed/val/images",
    f"{PROJECT_PATH}/data/processed/val/labels",
    len(class_names),
    batch_size=16,
    augment=False
)

# Load validation data for evaluation
X_val, y_bbox_val, y_cls_val = val_generator.get_all_data()
X_train, y_bbox_train, y_cls_train = train_generator.get_all_data()

print(f"✅ Data loading completed!")
print(f"   📚 Training samples: {len(X_train)}")
print(f"   🧪 Validation samples: {len(X_val)}")

print("✅ Step 5: Advanced loss functions defined!")

# Create and train baseline model
print("🚀 Step 6: Creating and Training Baseline Model")
baseline_model = create_baseline_model(len(class_names))

print("📊 Baseline Model Architecture:")
baseline_model.summary()

# Train baseline model (quick training for comparison)
print("🏃 Training baseline model...")
baseline_history = baseline_model.fit(
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
    epochs=20,
    batch_size=16,
    verbose=1
)

# Save baseline model
baseline_model.save(f'{PROJECT_PATH}/models/baseline/baseline_model.h5')
print("✅ Baseline model trained and saved!")

# Create improved model
print("🚀 Step 7: Creating Improved Model")
improved_model = create_improved_model(len(class_names))

print("📊 Improved Model Architecture:")
improved_model.summary()

# Plot model architecture
tf.keras.utils.plot_model(
    improved_model, 
    to_file=f'{PROJECT_PATH}/results/improved/model_architecture.png',
    show_shapes=True,
    show_layer_names=True,
    rankdir='TB',
    dpi=150
)

# Train improved model
print("🚀 Step 8: Training Improved Model with Multi-Stage Strategy")
improved_history = train_improved_model_multistage(PROJECT_PATH,
    improved_model, X_train, y_cls_train, y_bbox_train,
    X_val, y_cls_val, y_bbox_val
)

# Save improved model
improved_model.save(f'{PROJECT_PATH}/models/improved/improved_model.h5')
print("✅ Improved model trained and saved!")

# Load test data
test_generator = AdvancedDataGenerator(
    f"{PROJECT_PATH}/data/processed/test/images",
    f"{PROJECT_PATH}/data/processed/test/labels",
    len(class_names),
    batch_size=16,
    augment=False
)

X_test, y_bbox_test, y_cls_test = test_generator.get_all_data()

print(f"🚀 Step 9: Comprehensive Evaluation")
print(f"   Test samples: {len(X_test)}")

# Evaluate both models
baseline_results = comprehensive_evaluation(
    baseline_model, X_test, y_cls_test, y_bbox_test, class_names, "Baseline Model"
)

improved_results = comprehensive_evaluation(
    improved_model, X_test, y_cls_test, y_bbox_test, class_names, "Improved Model"
)

# Save results
with open(f"{PROJECT_PATH}/results/evaluation_results.json", "w") as f:
    results_dict = {
        'baseline': baseline_results,
        'improved': improved_results,
        'comparison': {
            'iou_improvement': improved_results['mean_iou'] - baseline_results['mean_iou'],
            'accuracy_improvement': improved_results['classification_accuracy'] - baseline_results['classification_accuracy'],
            'excellent_predictions_improvement': improved_results['excellent_predictions_ratio'] - baseline_results['excellent_predictions_ratio']
        }
    }
    json.dump(convert_to_serializable(results_dict), f, indent=2)

print("✅ Evaluation results saved!")

# Create visual comparison
print("🚀 Step 10: Creating Visual Comparison")
comparison_data = create_detailed_comparison_visualization(PROJECT_PATH, baseline_model, improved_model, class_names)

# Create performance charts
print("🚀 Step 11: Creating Performance Comparison Charts")
create_performance_comparison_charts(PROJECT_PATH, baseline_history, improved_history)

# Perform final validation and generate report
print("🚀 Step 12: Final Model Validation and Report Generation")
challenging_test_results = final_model_validation(PROJECT_PATH, X_test, y_bbox_test, y_cls_test, class_names, improved_model)
final_report = generate_final_report(PROJECT_PATH, class_names)



# # Load the improved model
# model = tf.keras.models.load_model('{PROJECT_PATH}/models/improved/improved_model.h5')

# # Example usage
# prediction = predict_image(model, 'your_image.jpg', class_names)
# print(f"Detected: {{prediction['class']}} ({{prediction['confidence']:.3f}})")
# print(f"Bounding box: {{prediction['bbox']}}")