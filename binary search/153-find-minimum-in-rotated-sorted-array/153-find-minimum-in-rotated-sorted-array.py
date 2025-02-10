
# Approach:
# Identify the property of the rotated sorted array:
#   The minimum element is the pivot point where the rotation occurred.
#   The rightmost element is always greater than or equal to the minimum.
# Binary Search Strategy:
#   Set left = 0 and right = len(nums) - 1.
#   Find mid = (left + right) // 2.
#   If nums[mid] > nums[right], it means the minimum must be in the right half (move left = mid + 1).
#   Otherwise, the minimum is either at mid or in the left half (move right = mid).
#   Continue this process until left == right, which will point to the minimum element.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:  # Min must be in the right half
                left = mid + 1
            else:  # Min is at mid or in the left half
                right = mid
        
        return nums[left]  # or nums[right], since left == right at the end
                
# Time Complexity Analysis:
# O(log n) since we halve the search space in each step.
# O(1) space since we use only a few variables.