#iterate through nums and store in hashmap {int:count}
#get hashmap keys and values, sort by values, descending
#return k elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        res = []
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        sorted_nums_count = sorted(nums_count.items(), key = lambda item:item[1], reverse=True)
        for i in range(k):
            res.append(sorted_nums_count[i][0])
        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num:count
        # create list to account for frequency
        # max frequency = len of list
        # index = frequency, value = list of nums
        # need len(nums) + 1 because frequency starts at 0 even tho that frequency will be empty
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