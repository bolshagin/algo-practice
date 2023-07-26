from typing import List


class Solution(object):
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            row, column = {}, {}
            for j in range(n):
                if board[j][i] in column and board[j][i] != '.':
                    return False
                if board[i][j] in row and board[i][j] != '.':
                    return False
                column[board[j][i]] = True
                row[board[i][j]] = True

        for start_row in range(0, n, 3):
            for start_column in range(0, n, 3):
                cell = {}
                for i in range(start_row, start_row + 3):
                    for j in range(start_column, start_column + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in cell:
                            return False
                        cell[board[i][j]] = True
        return True


if __name__ == "__main__":
    s = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(s.is_valid_sudoku(board))
