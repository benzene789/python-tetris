from tetris_info import TetrisInfo

import random
class TetrisBlock:
    def __init__(self, board):
        self.info = TetrisInfo()
        self.x = 5
        self.y = 0
        self.block = random.choice(self.info.all_shapes)
        self.height = len(self.block)
        self.width = len(self.block[0])
        self.colour = random.randint(1, 7)
        self.stored_board = board

    def move_left(self):
        if self.valid_move("left") and self.check_collision(-1, 0):
            # erase the shape from the board
            self.remove_shape()
            # move left
            self.x -= 1

    def move_right(self):
        if self.valid_move("right") and self.check_collision(1, 0):
            # erase shape from board
            self.remove_shape()
            # move right
            self.x += 1

    # Huge shout out to WilliamWFLee!, helped me on this function
    def valid_move(self, direction):

        valid_move = True
        # check if block is within the boundary of the board
        # when moving both left and right
        if direction == "right":
            # check withink bounds of the board (right side)
            if self.x + self.width < self.info.columns:
                for y in range(self.height):
                    if self.block[y][self.width-1] == "B":
                        if self.stored_board[self.y + y][self.x + self.width] != ".":
                            valid_move = False
            else:
                valid_move = False

        # check left
        else:
            # check withink bounds of the board (left side)
            if self.x > 0:
                for y in range(self.height):
                    if(self.block[y][self.width-1] == "B"):
                        if self.stored_board[self.y + y][self.x - self.width] != ".":
                            valid_move = False
            else:
                valid_move = False

        return valid_move

    # add the shape to the board by putting the colour in

    def add_shape(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.block[row][col] == "B":
                    if (self.y + row < self.info.rows and self.x + col < self.info.columns):
                        # add colour as integer
                        self.stored_board[self.y+row][self.x+col] = self.colour

    # remove the previous location of the shape
    def remove_shape(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.block[row][col] == "B":
                    if (self.y + row < self.info.rows and self.x + col < self.info.columns):
                        self.stored_board[self.y + row][self.x + col] = "."

    # rotate the shape
    def rotate_shape(self):
        # first remove the old shape
        self.remove_shape()
        # perform a rotation
        rotation = []
        # iterate through the width of the matrix
        for row in range(self.width):
            new_row = []
            # iterate through the height of the matrix
            for column in range(len(self.block)-1, -1, -1):
                # create a new row
                new_row.append(self.block[column][row])
            # add each new row to the new rotation
            rotation.append(new_row)

        board_right = self.x + len(rotation[0])
        
        if board_right <= len(self.stored_board[0]):
            if self.check_collision(1,0) and self.check_collision(-1,0):
                self.remove_shape()

                self.block = rotation
                self.width = len(self.block[0])
                self.height = len(self.block)

    # check if there will be a collision between current block and row below
    # Another huge shout out for WilliamWFLee, helped me on this function
    def check_collision(self, dx: int, dy: int):

        can_move = True
        self.remove_shape()  # Remove the shape from the board
        for y, row in enumerate(self.block):
            for x, square in enumerate(row):
                if square == "B":  # If the square is a part of the block
                    # If the end of the shape is at the end of the board then
                    # it will check out of range, so set dx to 0
                    if self.x+x+dx == self.info.columns:
                        dx = 0
                        
                    # If one of the blocks can't move in
                    # that direction, then the whole shape cannot move
                    if self.stored_board[self.y+y+dy][self.x+x+dx] != ".":
                        can_move = False
                        break

        self.add_shape()  # Place the shape back on the grid
        return can_move