# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        return self.height(root)
        
    def height(self, currNode):
        if (not currNode.left) and (not currNode.right):
            return 1
        if not currNode.left:
            return 1+self.height(currNode.right)
        if not currNode.right:
            return 1+self.height(currNode.left)
        return 1+min(self.height(currNode.left), self.height(currNode.right))
