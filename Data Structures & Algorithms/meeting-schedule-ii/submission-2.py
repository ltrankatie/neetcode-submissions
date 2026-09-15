"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #     ----
        #.         ----  
        #  ---------
        #. -------------------
        #               --   
        # < 0 5 10 15 20 25 30 35 40 >

        #if you have an overlapping interval, that means add another day
        #appending to a heap the endtimes
        #when you pop off you pop off the smallest end time
        #length of the heap represents number of meeting rooms required
                                       #curr
        # [[0, 15], [0, 30], [5, 10], [15,20], [21, 25]]
        #heap = [ 30]
        #count = 3

        intervals.sort(key = lambda x: x.start)
        heap = []
        count = 0
        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            count = max(count, len(heap))
        return count

        

        



