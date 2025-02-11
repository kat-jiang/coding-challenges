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
    
from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    left = 0  # Left pointer of the window
    max_len = 0  # Maximum length of the valid window
    char_count = defaultdict(int)  # Frequency of characters in the current window
    max_count = 0  # Most frequent character count in the window
    
    for right in range(len(s)):
        # Increment the count of the current character
        char_count[s[right]] += 1
        # Update the max_count, i.e., the count of the most frequent character
        max_count = max(max_count, char_count[s[right]])
        
        # If the window size minus the most frequent count is greater than k,
        # we need to shrink the window
        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1
        
        # Update the maximum length of the window
        max_len = max(max_len, right - left + 1)
    
    return max_len
