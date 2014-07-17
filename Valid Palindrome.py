class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s)<=1:
            return True
        s=s.lower()
        char='0123456789abcdefghijklmnopqrstuvwxyz'
        isPali=True
        aList=list(s)
        head=0
        tail=len(aList)-1
        while head<=tail:
            while aList[head] not in char and head<tail:
                head+=1
            while aList[tail] not in char and tail>head:
                tail-=1
            if aList[head]!=aList[tail]:
                isPali=False
                break
            else:
                head+=1
                tail-=1
        return isPali
