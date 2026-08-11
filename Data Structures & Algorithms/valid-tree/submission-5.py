class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check for cycle and connected (run dfs once)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, node) == False:
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n