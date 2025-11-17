import json
import numpy as np
import matplotlib.pyplot as plt

def create_performance_comparison_charts(PROJECT_PATH, baseline_history, improved_history):
    """Create comprehensive performance comparison charts"""
    
    print("📊 Creating performance comparison charts...")
    
    # Load evaluation results
    with open(f"{PROJECT_PATH}/results/evaluation_results.json", "r") as f:
        results = json.load(f)
    
    baseline = results['baseline']
    improved = results['improved']
    
    # Create comprehensive comparison charts
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # 1. Overall Performance Comparison
    metrics = ['Classification\nAccuracy', 'Mean IoU', 'Excellent\nPredictions\n(IoU > 0.7)']
    baseline_values = [baseline['classification_accuracy'], baseline['mean_iou'], baseline['excellent_predictions_ratio']]
    improved_values = [improved['classification_accuracy'], improved['mean_iou'], improved['excellent_predictions_ratio']]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    axes[0, 0].bar(x - width/2, baseline_values, width, label='Baseline', color='lightcoral', alpha=0.8)
    axes[0, 0].bar(x + width/2, improved_values, width, label='Improved', color='lightblue', alpha=0.8)
    axes[0, 0].set_xlabel('Metrics')
    axes[0, 0].set_ylabel('Score')
    axes[0, 0].set_title('Overall Performance Comparison')
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(metrics)
    axes[0, 0].legend()
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for i, (base_val, imp_val) in enumerate(zip(baseline_values, improved_values)):
        axes[0, 0].text(i - width/2, base_val + 0.01, f'{base_val:.3f}', ha='center', va='bottom')
        axes[0, 0].text(i + width/2, imp_val + 0.01, f'{imp_val:.3f}', ha='center', va='bottom')
    
    # 2. IoU Distribution Comparison
    iou_ranges = ['0-0.1', '0.1-0.3', '0.3-0.5', '0.5-0.7', '0.7-0.9', '0.9-1.0']
    baseline_dist = [baseline['bbox_accuracy_distribution'][key]/baseline['total_samples'] for key in 
                     ['iou_0_1', 'iou_1_3', 'iou_3_5', 'iou_5_7', 'iou_7_9', 'iou_9_1']]
    improved_dist = [improved['bbox_accuracy_distribution'][key]/improved['total_samples'] for key in 
                     ['iou_0_1', 'iou_1_3', 'iou_3_5', 'iou_5_7', 'iou_7_9', 'iou_9_1']]
    
    x = np.arange(len(iou_ranges))
    axes[0, 1].bar(x - width/2, baseline_dist, width, label='Baseline', color='lightcoral', alpha=0.8)
    axes[0, 1].bar(x + width/2, improved_dist, width, label='Improved', color='lightblue', alpha=0.8)
    axes[0, 1].set_xlabel('IoU Range')
    axes[0, 1].set_ylabel('Proportion of Samples')
    axes[0, 1].set_title('IoU Distribution Comparison')
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels(iou_ranges, rotation=45)
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # 3. Class-wise Performance Comparison (Mean IoU)
    classes = list(baseline['class_performance'].keys())
    baseline_class_ious = [baseline['class_performance'][cls]['mean_iou'] for cls in classes]
    improved_class_ious = [improved['class_performance'][cls]['mean_iou'] for cls in classes]
    
    x = np.arange(len(classes))
    axes[0, 2].bar(x - width/2, baseline_class_ious, width, label='Baseline', color='lightcoral', alpha=0.8)
    axes[0, 2].bar(x + width/2, improved_class_ious, width, label='Improved', color='lightblue', alpha=0.8)
    axes[0, 2].set_xlabel('Classes')
    axes[0, 2].set_ylabel('Mean IoU')
    axes[0, 2].set_title('Class-wise IoU Comparison')
    axes[0, 2].set_xticks(x)
    axes[0, 2].set_xticklabels(classes)
    axes[0, 2].legend()
    axes[0, 2].grid(axis='y', alpha=0.3)
    
    # 4. Training History Comparison (if available)
    if hasattr(baseline_history, 'history') and hasattr(improved_history, 'history'):
        epochs_baseline = range(1, len(baseline_history.history['loss']) + 1)
        epochs_improved = range(1, len(improved_history.history['loss']) + 1)
        
        axes[1, 0].plot(epochs_baseline, baseline_history.history['val_loss'], 'r-', label='Baseline Val Loss', alpha=0.8)
        axes[1, 0].plot(epochs_improved, improved_history.history['val_loss'], 'b-', label='Improved Val Loss', alpha=0.8)
        axes[1, 0].set_xlabel('Epochs')
        axes[1, 0].set_ylabel('Validation Loss')
        axes[1, 0].set_title('Training Loss Comparison')
        axes[1, 0].legend()
        axes[1, 0].grid(alpha=0.3)
    
    # 5. Improvement Metrics
    improvements = {
        'IoU': results['comparison']['iou_improvement'],
        'Accuracy': results['comparison']['accuracy_improvement'],
        'Excellent\nPredictions': results['comparison']['excellent_predictions_improvement']
    }
    
    colors = ['green' if val > 0 else 'red' for val in improvements.values()]
    axes[1, 1].bar(improvements.keys(), improvements.values(), color=colors, alpha=0.7)
    axes[1, 1].set_ylabel('Improvement')
    axes[1, 1].set_title('Improvement Over Baseline')
    axes[1, 1].axhline(y=0, color='black', linestyle='-', alpha=0.3)
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, (key, val) in enumerate(improvements.items()):
        axes[1, 1].text(i, val + 0.001, f'{val:.4f}', ha='center', va='bottom' if val > 0 else 'top')
    
    # 6. Summary Statistics
    summary_text = f"""
IMPROVEMENT SUMMARY

📈 Mean IoU Improvement: {results['comparison']['iou_improvement']:.4f}
📊 Classification Accuracy Improvement: {results['comparison']['accuracy_improvement']:.4f}
🎯 Excellent Predictions Improvement: {results['comparison']['excellent_predictions_improvement']:.4f}

BASELINE MODEL:
• Mean IoU: {baseline['mean_iou']:.4f}
• Classification Accuracy: {baseline['classification_accuracy']:.4f}
• Excellent Predictions: {baseline['excellent_predictions_ratio']:.4f}

IMPROVED MODEL:
• Mean IoU: {improved['mean_iou']:.4f}
• Classification Accuracy: {improved['classification_accuracy']:.4f}
• Excellent Predictions: {improved['excellent_predictions_ratio']:.4f}

RELATIVE IMPROVEMENT:
• IoU: {((improved['mean_iou']/baseline['mean_iou'] - 1) * 100):.1f}%
• Accuracy: {((improved['classification_accuracy']/baseline['classification_accuracy'] - 1) * 100):.1f}%
• Excellent Pred: {((improved['excellent_predictions_ratio']/baseline['excellent_predictions_ratio'] - 1) * 100):.1f}%
    """
    
    axes[1, 2].text(0.05, 0.95, summary_text, transform=axes[1, 2].transAxes, 
                    verticalalignment='top', fontfamily='monospace', fontsize=9)
    axes[1, 2].set_xlim(0, 1)
    axes[1, 2].set_ylim(0, 1)
    axes[1, 2].axis('off')
    axes[1, 2].set_title('Performance Summary')
    
    plt.tight_layout()
    plt.savefig(f'{PROJECT_PATH}/comparisons/performance_comparison_charts.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Performance comparison charts created!")

