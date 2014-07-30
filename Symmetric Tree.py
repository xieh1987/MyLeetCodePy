# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        def swap(root):
            if root==None:
                return root
            if root.left or root.right:
                temp=swap(root.left)
                root.left=swap(root.right)
                root.right=temp
            return root
    
        def isSame(node1, node2):
            if node1==None and node2==None:
                return True
            elif node1==None or node2==None:
                return False
            else:
                if node1.val==node2.val:
                    return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
                else:
                    return False
                    
        if root==None:
            return True
        else:
            return isSame(root.left, swap(root.right))
