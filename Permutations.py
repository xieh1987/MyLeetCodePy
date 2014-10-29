class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num)==0:
            return num
        if len(num)==1:
            return [num]
        result = []
        for i in range(len(num)):
            for j in self.permute(num[:i]+num[i+1:]):
                result.append([num[i]]+j)
        return result
