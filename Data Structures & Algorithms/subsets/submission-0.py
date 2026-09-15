class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            #you can include i 
            curr.append(nums[i])
            dfs(i + 1)
            #you can exclude i
            curr.pop()
            dfs(i + 1)
            return res
        
        return dfs(0)