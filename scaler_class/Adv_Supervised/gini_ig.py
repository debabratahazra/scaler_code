'''
Lets assume a dataset has 5 purple and 5 yellow examples. If we split the dataset into 
two branches. The left branch has 4 purples while the right one has 5 yellows and 1 purple.

A perfect split would have five examples on each branch. This is clearly not a perfect split, 
but we can determine how good the split is (by weighing the "Gini Index" of each branch by
the number of elements each contains.). Please calculate the Information Gain and 
the weighted Gini Index of child after the split.
'''

import numpy as np

def gini_index(groups, classes):
    """Calculate the Gini Index for a split dataset."""
    total_samples = sum(len(group) for group in groups)
    gini = 0.0
    for group in groups:
        group_size = len(group)
        if group_size == 0:
            continue
        # Calculate class proportions in the group
        proportions = [np.sum(group == c) / group_size for c in classes]
        # Sum squared probabilities
        gini_group = 1.0 - sum(p**2 for p in proportions)
        # Weighted contribution to total Gini
        gini += gini_group * (group_size / total_samples)
    return gini

def information_gain(parent_gini, child_gini):
    """Calculate Information Gain from parent and child Gini indices."""
    return parent_gini - child_gini

# Define the dataset (0 = Purple, 1 = Yellow)
parent = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])  # 5 Purple, 5 Yellow

# Split into left (4 Purple, 0 Yellow) and right (1 Purple, 5 Yellow)
left_branch = np.array([0, 0, 0, 0])  # 4 Purple
right_branch = np.array([0, 1, 1, 1, 1, 1])  # 1 Purple, 5 Yellow

# Classes (Purple=0, Yellow=1)
classes = [0, 1]

# Calculate parent Gini
parent_gini = 1.0 - ( (5/10)**2 + (5/10)**2 )

# Calculate weighted Gini for children
child_groups = [left_branch, right_branch]
child_gini = gini_index(child_groups, classes)

# Calculate Information Gain
info_gain = information_gain(parent_gini, child_gini)

print(f"Parent Gini Index: {parent_gini:.4f}")
print(f"Weighted Gini Index (after split): {child_gini:.4f}")
print(f"Information Gain: {info_gain:.4f}")