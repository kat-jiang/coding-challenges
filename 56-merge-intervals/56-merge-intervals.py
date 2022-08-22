class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        
        for start, end in sorted_intervals:
            if res == []:
                res.append([start, end])
            if start <= res[-1][1]:
                res[-1][1] = end if end > res[-1][1] else res[-1][1]
            else:
                res.append([start, end])
                
        return res