'''
Given a binary tree, determine if it is a valid binary search tree
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isValidBST(self, A):
        root = A
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not a BST.
            if root.val <= inorder:
                return 0
            inorder = root.val
            root = root.right

        return 1

s = Solution()

# Create nodes
root = TreeNode(5)
node3 = TreeNode(3)
node8 = TreeNode(8)
node2 = TreeNode(2)
node4 = TreeNode(4)
node6 = TreeNode(6)
node9 = TreeNode(9)

# Connect nodes to construct the tree
#      5
#     / \
#    3   8
#   / \ / \
#  2  4 6  9
root.left = node3
root.right = node8
node3.left = node2
node3.right = node4
node8.left = node6
node8.right = node9

print(s.isValidBST(root))  # Output: True

# Now, let's create a binary tree that is not a BST
# Create nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

# Connect nodes to construct the tree
#  1
# / \
#2   3
root.left = node2
root.right = node3

print(s.isValidBST(root))  # Output: False
