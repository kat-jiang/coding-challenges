class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_num = nums[0]
        max_num = nums[-1]
        
        if target > max_num:
            return -1
        elif target < min_num:
            return -1
        
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif num > target:
                return -1
        
        return -1
        