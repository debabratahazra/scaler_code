'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
    def levelOrder(self, A):
        root = A
        if not root:
            return []
        result, current_level = [], [root]
        while current_level:
            next_level, vals = [], []
            for node in current_level:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
            result.append(vals)
        return result
    


# Create nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Connect nodes to create the tree
#     1
#    / \
#   2   3
#  / \
# 4   5
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5

s = Solution()
print(s.levelOrder(root))

