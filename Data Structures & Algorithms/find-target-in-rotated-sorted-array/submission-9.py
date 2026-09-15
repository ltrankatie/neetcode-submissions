class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the min_index (aka the pivot index)
        #[3,4,5,6,1,2]
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        min_i = l

        if min_i == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
