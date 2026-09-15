class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #     ---
        #   ---
        # < 1 2 3 4 5 6 7 >
        # to check, if the start of one interval is less than the end of another interval

        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]
        
        #starts looking through intervals except for first one
        for start, end in intervals[1:]:
            #output[-1] gets the entry from the most recently added interval
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output







