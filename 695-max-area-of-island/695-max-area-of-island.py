class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited.add((row, col))
            
            area = 1
            area += dfs(row-1, col) #top
            area += dfs(row+1, col) #bottom
            area += dfs(row, col-1) #left
            area += dfs(row, col+1) #right
            
            return area
        
        for row in range(rows):
            for col in range(cols):
                area = dfs(row, col)
                max_area = max(area, max_area)
                
        return max_area