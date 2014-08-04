# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        aList=[]
        if root:
            if root.left:
                aList+=self.postorderTraversal(root.left)
            if root.right:
                aList+=self.postorderTraversal(root.right)
            aList+=[root.val]
        return aList
