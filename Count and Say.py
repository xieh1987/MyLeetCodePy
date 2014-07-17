class Solution:
    # @return a string
    def countAndSay(self, n):
        if n==1:
            return '1'
        elif n==2:
            return '11'
        else:
            myStr=self.countAndSay(n-1)
            count=1
            newStr=''
            for i in range(1,len(myStr)):
                if myStr[i]==myStr[i-1]:
                    count+=1
                else:
                    newStr+=str(count)+myStr[i-1]
                    count=1
            newStr+=str(count)+myStr[len(myStr)-1]
            return newStr
