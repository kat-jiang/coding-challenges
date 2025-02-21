class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #rows, cols
        #visited set
        #iterate through grid, only do something if cell is a 1
        #recursion
        #basecase:
            #if out of bounds row <0 or row >= rows
            #col <0 or col>= rows
            #if water then perimeter increase by 1
        #if seen, skip
        #add to visited
        #recurse into top, bottom, left, right
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(row, col):
            if row < 0  or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0
            visited.add((row, col))
            
            perimeter = (dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1))
            return perimeter
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    return dfs(row, col)