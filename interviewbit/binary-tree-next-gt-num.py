'''
Given a BST node, return the node which has value just greater than the given node.
If not found, return NULL'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        root = A
        p = B
        successor = None
        while root:
            if root.val > p:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

s = Solution()

# Create nodes
root = TreeNode(20)
node8 = TreeNode(8)
node22 = TreeNode(22)
node4 = TreeNode(4)
node12 = TreeNode(12)
node10 = TreeNode(10)
node14 = TreeNode(14)
node25 = TreeNode(25)

# Connect nodes to create the tree
#         20
#        /  \
#       8    22
#      / \
#     4  12
#        / \
#       10 14
#            \
#            25

root.left = node8
root.right = node22
node8.left = node4
node8.right = node12
node12.left = node10
node12.right = node14
node14.right = node25

# Test the function
target_node = 12
successor = s.getSuccessor(root, target_node)
if successor is not None:
    print("Successor of node", target_node, "is", successor.val)  # Output: Successor of node 6 is 8
else:
    print("No successor found for node", target_node)
