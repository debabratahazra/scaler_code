import os
from datetime import datetime

# Global project name variable
project_name = "improved_object_detection"

def create_improved_project_structure():
    """Create comprehensive project directory structure"""
    
    global project_name
    
    directories = [
        f"{project_name}",
        f"{project_name}/data/synthetic_raw",
        f"{project_name}/data/synthetic_raw/images",
        f"{project_name}/data/synthetic_raw/labels",
        f"{project_name}/data/processed/train/images",
        f"{project_name}/data/processed/train/labels", 
        f"{project_name}/data/processed/val/images",
        f"{project_name}/data/processed/val/labels",
        f"{project_name}/data/processed/test/images",
        f"{project_name}/data/processed/test/labels",
        f"{project_name}/models/baseline",
        f"{project_name}/models/improved",
        f"{project_name}/results/baseline",
        f"{project_name}/results/improved",
        f"{project_name}/logs",
        f"{project_name}/comparisons"
    ]
    
    for directory in directories:
        # Check if directory exists, if not create it
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    print("✅ Enhanced project structure created!")
    print(f"📁 Project directory: {project_name}")
    return project_name