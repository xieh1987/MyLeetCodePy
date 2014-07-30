class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        head, end = 0, x/2+1
        while end>=head:
            mid=(head+end)/2
            if mid**2>x:
                end=mid-1
            else:
                head=mid+1
        return int(end)
