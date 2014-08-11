class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []
        
        for i in range(len(num)-2):
            if num[i]==num[i-1] and i-1>=0:
                continue
            else:
                for j in range(i+1, len(num)-1):
                    if num[j]==num[j-1] and j-1>i:
                        continue
                    if -(num[i]+num[j]) in num[j+1: len(num)]:
                        result.append([num[i], num[j], -(num[i]+num[j])])
        
        return result
