# import testmod for testing our function
from doctest import testmod
from typing import List

def max_subarray(nums: List[int]) -> int:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.

    >>> max_subarray([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> max_subarray([1])
    1
    >>> max_subarray([5,4,-1,7,8])
    23

    """
    if len(nums) == 0:
        return 0
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

#Runtime complexity: O(n)
#Spacetime complexity:O(n)

# call the testmod function
if __name__ == '__main__':
    testmod(name ='max_subarray', verbose = True)