https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]) and board[r][c] == "O":
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"

                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r, c + 1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"

                    
########################################################################################
############################# Recursive Solution  ######################################
########################################################################################

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def explore(row, col):
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O":
                board[row][col] = "D"
                explore(row+1, col)
                explore(row-1, col)
                explore(row, col+1)
                explore(row, col-1)
                
                    
        
        # Put all zeros in queue which are in the borders
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row in [0, len(board)-1] or col in [0, len(board[0])-1]) and board[row][col] == "O":
                    explore(row, col)
        
              
        for row in range(len(board)):
            for col in range(len(board[0])):
                    if board[row][col] == "O":
                        board[row][col] = 'X'
        
                    if board[row][col] == "D":
                        board[row][col] = 'O'
        
        return board
