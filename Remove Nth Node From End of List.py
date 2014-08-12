# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        aStack, dummy = [], ListNode(0)
        dummy.next = head
        curr = dummy
        while curr:
            aStack.append(curr)
            curr = curr.next
        for i in range(n):
            curr = aStack.pop()
        temp = aStack.pop()
        temp.next = curr.next
        return dummy.next
