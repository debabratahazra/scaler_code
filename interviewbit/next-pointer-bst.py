'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
'''

# Definition for a  binary tree node
class TreeLinkNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        # Start with the root node. There are no next right nodes at the root level
        node = root
        node.next = None

        # Continue with other levels
        while node.left:
            # For each node at the current level, connect the child nodes
            curr = node
            while curr:
                # Connect the left child to the right child
                curr.left.next = curr.right

                # Connect the right child to the next left child, if available
                if curr.next:
                    curr.right.next = curr.next.left
                else:
                    curr.right.next = None

                # Move to the next node at the current level
                curr = curr.next

            # Move to the next level
            node = node.left

s = Solution()


# Let's create a binary tree with the following structure:
#          1
#         / \
#        2   3
#       / \ / \
#      4  5 6  7

root = TreeLinkNode(1)

root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)

root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

# Call the connect function
s.connect(root)

# Now, we'll print the tree level by level, using the next pointers
node = root
while node:
    curr = node
    while curr:
        print(curr.val, end = " ")
        curr = curr.next
    print("\n")
    node = node.left
        
