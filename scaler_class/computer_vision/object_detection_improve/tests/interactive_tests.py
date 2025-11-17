import os
import sys
import random
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.folder_structure import project_name
from tests.create_test_image import create_sample_test_images
from modules.viz_compare import predict_single_image
from modules.advance_train_model import compile_improved_model, IoUMetric
from modules.loss_func import focal_loss, combined_bbox_loss

PROJECT_PATH = f"{project_name}"

# Alias for compatibility
predict_single_image_complete = predict_single_image

def load_and_compile_model(model_path):
    """Load model and recompile with metrics to make them available"""
    # Load the model
    model = tf.keras.models.load_model(
        model_path,
        custom_objects={
            'focal_loss': focal_loss,
            'combined_bbox_loss': combined_bbox_loss,
            'IoUMetric': IoUMetric
        }
    )
    
    # Recompile with the same configuration to build metrics
    model = compile_improved_model(model, stage='initial')
    
    print("✅ Model loaded and compiled with metrics!")
    return model

def visualize_single_prediction(image_path, prediction):
    """Visualize prediction on image"""
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    x1, y1, x2, y2 = prediction['bbox']
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(img, f"{prediction['class']} ({prediction['confidence']:.2f})", 
                (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.title(f"Prediction: {prediction['class']} ({prediction['confidence']:.3f})")
    plt.axis('off')
    plt.show()

def test_model_with_samples(model_path, class_names, folder_path):
    """Test model with multiple sample images"""
    model = tf.keras.models.load_model(model_path)
    test_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    results = []
    
    for img_file in test_files:
        img_path = os.path.join(folder_path, img_file)
        prediction = predict_single_image_complete(model, img_path, class_names)
        results.append({
            'image': img_file,
            'prediction': prediction
        })
    
    return results

def interactive_model_test():
    """Interactive function to test model with different scenarios"""
    
    print("🎮 Interactive Model Testing")
    print("=" * 50)
    
    # Load model
    try:
        model_path = input("Enter model path (or press Enter for default): ").strip()
        if not model_path:
            model_path = f"{PROJECT_PATH}/models/improved/improved_model.h5"
        
        # Load and compile model with metrics
        model = load_and_compile_model(model_path)
        
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return
    
    class_names = ["rectangle", "circle", "triangle"]
    
    while True:
        print("\n🔧 Choose test option:")
        print("1. Test with generated sample images")
        print("2. Test with specific image path")
        print("3. Generate new sample images")
        print("4. Batch test multiple images")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == "1":
            # Test with existing samples
            if not os.path.exists("sample_test_images"):
                create_sample_test_images(5, "sample_test_images")
            
            test_files = [f for f in os.listdir("sample_test_images") if f.endswith('.jpg')]
            if test_files:
                img_file = random.choice(test_files)
                img_path = os.path.join("sample_test_images", img_file)
                
                print(f"\n🔍 Testing: {img_file}")
                prediction = predict_single_image_complete(model, img_path, class_names)
                
                if prediction:
                    print(f"✅ Result: {prediction['class']} ({prediction['confidence']:.3f})")
                    visualize_single_prediction(img_path, prediction)
                else:
                    print("❌ No detection")
            else:
                print("❌ No sample images found")
        
        elif choice == "2":
            # Test with specific image
            img_path = input("Enter image path: ").strip()
            if os.path.exists(img_path):
                prediction = predict_single_image_complete(model, img_path, class_names)
                if prediction:
                    print(f"✅ Result: {prediction['class']} ({prediction['confidence']:.3f})")
                    visualize_single_prediction(img_path, prediction)
                else:
                    print("❌ No detection")
            else:
                print("❌ Image not found")
        
        elif choice == "3":
            # Generate new samples
            num_images = int(input("Number of images to generate (default 5): ") or "5")
            create_sample_test_images(num_images, "sample_test_images")
        
        elif choice == "4":
            # Batch test
            folder_path = input("Enter folder path (default: sample_test_images): ").strip()
            if not folder_path:
                folder_path = "sample_test_images"
            
            if os.path.exists(folder_path):
                test_results = test_model_with_samples(model_path, class_names, folder_path)
                print(f"\n📊 Batch test completed on {len(test_results)} images")
            else:
                print("❌ Folder not found")
        
        elif choice == "5":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

# Run interactive test
interactive_model_test()