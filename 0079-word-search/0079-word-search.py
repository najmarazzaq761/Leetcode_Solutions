class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, k):

            # complete word match 
            if k == len(word):
                return True
            # out of range or mismatch condition
            if i<0 or i >= m or j<0 or j >= n or board[i][j] != word[k]:
                return False

            # visited mark
            temp = board[i][j]
            board[i][j] = "#"

            # directions 
            found = (dfs(i+1, j, k+1)  or
                     dfs(i-1, j, k+1)  or
                     dfs(i, j+1, k+1)  or
                     dfs(i, j-1, k+1))
            # backtrack (restore)
            board[i][j] = temp
            return found

        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False


