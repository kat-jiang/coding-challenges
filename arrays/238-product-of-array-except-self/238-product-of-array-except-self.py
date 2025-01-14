# since we cannot use division, we can calculate the product via 
# the product of all elements to the left and right of the current element
# create a return array of the same length as the input array, consisting of 1s
# iterate through the array, storing the product of all elements to the right of the current element
# iterate through the array in reverse, storing the product of all elements to the left of the current element
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        right_side = 1
        for i in range(len(nums)):
            res[i] = right_side
            right_side *= nums[i]

        left_side = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= left_side
            left_side *= nums[i]

        return res