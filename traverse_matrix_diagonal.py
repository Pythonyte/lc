class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix is None or matrix == []: return []
        res = []
        from collections import defaultdict 
        lines = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lines[i+j].append(matrix[i][j])
        for k in range(len(matrix) + len(matrix[0]) - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res
