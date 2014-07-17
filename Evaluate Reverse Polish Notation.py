class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        tempList=[]
        for i in range(len(tokens)):
            if tokens[i]=='+':
                b = int(tempList.pop())
                a = int(tempList.pop())
                tempList.append(a+b)
            elif tokens[i]=='-':
                b = int(tempList.pop())
                a = int(tempList.pop())
                tempList.append(a-b)
            elif tokens[i]=='*':
                b = int(tempList.pop())
                a = int(tempList.pop())
                tempList.append(a*b)
            elif tokens[i]=='/':
                b = float(tempList.pop())
                a = float(tempList.pop())
                tempList.append(int(a/b))
            else:
                tempList.append(tokens[i])
        return int(tempList.pop())
