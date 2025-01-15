# convert nums into a set, since it does not matter if there are duplicates, we are only looking for consecutive numbers
# initialize a variable to keep track of the longest sequence
# iterate through the set, if the number - 1 is not in the set, then we know that this is the start of a sequence
# increment num by 1 and check if it is in set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        
        for num in nums:
            if (num - 1) not in hashset:
                curr_len = 1
                while (num + curr_len) in hashset:
                    curr_len += 1
                longest = max(curr_len, longest)
        
        return longest