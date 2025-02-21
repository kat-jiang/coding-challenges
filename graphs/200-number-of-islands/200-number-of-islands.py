class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(row, col):
            # check if row and col are in bounds before assessing grid[row][col]
            # indices go from 0 to rows-1 and 0 to cols-1, so it is row >= rows or col >= cols
            # and not row > rows or col > cols
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0' or (row, col) in visited:
                return
            
            visited.add((row, col))
            
            dfs(row-1, col) #top
            dfs(row+1, col) #bottom
            dfs(row, col-1) #left
            dfs(row, col+1) #right
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)
                    
        return islands
    

# Time Complexity: 
# O(m * n) where m is the number of rows and n is the number of columns in the grid.
# Space Complexity:
# O(m * n) for the visited set in the worst case where all cells are land.