class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        sum=0
        map={}
        for i in range(len(A)):
            if A[i] not in map:
                map[A[i]]=A[i]
                sum+=A[i]
            elif A[i]==map[A[i]]:
                map[A[i]]+=1
                sum+=A[i]
            else:
                sum-=2*A[i]
        return sum
