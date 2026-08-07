class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # run bfs from every chest

        m, n = len(grid), len(grid[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                elif grid[nr][nc] != 2147483647:
                    continue
                else:
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))
