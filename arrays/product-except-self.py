import unittest
from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    >>> product_except_self([1,2,3,4])
    [24,12,8,6]
    >>> product_except_self([-1,1,0,-3,3])
    [0,0,9,0,0]
    """

    #product list to return at the end
    products = [1] * len(nums)

    #variables declared to get product of nums iterating from left->right and from right-> left
    product_left = 1
    product_right = 1

    #iterate through nums from left->right
    #multiply product_left to get product at index i
    #increment product_left by multiplying value at index i
    for i in range(len(nums)):
        products[i] *= product_left
        product_left *= nums[i]

    #iterate thru nums from right->left (using reversed function)
    #multiply product_right to get product at index i
    #increment product_right by multiplying value at index i
    for i in reversed(range(len(nums))):
        products[i] *= product_right
        product_right *= nums[i]
    return products

#Runtime complexity: O(n)
#Spacetime complexity:O(n)


class TestHandler(unittest.TestCase):
    def test_handler(self):
        self.assertEqual(product_except_self([1,2,3,4]), [24,12,8,6])
        self.assertEqual(product_except_self([-1,1,0,-3,3]), [0,0,9,0,0])

testclass = unittest.main(exit=False)
if testclass.result.wasSuccessful():
    print("Test pass -- woohoo!")