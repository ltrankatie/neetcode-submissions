class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        #must keep track of the parent in undirected graphs
        #dfs can mistake a parent for a cycle
        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node):
                    return True
            return False
        
        #since you want to return the edge that creates the cycle
        #don't prebuild the graph--add edges one by one and immediately
        #return when you see the edge that causes the cycle
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            if dfs(u, -1):
                return [u, v]
        return []
