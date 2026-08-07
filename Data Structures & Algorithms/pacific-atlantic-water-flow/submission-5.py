class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        pacific, atlantic = set(), set()

        def dfs(row, col, height, visited):
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            elif (row, col) in visited:
                return
            elif heights[row][col] < height:
                return
            else:
                visited.add((row, col))
                
                for dr, dc in directions:
                    dfs(row + dr, col + dc, heights[row][col], visited)
        
        for i in range(n):
            dfs(0, i, heights[0][i], pacific)
            dfs(m - 1, i, heights[m - 1][i], atlantic)
        
        for i in range(m):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, n - 1, heights[i][n - 1], atlantic)
        
        return [[row, col] for row, col in pacific if (row, col) in atlantic]