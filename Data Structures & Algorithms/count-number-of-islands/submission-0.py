class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            elif visited[row][col]:
                return
            elif grid[row][col] == '0':
                return
            else:
                visited[row][col] = True
                dfs(row, col + 1)
                dfs(row, col - 1)
                dfs(row + 1, col)
                dfs(row - 1, col)

        num = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    num += 1
                    dfs(i, j)

        return num