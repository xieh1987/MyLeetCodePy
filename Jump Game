class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A)<=1:
            return True
        pos=0
        while pos<len(A) and A[pos]!=0:
            maxpos=pos+A[pos]
            for tryfrom in range(pos ,min(pos+A[pos],len(A)-1)):
                maxpos=max(maxpos,tryfrom+A[tryfrom])
            pos=max(maxpos,pos+A[pos])
        return pos>=len(A)-1
