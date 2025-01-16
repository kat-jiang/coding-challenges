# use 2 pointers left and right pointer to iterate through the string
# variable to save longest string count
# set to store seen letters
# if seen before, increment the left pointer, clear the set
# if letter not seen before, increment the right pointer
# ends when right pointer reaches end of string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left_p = 0
        max_length = 0

        for right_p in range(len(s)):
            while s[right_p] in seen:
                seen.remove(s[left_p])
                left_p += 1
            seen.add(s[right_p])
            max_length =  max(max_length, len(seen))
        
        return max_length
        