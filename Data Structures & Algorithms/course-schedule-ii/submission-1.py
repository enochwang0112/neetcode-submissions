class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()
        curr_path = set()
        order = []

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
            order.append(node)

            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return order[::-1]