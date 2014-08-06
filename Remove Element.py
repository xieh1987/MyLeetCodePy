class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, last = 0, len(A)-1
        while i<=last:
            if A[i]==elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return i
