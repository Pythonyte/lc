https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = range(len(matrix))
        cols = range(len(matrix[0]))
        
        for r in rows:
            for c in cols:
                if matrix[r][c] == 0:
                    matrix = self.mark_row(r, cols, matrix)
                    matrix = self.mark_col(c, rows, matrix)
        for r in rows:
            for c in cols:
                if matrix[r][c] == '#':
                    matrix[r][c] = 0
    
    def mark_row(self, r, cols, matrix):
        for c in cols:
            if matrix[r][c] != 0:
                matrix[r][c] = '#'
        return matrix
    
    def mark_col(self, c, rows, matrix):
        for r in rows:
            if matrix[r][c] != 0:
                matrix[r][c] = '#'
        return matrix
