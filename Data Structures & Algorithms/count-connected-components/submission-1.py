class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for v in graph[node]:
                dfs(v)
        
        num = 0

        for i in range(n):
            if i not in visited:
                num += 1
                dfs(i)
        
        return num