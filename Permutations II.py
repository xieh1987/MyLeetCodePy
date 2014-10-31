class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if len(num)==0:
            return []
        if len(num)==1:
            return [num]
        num.sort()
        result = []
        for i in range(len(num)):
            if i>0 and num[i]==num[i-1]:
                continue
            for j in self.permuteUnique(num[:i]+num[i+1:]):
                result.append([num[i]]+j)
        return result
