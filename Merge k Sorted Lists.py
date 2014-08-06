# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        pheap = []
        for i in lists:
             if i:
                 heapq.heappush(pheap, (i.val, i))
        head = ListNode(0)
        currNode = head
        while pheap:
            temp = heapq.heappop(pheap)[1]
            currNode.next = temp
            currNode = currNode.next
            if temp.next:
                heapq.heappush(pheap, (temp.next.val, temp.next))
        return head.next
