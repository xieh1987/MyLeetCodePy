class Solution:
    # @return an integer
    def atoi(self, str):
        aDict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        subStr=str
        num=0
        negative=False
        if subStr:
            while subStr[0]==' ':
                subStr=subStr[1:]
            if subStr[0]=='-' or subStr[0]=='+':
                negative=True if subStr[0]=='-' else False
                subStr=subStr[1:]
            while subStr:
                if subStr[0] in aDict:
                    num=num*10+aDict[subStr[0]]
                    subStr=subStr[1:]
                else:
                    break
        if negative:
            num=-num
        if num>=0:
            return min(2147483647, num) 
        else:
            return max(-2147483648, num)
