class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #{1: 1, 2: 2, 3: 3}
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = sorted(freq.items(), key= lambda x: x[1], reverse = True)
        
        for i in range(k):
            res.append(freq[i][0])
        return res
        
        

        
        