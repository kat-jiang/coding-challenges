class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            #check if left portion is sorted
            if nums[l] <= nums[mid]:
                #if target not within left range, update l pointer
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                #if within left range, update r pointer
                else:
                    r = mid - 1
            #right portion
            else: 
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1