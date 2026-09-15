class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)

        for u, v in prerequisites:
            prereqs[u].append(v)
        
        res = []
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for neigh in prereqs[crs]:
                if not dfs(neigh):
                    return False
            visited.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
