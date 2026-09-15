class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)
        
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            cycle.add(crs)
            for neigh in adj[crs]:
                if not dfs(neigh):
                    return False
            cycle.remove(crs)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True


            
