class Solution:
    # @return an integer
    def reverse(self, x):
        if x<0:
            return -self.reverse(-x)
        if x==0:
            return 0
        aQueue=[]
        res=x
        while res>0:
            aQueue.append(res%10)
            res=res//10
        num=1
        while aQueue:
            temp=aQueue.pop(0)
            if temp:
                num=num*temp
                break
        while aQueue:
            temp=aQueue.pop(0)
            num=num*10+temp
        return num
