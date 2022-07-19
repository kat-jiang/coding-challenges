class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num:count
        #create list to account for frequency - max frequency = len of list
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, ct in count.items():
            freq[ct].append(num)
            
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res