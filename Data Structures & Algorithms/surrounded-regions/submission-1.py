class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            elif board[row][col] != "O":
                return
            else:
                board[row][col] = "#"
                dfs(row, col + 1)
                dfs(row, col - 1)
                dfs(row + 1, col)
                dfs(row - 1, col)
        
        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"