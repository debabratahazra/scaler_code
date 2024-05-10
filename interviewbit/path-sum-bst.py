'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.'''


# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
    def hasPathSum(self, A, B):
        root = A
        sum = B
        if root is None:  # If tree is empty
            return 0

        else:
            answer = False 

            # Subtract the node value from sum
            subSum = sum - root.val 

            # if reach a leaf node and sum becomes 0, return True
            if(subSum == 0 and root.left == None and root.right == None):
                return True

            # Otherwise, check both subtrees
            if root.left is not None:
                answer = answer or self.hasPathSum(root.left, subSum)
            if root.right is not None:
                answer = answer or self.hasPathSum(root.right, subSum)

            if answer:
                return 1
            else:
                return 0

s = Solution()

# Let's create a binary tree with the following structure:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \      \
#   7    2      1

root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print(s.hasPathSum(root, 22))  # Should return True (5->4->11->2)
print(s.hasPathSum(root, 27))  # Should return True (5->8->13->1)
print(s.hasPathSum(root, 15))  # Should return False
