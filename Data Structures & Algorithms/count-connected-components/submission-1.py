class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)
        
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count
        
            

      
        
        

            
       
     
        
        

        




        
