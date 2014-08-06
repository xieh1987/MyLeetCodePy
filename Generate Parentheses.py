class Solution:
    # @param an integer
    # @return a list of string
    def helper(self, n, left, right, curr, result):
        if left==n and right==n:
            result.append(curr)
        if left<n:
            self.helper(n, left+1, right, curr+'(', result)
        if right<left:
            self.helper(n, left, right+1, curr+')', result)
    
    def generateParenthesis(self, n):
        result=[]
        self.helper(n, 0, 0, '', result)
        return result
