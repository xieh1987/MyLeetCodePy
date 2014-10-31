class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        result = [[1 for j in range(len(matrix))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                result[i][j] = matrix[len(matrix)-1-j][i]
        return result
