class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search
        #get len of rows and cols
        #get mid point 
        #work on rows first
        #if target > last num in row, increase row
        #if target < first num in row, decrease row
        #else target in row
        #work on cols next, l and r
        #get mid point - if target > mid, increment l
        #if target < mid, decrease r
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bottom = 0, ROWS - 1
        
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom =  mid - 1
            else:
                break
        #while loop breaks naturally meaning target not within any of the rows
        else:
            return False
        
        l, r = 0, COLS - 1
        cur_row = (top + bottom) // 2
        while l <= r:
            mid = (l + r) //2
            if target > matrix[cur_row][mid]:
                l = mid + 1
            elif target < matrix[cur_row][mid]:
                r = mid - 1
            else:
                return True
            
        return False