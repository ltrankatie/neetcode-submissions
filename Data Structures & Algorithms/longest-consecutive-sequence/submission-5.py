class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = {}
        res, currCount, currNum = 0, 0, 0
        for num in nums:
            numMap[num] = numMap.get(num, 0) + 1
        print(numMap)
        for i in range(len(nums)):
            if (nums[i] == 0 and nums[i] - 1) not in numMap or (nums[i] - 1) not in numMap:
                currCount = 0
                currNum = nums[i]
                print(nums[i])
                while currNum in numMap:
                    currCount += 1
                    currNum += 1
            res = max(res, currCount)
        return res
# c = 0
# p
# i
#[0, -1]
            
        