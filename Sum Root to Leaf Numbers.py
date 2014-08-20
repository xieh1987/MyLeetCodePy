# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        result = []
        self.Helper(root, result, 0)
        sum = 0
        for i in range(len(result)):
            sum += result[i]
        return sum
        
    def Helper(self, currNode, result, num):
        if (not currNode.left) and (not currNode.right):
            result.append(num*10+currNode.val)
        if currNode.left:
            self.Helper(currNode.left, result, currNode.val+num*10)
        if currNode.right:
            self.Helper(currNode.right, result, currNode.val+num*10)
