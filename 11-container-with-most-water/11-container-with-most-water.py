class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            min_height = min(height[l], height[r])
            width = r - l
            cur_water = min_height * width
            max_water = max(max_water, cur_water)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return max_water   