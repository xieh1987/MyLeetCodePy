class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        pos, next = -1, 0
        for i in range(len(num)-1):
            if num[i]<num[i+1]:
                pos = i
        if pos==-1:
            return num[::-1]
        for i in range(pos, len(num)):
            if num[i]>num[pos]:
                next = i
        num[pos], num[next] = num[next], num[pos]
        return num[:pos+1]+num[:pos:-1]
