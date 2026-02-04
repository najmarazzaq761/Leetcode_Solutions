class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
       
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isValid(row, col):
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # Check left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # Check right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def solve(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if isValid(row, col):
                    board[row][col] = 'Q'
                    solve(row + 1)
                    board[row][col] = '.'

        solve(0)
        return result

            