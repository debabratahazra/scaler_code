'''
Given a binary tree, return the inorder traversal of its nodes values without recursion.'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def inorderTraversal(self, A):
        root = A
        res = []
        stack = []
        while True:
            while root: 
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
    
s = Solution()

# Create nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Connect nodes to construct the tree
#     1
#    / \
#   2   3
#  / \
# 4   5
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5

print(s.inorderTraversal(root))  # Output: [4, 2, 5, 1, 3]