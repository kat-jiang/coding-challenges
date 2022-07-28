class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        l = 0
        max_length = 0
        
        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[i])
            max_length =  max(max_length, len(substring))
        
        return max_length
        