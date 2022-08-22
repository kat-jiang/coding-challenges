class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        res = []
        
        for start, end in intervals:
            if res == []:
                res.append([start, end])
                
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
                
        return res