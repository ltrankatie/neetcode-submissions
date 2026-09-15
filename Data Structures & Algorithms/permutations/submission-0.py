class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base -> when curr == len(lens)
        #choices are digit in nums -> for num in nums
        
        res = []
        curr = []

        def backtracking():
            if len(curr) == len(nums):
                res.append(curr.copy())

            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                backtracking()
                curr.pop()
        backtracking()
        return res


        