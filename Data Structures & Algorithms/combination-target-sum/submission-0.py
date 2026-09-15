class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #base case -> numbers add up to target
        #constraint is if two combinations have the same frequency of nums
        #choices are num in nums
        #decision -> include i or exclude i
        #keep track of i and target 

        res = []
        curr = []

        def backtracking(i, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or curr_sum > target:
                return
            #first choice include i

            curr.append(nums[i])
            backtracking(i, curr_sum + nums[i])
            #second to exclude i
            curr.pop()
            backtracking(i + 1, curr_sum)
            return res
        
        return backtracking(0, 0)
