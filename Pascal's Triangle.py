class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        Triangle=[]
        if numRows==1:
            Triangle=[[1]]
        elif numRows>1:
            Triangle=[[1]]
            for row in range(1,numRows):
                rowList=[1]
                for column in range(1,row):
                    rowList.append(Triangle[row-1][column-1]+Triangle[row-1][column])
                rowList.append(1)
                Triangle.append(rowList)
        else:
            pass
        return Triangle
