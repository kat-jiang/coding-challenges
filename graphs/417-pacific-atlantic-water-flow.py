from typing import List

"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where 
heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells 
directly north, south, east, and west if the neighboring cell's height 
is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where 
result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) 
to both the Pacific and Atlantic oceans.

"""
# vist the rows that border the pacific ocean
# for each cell, check if it can flow to the pacific ocean
# meaning we are looking for cells that are greater or equal in height to the current cell
# save the cells that can flow to the pacific ocean in a set
# do the same for the atlantic ocean
# return the intersection of the two sets
# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid.
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prev_height):
            #base case:
            # if the row and col are out of bounds
            # if the cell is already visited
            # if the cell is lower than the previous cell means that water cannot flow down
            if ((r, c) in visit or
                r < 0 or c < 0 or r >= rows or c >= cols or
                heights[r][c] < prev_height):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for r in range(rows):
            # visit cells in the first column and last column for pacific and atlantic ocean
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        for c in range(cols):
            # visit cells in the first row and last row for pacific and atlantic ocean
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        return list(pacific & atlantic)

