class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # first mark one island and then run bfs
        m, n = len(grid), len(grid[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            elif grid[row][col] != 1:
                return
            else:
                grid[row][col] = 2
                queue.append((row, col))

                for dr, dc in directions:
                    dfs(row + dr, col + dc)

        found = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break
        
        timer = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    elif grid[nr][nc] == 2:
                        continue
                    elif grid[nr][nc] == 1:
                        return timer
                    else:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            
            timer += 1
        
        return -1