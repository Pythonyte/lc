class Solution:
#     def numDistinctIslands_OLD(self, grid: List[List[int]]) -> int:
#         count = 0
        
#         def get_vertices(i,j):
#             directions = [(0,-1),(0,1),(1,0),(-1,0)]
#             for x,y in directions:
#                 r, c = x+i, y+j
#                 if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
#                     yield r,c
        
#         def dfs():
#             def dfs_util(r, c):
#                 for ir, ic in get_vertices(r, c):
#                     if grid[ir][ic] != 'Checked' and grid[ir][ic] != 0:
#                         grid[ir][ic] = 'Checked'
#                         dfs_util(ir, ic)
                        
#             rows, cols = range(len(grid)), range(len(grid[0]))
            
#             for r in rows:
#                 for c in cols:
#                     if grid[r][c] == 1:
#                         nonlocal count
#                         count += 1
#                         dfs_util(r, c)
        
#         dfs()
#         print(grid)
#         return count
    
    def numDistinctIslands(self, grid):
        seen = set()
        def explore(r, c, di = 0):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.append(di)
                explore(r+1, c, 1)
                explore(r-1, c, 2)
                explore(r, c+1, 3)
                explore(r, c-1, 4)
                shape.append(0)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = []
                explore(r, c)
                print(r,c,shape)
                if shape:
                    shapes.add(tuple(shape))

        return len(shapes)

    """
    (shape.add(0))
    Say we have shapes like

    A = [[1,0],
         [1,1]]
    B = [[1,1],
         [1,0]]
    Without shape.add(0), which records when we exit the function, these two shapes have the same path signature of [0, 1, 3]. This is because we don't know whether the east ("3") direction marked in the shape means east of the top left corner, or east of the bottom left corner.

    When we record exiting the function, they will have the signature [0, 1, 3, 0, 0, 0] and [0, 1, 0, 3, 0, 0] respectively. The 0 basically functioned as an "escape" or "backwards" move when describing the path - it says take the cursor that you have, and go back to the square you were on. We could interpret these path signatures as [SOUTH, EAST, ESCAPE, ESCAPE, ESCAPE], and [SOUTH, ESCAPE, EAST, ESCAPE, ESCAPE] if we wanted to reconstruct the path.
    """
