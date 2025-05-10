import numpy as np

def entropy(s):
    '''
    Calculates the entropy given list of target(binary) variables
    '''
    # Write your code here
    
    # Caclulate entropy
    entropy = 0
    
    
    #Your code ends here
    # Calculate entropy
    unique_labels, counts = np.unique(s, return_counts=True)
    total_count = len(s)
    probabilities = counts / total_count
    entropy = np.sum(probabilities * np.log2(probabilities))
    
    return -entropy
    

def information_gain(parent, left_child, right_child):
    
    '''
    Compute information gain given left_child target variables (list), right_child target variables(list) and their parent targets(list)
    '''
    
    info_gain=None
    # Write your code here
    
    # Calculate information gain
    parent_entropy = entropy(parent)
    left_entropy = entropy(left_child)
    right_entropy = entropy(right_child)
    left_weight = len(left_child) / len(parent)
    right_weight = len(right_child) / len(parent)
    info_gain = parent_entropy - (left_weight * left_entropy) - (right_weight * right_entropy)
    #Your code ends here
    return info_gain
    
def best_split(features,labels):
    '''
    inputs:
        features: nd-array
        labels: nd-array
    output:
        float value determining best threshold for decision tree classification
    '''
    
    best_threshold=None
    best_info_gain = -1
    
    # For every unique value of that feature
    for threshold in np.unique(features):
            
        y_left = labels[features <= threshold]  #list of labels in left child
        y_right = labels[features > threshold]  #list of labels in right child
            
        if len(y_left) > 0 and len(y_right) > 0:
            gain = information_gain(labels, y_left, y_right)  # Calculate the information gain and save the split parameters if the current split is better than the previous best
    
            if gain > best_info_gain:
                best_threshold = threshold
                best_info_gain = gain
    
    return best_threshold


feature= np.array([0.58, 0.9 , 0.45, 0.18, 0.5,  0.12, 0.31, 0.09, 0.24 ,0.83])
label= np.array([1, 0, 0, 0, 0, 0, 1, 0 ,1, 1])
print(best_split(feature,label))