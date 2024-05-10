'''
Given a root of binary tree A, determine if it is height-balanced
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
    def isBalanced(self, A):
        def check_height(node):
            if node is None:
                return 0

            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return 1 if check_height(A) != -1 else 0

s = Solution()

# Create nodes for a balanced binary tree
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

print(s.isBalanced(root))  # Output: 1

# Now, create an imbalanced binary tree
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

# Connect nodes to construct the tree
# 1
#  \
#   2
#    \
#     3
#      \
#       4
root.right = node2
node2.right = node3
node3.right = node4

print(s.isBalanced(root))  # Output: 0

