class Solution:
    def uniquePathsRecursive(self, m: int, n: int) -> int:
        possible_paths = 0
        
        def explore(r,c):
            if r==m-1 and c==n-1:
                nonlocal possible_paths 
                possible_paths += 1
                return
            if not (0<=r<m and 0<=c<n):
                return
            explore(r+1,c) 
            explore(r,c+1)
        
        explore(0,0)
        return possible_paths
    
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[None for _ in range(n)] for _ in range(m)]
        
        for i in range(n):
            mem[0][i] = 1
        
        for i in range(m):
            mem[i][0] = 1
        
        for r in range(1,m):
            for c in range(1,n):
                mem[r][c] = mem[r-1][c] + mem[r][c-1]
        
        return mem[m-1][n-1]
    
        
        
