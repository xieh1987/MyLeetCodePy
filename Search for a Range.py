class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = self.searchStart(A, target)
        return [-1, -1] if start==-1 else [start, self.searchEnd(A, target)]
        
    def searchStart(self, A, target):
        left, right, start = 0, len(A)-1, -1
        while left<=right:
            mid = (left+right)//2
            if A[mid]==target:
                start = mid
                right = mid-1
            elif A[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return start
        
    def searchEnd(self, A, target):
        left, right, end = 0, len(A)-1, -1
        while left<=right:
            mid = (left+right)//2
            if A[mid]==target:
                end = mid
                left = mid+1
            elif A[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return end
