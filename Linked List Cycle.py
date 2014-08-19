# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        aDict, found, curr = {}, False, head
        while curr:
            if curr in aDict:
                return True
            else:
                aDict[curr] = 0
                curr = curr.next
        return found
