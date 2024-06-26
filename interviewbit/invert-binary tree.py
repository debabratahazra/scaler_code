'''
Given a binary tree A, invert the binary tree and return it. 

 Inverting refers to making left child as the right child and vice versa.
 '''
 
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
    def invertTree(self, A):
        if A is None:
            return None

        # Recursively invert the left subtree
        left_inverted = self.invertTree(A.left)
        # Recursively invert the right subtree
        right_inverted = self.invertTree(A.right)

        # Swap the inverted subtrees
        A.left, A.right = right_inverted, left_inverted

        return A
    
s = Solution()

# Example usage:
# Construct the binary tree
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Invert the binary tree
reverse_tree = s.invertTree(root)
print(reverse_tree)

# Now the tree should be:
#       1
#      / \
#     3   2
#    / \ / \
#   7  6 5  4