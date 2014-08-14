# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        front, rear = head, head
        while True:
            if front.next: front = front.next
            else: break
            if front.next: front, rear = front.next, rear.next
            else: break
        dummy = ListNode(0)
        dummy.next, curr = rear.next, rear.next
        while curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
        curr1, curr2, rear.next = head, dummy.next, None
        while curr2:
            tmp, curr2 = curr2, curr2.next
            tmp.next, curr1.next = curr1.next, tmp
            curr1 = curr1.next.next
