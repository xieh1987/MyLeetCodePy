class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle)==1:
            return triangle[0][0]
        else:
            for row in range(len(triangle)-1,0,-1):
                for column in range(row):
                    triangle[row-1][column]+=min(triangle[row][column],triangle[row][column+1])
            return triangle[0][0]
