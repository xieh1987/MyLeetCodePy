class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        found=False
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=m-1
        while low<=high:
            mid=(low+high)//2
            if matrix[mid][0]==target:
                found=True
                break
            elif matrix[mid][0]>target:
                high=mid-1
            else:
                low=mid+1
        if high<0:
            return False
        head=0
        end=n-1
        while head<=end and not found:
            mid=(head+end)//2
            if matrix[high][mid]==target:
                found=True
            elif matrix[high][mid]>target:
                end=mid-1
            else:
                head=mid+1
        return found
