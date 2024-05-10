'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return  0 / 1  ( 0 for false, 1 for true ) for this problem
'''

# Definition for a  binary tree node
class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None or B is None:
            return 0
        elif A.val != B.val:
            return 0
        else:
            return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)

s = Solution()


# Creating the first binary tree
tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)

# Creating the second binary tree
tree2 = Node(1)
tree2.left = Node(2)
tree2.right = Node(3)

# Test the function with the trees
print(s.isSameTree(tree1, tree2))  # Expected output: 1 (because trees are the same)

# Modifying the second tree
tree2.right.right = Node(4)

# Test the function with the modified tree
print(s.isSameTree(tree1, tree2))  # Expected output: 0 (because trees are not the same)
