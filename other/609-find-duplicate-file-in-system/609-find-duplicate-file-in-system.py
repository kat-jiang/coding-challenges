from collections import defaultdict

class Solution:
    
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        res = []
        
        for p in paths:
            
            path = p.split()
            directory, files = path[0], path[1:]
            
            for file in files:
                
                f = file.split('(')
                filename, content = f[0], f[1][:-1]
                
                hashmap[content].append(f"{directory}/{filename}")
             
        for lst in hashmap.values():
            if len(lst) > 1:
                res.append(lst)
                
        return res