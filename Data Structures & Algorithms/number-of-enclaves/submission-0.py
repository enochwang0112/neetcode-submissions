class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            elif grid[row][col] != 1:
                return
            else:
                grid[row][col] = 0
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

        num = 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    num += 1
        
        return num