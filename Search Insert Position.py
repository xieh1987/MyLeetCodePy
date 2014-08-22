class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left, right = 0, len(A)-1
        while left<=right:
            if A[left]>target:
                return left
            elif A[right]<target:
                return right+1
            else:
                mid = (left+right)//2
                if A[mid]==target:
                    return mid
                elif A[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
