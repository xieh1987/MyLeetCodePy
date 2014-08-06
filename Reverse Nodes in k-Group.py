# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head:
            return None
        aStack = []
        dummy = ListNode(0)
        curr = dummy
        tmp = head
        while tmp:
            for i in range(k):
                if tmp:
                    aStack.append(tmp)
                    tmp = tmp.next
            if len(aStack)==k:
                while aStack:
                    curr.next = aStack.pop()
                    curr = curr.next
                    curr.next = None
            else:
                while aStack:
                    curr.next = aStack.pop(0)
                    curr = curr.next
                    curr.next = None
        return dummy.next
