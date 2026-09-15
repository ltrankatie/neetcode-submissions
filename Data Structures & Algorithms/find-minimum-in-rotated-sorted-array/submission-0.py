class Solution:
    def findMin(self, nums: List[int]) -> int:
        #
        #[3, 4, 5, 6, 1, 2]
        # 0. 1. 2. 3. 4. 5
        
        #what does it mean if m > l? increasing
        #if m > r, decreasing -> search in that portion
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
        return nums[l]
            