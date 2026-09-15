class Solution:
    def rob(self, nums: List[int]) -> int:
        #              i      
        # [2, 9, 8, 3, 6]
        #prev curr
        # [2, 9, 10, 12, 16]
        #  0, 1,  2 , 3,  4
        # calculate dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = prev
            prev = curr
            curr = max(temp + nums[i], prev)
        return curr
            


            





    