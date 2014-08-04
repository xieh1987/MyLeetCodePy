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
        aStack=[]
        currNode=root
        while currNode or aStack:
            while currNode:
                aList+=[currNode.val]
                aStack+=[currNode]
                currNode=currNode.left
            if aStack:
                temp=aStack.pop()
                currNode=temp.right
        return aList
