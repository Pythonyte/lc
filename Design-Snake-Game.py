"""
https://leetcode.com/problems/design-snake-game/description/
https://leetcode.com/problems/design-snake-game/discuss/82681/Straightforward-Python-solution-using-deque
"""
class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        from collections import deque
        # snake head is at the front
        # snake will contain all the coordinates where snake body exists (in-order)
        # == in board will be deque([[0,1],[0,0]]) as head of snake is at 0,1   
        self.snake = deque([[0, 0]])

        self.width = width
        self.height = height

        self.food = deque(food)
        self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def get_new_head(self, direction):
        curr_head = self.snake[0]
        possible_new_head = [
            curr_head[0] + self.direct[direction][0],
            curr_head[1] + self.direct[direction][1]
        ]
        return possible_new_head

    def invalid_location(self, possible_new_head):
        """
        Possible new heasd can be invalid and make game over if
            next row does not exist (reaches boundary)
            next col does not exist (reaches boundary)
            next row col is already part of snake body, but not the snake tail...
            because, it is possible that snake is moving to its tail and that can be made,
            because it will shift by 1, so prev tail will be valid place 
        """
        invalid_row = (possible_new_head[0] < 0 or possible_new_head[0] >= self.height)
        invalid_col = (possible_new_head[1] < 0 or possible_new_head[1] >= self.width)
        new_head_in_snake_body = (
            # notice that the possible_new_head can be equal to self.snake[-1]  
            possible_new_head in self.snake and possible_new_head != self.snake[-1]
        )
        return invalid_row or invalid_col or new_head_in_snake_body
    
    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        possible_new_head = self.get_new_head(direction)
        if self.invalid_location(possible_new_head): return -1

        # eat food if new head is at food location
        if self.food and self.food[0] == possible_new_head:
            # Add new head in snake, becoming snake body
            self.snake.appendleft(possible_new_head)  
            # remove that food, as its eaten and never come again
            self.food.popleft()
        else:
            # not eating food: append head and delete tail                 
            self.snake.appendleft(possible_new_head)
            self.snake.pop()
        
        # Score will be: total length of snake, beacuse snake length is getting increase
        # only when food is eaten
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
