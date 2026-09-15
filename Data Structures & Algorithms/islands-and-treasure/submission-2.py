class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= m or nc < 0 or nc >= n
                        or (nr, nc) in visited or grid[nr][nc] == -1):
                        continue
                    visited.add((nr, nc))
                    q.append([nr, nc])
            dist += 1
        