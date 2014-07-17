class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        map={}
        sum=0
        for i in range(len(A)):
            if A[i] not in map:
                sum+=A[i]
                map[A[i]]=i
            else:
                sum-=A[i]
        return sum
