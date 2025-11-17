import cv2
import numpy as np

def predict_image(model, image_path, class_names):
    # Load and preprocess image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    original_shape = image.shape[:2]
    
    # Resize and normalize
    image_resized = cv2.resize(image, (224, 224))
    image_normalized = image_resized.astype(np.float32) / 255.0
    image_batch = np.expand_dims(image_normalized, axis=0)
    
    # Make prediction
    predictions = model.predict(image_batch)
    class_probs = predictions[0][0]
    bbox_coords = predictions[1][0]
    
    # Get results
    predicted_class_idx = np.argmax(class_probs)
    confidence = class_probs[predicted_class_idx]
    predicted_class = class_names[predicted_class_idx]
    
    # Convert bbox to pixel coordinates
    h, w = original_shape
    x1 = int(bbox_coords[0] * w)
    y1 = int(bbox_coords[1] * h)
    x2 = int(bbox_coords[2] * w)
    y2 = int(bbox_coords[3] * h)
    
    return {{
        'class': predicted_class,
        'confidence': confidence,
        'bbox': [x1, y1, x2, y2]
    }}

