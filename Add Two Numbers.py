# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head=ListNode(0)
        currNode=head
        val,res=0,0
        while l1!=None or l2!=None:
            if l1!=None:
                val+=l1.val
                l1=l1.next
            if l2!=None:
                val+=l2.val
                l2=l2.next
            res=val%10
            val=val//10
            currNode.next=ListNode(res)
            currNode=currNode.next
        if val==1:
            currNode.next=ListNode(1)
        return head.next
