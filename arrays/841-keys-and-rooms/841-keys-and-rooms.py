from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        queue = deque()
        queue.append(0)
        
        while queue:
            
            room_num = queue.popleft()
            
            if room_num not in visited:
                keys = rooms[room_num]
                
                queue.extend(keys)
                
                visited.add(room_num)
                
        if len(visited) == len(rooms):
            return True
        
        return False
                
            