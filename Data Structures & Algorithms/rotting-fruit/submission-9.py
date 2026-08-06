class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs from rotten fruit
        m, n = len(grid), len(grid[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        timer = 0
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    elif grid[nr][nc] != 1:
                        continue
                    else:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            timer += 1
        
        if fresh == 0:
            return timer
        else:
            return -1
        