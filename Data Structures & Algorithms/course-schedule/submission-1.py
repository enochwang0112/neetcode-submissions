class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # check for cycles, if path has no cycles add to visited
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()
        curr_path = set()

        def dfs(node):
            if node in curr_path:
                return False
            if node in visited:
                return True
            
            curr_path.add(node)
            visited.add(node)

            for a in graph[node]:
                if dfs(a) == False:
                    return False
            
            curr_path.remove(node)

            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True