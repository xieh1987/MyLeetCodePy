class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left, right = 0, len(A)-1
        while left<=right:
            mid = (left+right)//2
            if A[mid]==target:
                return mid
            if A[left]>A[mid]:
                if A[right]>=target and A[mid]<target:
                    left=mid+1
                else:
                    right = mid-1
            elif A[left]<A[mid]:
                if A[left]<=target and A[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            else:
                left += 1
        return -1
