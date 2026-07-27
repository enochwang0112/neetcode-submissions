class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        total = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    total += 1
        
        return total