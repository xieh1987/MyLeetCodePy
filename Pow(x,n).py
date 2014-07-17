class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if x==0 or n==0:
            result=1
        if x!=0:
            if n>0:
                result=pow(x,n-1)*x
            else:
                result=1/pow(x,-n)
        return result
