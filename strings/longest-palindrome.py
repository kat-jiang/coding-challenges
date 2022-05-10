import unittest
from typing import List

def longest_palindrome(s: str) -> str:
    """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    >>> longest_palindrome("babad")
    "bab"
    >>> longest_palindrome("cbbd")
    "bb"
    """
    #variables to track longest palindrome and substrings
    longest_palindrome = ""
    substring = ""

    #initialize length of palindrome and index at 0
    len_palindrome = 0
    i = 0

    #iterate through string
    #add chars to substring
    #check if substring is palindrome and > in length than current palindrome
    #if so set longest palindrome to substring and update the length of palindrome
    #increment i
    #reset substring to empty string
    #while loop breaks when remaining chars in string is < than len of current longest palindrome
    while len(s)-i > len_palindrome:
        for index in range(i, len(s)):
            substring += s[index]
            if substring[::-1] ==  substring and len(substring) > len_palindrome:
                longest_palindrome = substring
                len_palindrome = len(longest_palindrome)
        i += 1
        substring = ""

    return longest_palindrome

#Runtime complexity: O(n^3?)
#Spacetime complexity:O(n)


class TestHandler(unittest.TestCase):
    def test_handler(self):
        self.assertEqual(longest_palindrome("babad"), "bab")
        self.assertEqual(longest_palindrome("cbbd"), "bb")
        self.assertEqual(longest_palindrome("baddabc"), "baddab")

testclass = unittest.main(exit=False)
if testclass.result.wasSuccessful():
    print("Test pass -- woohoo!")