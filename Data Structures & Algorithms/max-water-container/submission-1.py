class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l <= r:
            area = (r - l) * min(heights[l], heights[r])
            print(l, r, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, area)
        return max_area
        # area = 7 max_area = 7 
        #     l                 r 
        # [1, 7, 2, 5, 4, 7, 3, 6]
        #  0. 1. 2. 3. 4. 5. 6. 7