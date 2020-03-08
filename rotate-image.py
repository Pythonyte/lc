https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        end = len(matrix) - 1
        
        n = len(matrix[0])        
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[end - j][i]
                matrix[end - j][i] = matrix[end - i][end -j]
                matrix[end - i][end- j] = matrix[j][end -i]
                matrix[j][end - i] = matrix[i][j]
                matrix[i][j] = tmp
