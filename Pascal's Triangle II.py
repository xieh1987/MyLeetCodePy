class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        aList=[1]
        for k in range(1,rowIndex+1):
            aList.append(aList[-1]*(rowIndex+1-k)/(k))
        return aList
