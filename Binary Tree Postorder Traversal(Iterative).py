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
        aStack=[]
        pre=None
        currNode=root
        while currNode or aStack:
            while currNode:
                aStack+=[currNode]
                currNode=currNode.left
            if aStack:
                temp=aStack.pop()
                if temp.right and temp.right!=pre:
                    currNode=temp.right
                    aStack+=[temp]
                else:
                    aList+=[temp.val]
                    pre=temp
        return aList
