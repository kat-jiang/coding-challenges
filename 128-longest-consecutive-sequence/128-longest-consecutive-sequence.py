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