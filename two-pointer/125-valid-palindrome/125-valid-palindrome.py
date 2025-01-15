class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert to lowercase
        #remove spaces and non-alphanumeric chars
        #reverse the string and compare
        lowercase_string = s.lower()
        converted_string = ""
        for char in lowercase_string:
            if char.isalnum():
                converted_string += char

        return converted_string == converted_string[::-1]

# Time complexity: O(n)

# Two pointer approach

# convert to lowercase
# remove spaces and non-alphanumeric chars
# compare the first and last char using 2 pointers
# if they are not equal, return False
# increment left pointer and decrement right pointer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([char for char in s if char.isalnum()])
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] !=  s[r]:
                return False
            l += 1
            r -= 1
        
        return True