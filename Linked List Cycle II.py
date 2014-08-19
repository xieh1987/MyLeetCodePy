# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        aDict, curr = {}, head
        while curr:
            if curr in aDict:
                return curr
            else:
                aDict[curr] = 0
                curr = curr.next
        return None
