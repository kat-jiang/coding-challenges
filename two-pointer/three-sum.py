import unittest
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    >>> three_sum([-1,0,1,2,-1,-4])
    [[-1,-1,2], [-1,0,1]]
    >>> three_sum([])
    []
    >>> three_sum([0])
    [0]
    """
    #create list to catch results to return
    triplets_list = []

    #if len of nums < 3, cannot satisfy triplet conditions, so return empty list
    if len(nums) < 3:
        return triplets_list

    #sort nums so we can work l->r and r->l (O(nlogn) runtime)
    nums.sort()

    #iterate through nums and get target(-num)
    #do not want duplicate triplets so pass if current value is equal to previous index value (since this is sorted)
    #left pointer will increment to get to target
    #right pointer will decrement to get to target
    #while loop inside, breaks when l = r (nested loop -> O(n^2) runtime)
    #if target is reached, add to triplet list and increment left pointer
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue
        target = -num
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r -=1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                triplets_list.append([num, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return triplets_list


#Runtime complexity: O(n^2)
#Spacetime complexity:O(n)


class TestHandler(unittest.TestCase):
    def test_handler(self):
        self.assertEqual(three_sum([-1,0,1,2,-1,-4]), [[-1,-1,2], [-1,0,1]])
        self.assertEqual(three_sum([]), [])
        self.assertEqual(three_sum([0]), [])
        self.assertEqual(three_sum([0, 0, 0, 0]), [[0, 0, 0]])

testclass = unittest.main(exit=False)
if testclass.result.wasSuccessful():
    print("Test pass -- woohoo!")

def threeSum(nums):
    nums.sort()  # Sort the array
    result = []
    
    for i in range(len(nums) - 2):
        # Skip the same element to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:  # We found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move the pointers after finding a valid triplet
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # We need a larger sum, move the left pointer to the right
            else:
                right -= 1  # We need a smaller sum, move the right pointer to the left
    
    return result
