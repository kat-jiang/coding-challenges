"""
242. Valid Anagram

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# use hashmap to store each character, store as char:frequency
# iterate through each string to add each char
# compare hashmaps at the end
# if hashmap is the same we return true
# otherwise false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        return s_dict == t_dict

# Time complexity: O(n + m) where n is the length of s and m is the length of t