'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a  binary tree node
class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isSymmetric(self, A):
        return self.isMirror(A, A)
    
    def isMirror(self,t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

s = Solution()

# Create a symmetric binary tree
tree = Node(1)
tree.left = Node(2)
tree.right = Node(2)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right.left = Node(4)
tree.right.right = Node(3)

# Test with symmetric tree
print(s.isSymmetric(tree))  # Output should be True

# Create an asymmetric binary tree
tree = Node(1)
tree.left = Node(2)
tree.right = Node(2)
tree.left.right = Node(3)
tree.right.right = Node(3)

# Test with asymmetric tree
print(s.isSymmetric(tree))  # Output should be False
