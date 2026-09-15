class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)

        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            visiting.add(crs)
            for neigh in adj[crs]:
                if not dfs(neigh):
                    return False
            visiting.remove(crs)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
