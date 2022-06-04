class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #make list into a set
        #get the length of set and length of list
        #compare lengths and return true if unequal
        
        return len(set(nums)) != len(nums)
        