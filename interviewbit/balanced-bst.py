'''
Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).

Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

'''

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        nums = A
        if not nums:
            return None

        mid_val = len(nums) // 2

        node = TreeNode(nums[mid_val])
        node.left = self.sortedArrayToBST(nums[:mid_val])
        node.right = self.sortedArrayToBST(nums[mid_val+1:])

        return node
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
root = s.sortedArrayToBST(nums)
s.inorder(root)