https://leetcode.com/problems/search-a-2d-matrix-ii/description/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix)-1 , 0
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            val = matrix[row][col]
            if target == val: return True
            elif target > val: col += 1
            elif target < val: row -= 1
                
        return False
    """
        starting from bottom left
        if target is small:
            go upwords (row - 1)
        if target is large:
            go straight (col + 1)
    
    """
