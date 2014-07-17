class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A)<=1:
            return 0
        else:
            i=0
            step=1
            last=A[0]
            while last<len(A)-1:
                for tryfrom in range(i,i+A[i]):
                    if tryfrom+A[tryfrom]>last+A[last]:
                        last=tryfrom
                step+=1
                i=last
                last=i+A[i]
            return step
