import unittest
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    >>> two_sum([2,7,11,15], 9)
    [0, 1]
    >>> two_sum([3,3], 6)
    [0, 1]
    """
    sum_dict = {} # {num:index}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in sum_dict:
            return [sum_dict[diff], index]
        sum_dict[num] = index

    return []

#Runtime complexity: O(n)
#Spacetime complexity:O(n)

class TestHandler(unittest.TestCase):
    def test_handler(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

testclass = unittest.main(exit=False)
if testclass.result.wasSuccessful():
    print("Test pass -- woohoo!")