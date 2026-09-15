class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        existing = set()
        l, max_count = 0, 0

        for r in range(len(s)):
            while s[r] in existing:
                existing.remove(s[l])
                l += 1
            existing.add(s[r])
            max_count = max(max_count, r - l + 1)
        return max_count