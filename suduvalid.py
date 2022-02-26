class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dict_row = []
        dict_col = []
        dict_cell = []
        for i in range(0,9):
            dict_row.append({})
            dict_col.append({})
            dict_cell.append({})
        for i in range(0,9):
            for j in range(0, 9):
                cur = board[i][j]
                if cur == ".":
                    continue
                if dict_row[i].get(cur) is not None:
                    return False
                dict_row[i][cur] = True

                if dict_col[j].get(cur) is not None:
                    return False
                dict_col[j][cur] = True

                if dict_cell[i//3*3 + j//3].get(cur) is not None:
                    return False
                dict_cell[i//3*3 + j//3][cur] = True
        return True      

Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

