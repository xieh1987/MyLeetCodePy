# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        curr = head
        while curr and curr.next:
            tail = curr.next.next
            tmp = curr.next
            pre.next = tmp
            tmp.next = curr
            curr.next = tail
            curr = tail
            pre = pre.next.next
        return dummy.next
