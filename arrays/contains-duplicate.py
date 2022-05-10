# import testmod for testing our function
from doctest import testmod
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    >>> contains_duplicate([1,2,3,1])
    True
    >>> contains_duplicate([1,2,3,4])
    False
    >>> contains_duplicate([1,1,1,3,3,4,3,2,4,2])
    True
    """

    duplicate_dict = {}

    for num in nums:
        if duplicate_dict.get(num):
            return True
        duplicate_dict[num] = duplicate_dict.get(num, 0) + 1

    return False

#Runtime complexity: O(n)
#Spacetime complexity:O(n)

# call the testmod function
if __name__ == '__main__':
    testmod(name ='max_profit', verbose = True)