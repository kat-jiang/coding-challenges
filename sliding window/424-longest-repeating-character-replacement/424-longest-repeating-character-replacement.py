# use 2 pointers for sliding window
# left pointer starts at 0 and right pointer will iterate through the array
# create a dictionary to store the count of each character
# iterate through the array and count the characters
# we can return longest repeating char string by getting the size of the window
# if the window size - max(count.values()) > k, we need to shrink the window

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #char:count
        res = 0
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
        
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        
        return res