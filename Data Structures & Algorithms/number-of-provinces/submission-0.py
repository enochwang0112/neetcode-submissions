class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)

        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        def dfs(city):
            if city in visited:
                return
            
            visited.add(city)
            for v in graph[city]:
                dfs(v)
        
        num = 0
        for i in range(n):
            if i not in visited:
                num += 1
                dfs(i)

        return num