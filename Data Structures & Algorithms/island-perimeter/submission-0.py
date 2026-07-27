class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(row, col) -> int:
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            elif visited[row][col]:
                return 0
            elif grid[row][col] == 0:
                return 1
            else:
                visited[row][col] = True
                return (
                    dfs(row, col + 1) +
                    dfs(row, col - 1) +
                    dfs(row + 1, col) +
                    dfs(row - 1, col)
                )
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)
                
        