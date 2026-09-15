class Solution:
    def climbStairs(self, n: int) -> int:
        #. p     c        
        # [1, 2, 3, 0]
        # n = 4
        # at each point, ask yourself: how many ways are there to get to that step?
        
        if n == 1:
            return 1
        prev, curr = 1, 2
        for i in range(2, n):
            temp = curr
            curr = temp + prev
            prev = temp
        return curr

