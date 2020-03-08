# https://leetcode.com/problems/design-tic-tac-toe/description/

class TicTacToe:
    """
    Record the number of moves for each rows, columns, and two diagonals.
    For each move, we -1 for each player 1's move and +1 for player 2's move.
    Then we just need to check whether any of the recored numbers equal to n or -n.
    """

    def __init__(self, n: int):
        """
        Initialize your data structure herplayere.
        """
        self.n = n
        
        # Ex.. offset: {Player1: -1, Player2: 1}
        self.offset = {1:-1, 2:1}
        
        # store count for all n rows 
        self.rows = [0]*n
        
        # store count for all n cols
        self.cols = [0]*n

        # store count for forword diagonal 
        self.diag = 0
        
        # store count for forword diagonal 
        self.anti_diag = 0
        
        # total moves for win in one specific row, specific col or specific diag
        self.max_moves = n
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        offset = self.offset.get(player)
        
        # Add count in row, where move has been made
        self.rows[row] += offset
        
        # Add count in col, where move has been made
        self.cols[col] += offset

        # Add count in forward diagonal, where move has been made
        if row == col:
            self.diag += offset
        
        # Add count in backword diagonal, where move has been made
        if row + col == self.n - 1 :
            self.anti_diag += offset
            
        # check if one specific row, specific col or specific diag got max_moves
        # or negative max_moves that means either player one or two wins
        count_for_all_directions = [self.rows[row], self.cols[col], self.diag, self.anti_diag]
        if -self.max_moves in count_for_all_directions:
            return 1
        elif self.max_moves in count_for_all_directions:
            return 2
        else:
            return 0
        
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
