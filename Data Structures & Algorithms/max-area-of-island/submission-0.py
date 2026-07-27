class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        max_so_far = 0

        def dfs(row, col) -> int:
            if row < 0 or col < 0 or row >= m or col >= n:
                return 0
            elif visited[row][col]:
                return 0
            elif grid[row][col] == 0:
                return 0
            else:
                visited[row][col] = True
                return 1 + (
                    dfs(row, col + 1) + 
                    dfs(row, col - 1) + 
                    dfs(row + 1, col) + 
                    dfs(row - 1, col)
                )
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_so_far = max(max_so_far, dfs(i, j))

        return max_so_far