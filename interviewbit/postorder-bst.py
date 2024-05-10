'''
Given a binary tree, return the Postorder traversal of its nodes values.

NOTE: Using recursion is not allowed.
'''

# Definition for a  binary tree node
class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers

    def postorderTraversal(self, A):
        root = A
        if root is None:
            return []

        stack1, stack2 = [root], []
        output = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            output.append(node.val)

        return output

s = Solution()

# Creating a binary tree
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)

# Test the function with the tree
print(s.postorderTraversal(root))  # Expected output: [3, 2, 1]

# Creating another binary tree
root = Node(7)
root.left = Node(4)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(8)

# Test the function with the tree
print(s.postorderTraversal(root))  # Expected output: [1, 5, 4, 8, 9, 7]

    
