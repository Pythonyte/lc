class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        def containsCycleUtil(visited, r, c, p_r, p_c):
            if visited[r][c] == True:
                return True
            
            visited[r][c] = True
        
            valid_childs = [] 
            for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == grid[r][c] and (x,y) != (p_r,p_c):
                    valid_childs.append((x,y))

            for x,y in valid_childs:
                if containsCycleUtil(visited, x, y, r, c):
                    return True
        
        
        visited = [[False for _ in range(len(grid[0]))] for _ in grid]
        
        for r in range(len(grid)):  
            for c in range(len(grid[0])):
                if visited[r][c] == False:
                    if containsCycleUtil(visited, r, c, None, None):
                        return True
        return False
        
