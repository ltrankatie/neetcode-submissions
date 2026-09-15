class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #base case -> if curr == word return True
        #if c at i does not much word, then return
        #choices -> go up down right left
        #backtrack
        #undo and go a different direction
           
        # "CAT"
        curr = ""
        m, n = len(board), len(board[0])
        visited = set()
        #where k is the index of the character we're looking at in word
        def backtrack(i, j, k):
            if k == len(word):
                return True 
            if (i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited
            or board[i][j] != word[k]): 
                return False
            visited.add((i, j))
            res = (backtrack(i + 1, j, k + 1) or
            backtrack(i - 1, j, k + 1) or
            backtrack(i, j + 1, k + 1) or
            backtrack(i, j - 1, k + 1))
            visited.remove((i, j))
            return res
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False



