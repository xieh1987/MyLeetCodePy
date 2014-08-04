class Solution:
    # @return a float
    def getkValue(self,A,B,k):
        if len(A)>len(B):
            return self.getkValue(B,A,k)
        else:
            if len(A)==0:
                return B[k-1]
            if k==1:
                return min(A[0],B[0])
            posa=min(k/2, len(A))
            posb=k-posa
            return self.getkValue(A[posa:], B, posb) if A[posa-1]<=B[posb-1] else self.getkValue(A, B[posb:], posa)    
    
    def findMedianSortedArrays(self, A, B):
        if (len(A)+len(B))%2:
            return self.getkValue(A, B, (len(A)+len(B))//2+1)
        else:
            return (self.getkValue(A, B, (len(A)+len(B))//2)+self.getkValue(A, B, (len(A)+len(B))//2+1))/2.0
