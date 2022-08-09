class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                for i in row:
                    if i == target:
                        return True
                    elif i > target:
                        return False
            elif row[0] > target:
                return False