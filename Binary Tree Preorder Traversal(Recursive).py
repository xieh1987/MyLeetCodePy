# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        aList=[]
        if root:
            aList+=[root.val]
            if root.left:
                aList+=self.preorderTraversal(root.left)
            if root.right:
                aList+=self.preorderTraversal(root.right)
        return aList
