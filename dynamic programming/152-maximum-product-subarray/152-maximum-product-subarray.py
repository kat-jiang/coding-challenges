class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cur_max = nums[0]
        cur_min = nums[0]
        max_product = nums[0]

        for num in nums[1:]:
            temp = cur_max
            cur_max = max(num, cur_max * num, cur_min * num)
            cur_min = min(num, temp * num, cur_min * num)
            max_product = max(max_product, cur_max)

        return max_product