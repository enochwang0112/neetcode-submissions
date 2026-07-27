class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        visited = [[False] * n for _ in range(m)]
        original = image[sr][sc]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            elif visited[row][col]:
                return
            elif image[row][col] != original:
                return
            else:
                visited[row][col] = True
                image[row][col] = color
                dfs(row, col + 1)
                dfs(row, col - 1)
                dfs(row + 1, col)
                dfs(row - 1, col)
        
        dfs(sr, sc)
        return image
                