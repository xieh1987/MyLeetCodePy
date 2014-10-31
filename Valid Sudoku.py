class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(1, 9):
                if board[i][j]!='.' and board[i][j] in board[i][:j]:
                    return False
                    
        for j in range(9):
            row = [board[i][j] for i in range(9)]
            for k in range(1, 9):
                if row[k]!='.' and row[k] in row[:k]:
                    return False
                    
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                list = board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
                for k in range(1, 9):
                    if list[k]!='.' and list[k] in list[:k]:
                        return False
                        
        return True
