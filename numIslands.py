class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = {}
        
        def get_valid_edges(row, col):
            rows = [0,0,-1,1]
            cols = [-1,1,0,0]
            edges = []
            for i in range(len(rows)):
                ri = row + rows[i]
                ci = col + cols[i]
                # Valid edges are only those, which are
                # not yet checked
                # not having 0
                # must be in grid
                if 0 <= ri < len(grid) and 0 <= ci < len(grid[0]) and grid[ri][ci] == '1' and (ri, ci) not in visited:
                    yield (ri,ci)
        
        def dfs(row, col):
            nonlocal visited
            visited[(row, col)] = True  
            for r,c in get_valid_edges(row, col):
                if (r, c) not in visited:
                    dfs(r,c)

        
        def count_islands():
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if (row, col) not in visited and grid[row][col] == '1':
                        nonlocal islands
                        islands += 1
                        dfs(row, col)
        

            
        count_islands()
        
        return islands

  
# Improved Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def dfs():
            def explore(r, c):
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 'T' and grid[r][c] != '0':
                        grid[r][c] = 'T'
                        explore(r+1, c)
                        explore(r-1, c)
                        explore(r, c+1)
                        explore(r, c-1)

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == '1':
                        nonlocal count
                        count += 1
                        explore(r, c)
        
        dfs()
        print(grid)
        return count
