# import testmod for testing our function
from doctest import testmod
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    >>> twoSum([2,7,11,15], 9)
    [0, 1]
    >>> twoSum([3,3], 6)
    [0, 1]
    """
    for index, num in enumerate(nums):
        sum_dict={} # {num:index}
        diff = target - num
        if diff in sum_dict:
            return [sum_dict.get(diff), index]
        sum_dict[num] = index

    return []

#Runtime complexity: O(n)
#Spacetime complexity:O(n)


# call the testmod function
if __name__ == '__main__':
    testmod(name ='twoSum', verbose = True)