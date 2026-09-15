class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use bucket sort solution
        #array count: index is the number of occurences,
        #value is the num in array that occurs that many times
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
        return res







       

        

        
        