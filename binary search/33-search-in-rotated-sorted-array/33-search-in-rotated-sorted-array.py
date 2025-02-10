# Approach:
# Use binary search to find the target efficiently.
# Since the array is rotated, we first determine which half of the array is sorted (left or right).
# If the left half is sorted:
#   Check if the target lies within the left half.
#   If yes, search in the left half; otherwise, search in the right half.
# If the right half is sorted:
#   Check if the target lies within the right half.
#   If yes, search in the right half; otherwise, search in the left half.
# Repeat this process until the target is found or the search space is exhausted.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # Found target
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  # Target is in left half
                    right = mid - 1
                else:  # Target is in right half
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target is in right half
                    left = mid + 1
                else:  # Target is in left half
                    right = mid - 1
        
        return -1  # Target not found
    
# Time Complexity Analysis:
# Since we're using binary search, the time complexity is O(log n).
# Space complexity is O(1) since we're using constant extra space.