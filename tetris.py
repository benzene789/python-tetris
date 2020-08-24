import pygame
import random

COLUMNS = 10
ROWS = 24

WIDTH = 1550
HEIGHT = 1550

OBlock = [["B", "B"],
          ["B", "B"]]

IBlock1 = [["B", "B", "B", "B"]]

JBlock = [["B", ".", ".", "."],
          ["B", "B", "B", "B"]]

LBlock = [[".", ".", ".", "B"],
          ["B", "B", "B", "B"]]

SBlock = [[".", "B", "B"],
          ["B", "B", "."]]

ZBlock = [["B", "B", "."],
          [".", "B", "B"]]

TBlock = [[".", "B", "."],
          ["B", "B", "B"]]

all_shapes = [OBlock, IBlock1, ZBlock, SBlock, JBlock, LBlock, TBlock]

colours = ["", "blue", "green", "pink", "orange", "purple", "yellow", "red"]


class TetrisBlock:
    def __init__(self, board):
        self.x = 5
        self.y = 0
        self.block = random.choice(all_shapes)
        self.height = len(self.block)
        self.width = len(self.block[0])
        self.colour = random.randint(1, 7)

        self.stored_board = board

    def move_left(self):
        if self.valid_move("left"):
            # erase the shape from the board
            self.remove_shape()
            # move left
            self.x -= 1
            block.add_shape()

    def move_right(self):
        if self.valid_move("right"):
            print("F")
            # erase shape from board
            self.remove_shape()
            # move right
            self.x += 1
            block.add_shape()
        else:
            print("Dhfg")

            self.x = self.x

    # Huge shout out to WilliamWFLee!, helped me on this function
    def valid_move(self, direction):

        valid_move = True
        # check if block is within the boundary of the board
        # when moving both left and right
        if direction == "right":
            print(self.x + self.width)
            if self.x + self.width < COLUMNS:

                for y in range(self.height):
                  if(self.block[y][self.width-1] == "B") and self.stored_board[self.y + y][self.x + self.width] != ".":
                        valid_move = False
            else:
                  valid_move = False
                  

        else:
            if self.x > 0:
                for y in range(self.height):
                  if(self.block[y][self.width-1] == "B") and self.stored_board[self.y + y][self.x - self.width] != ".":
                        valid_move = False
            else:
                valid_move = False

        return valid_move

    # add the shape to the board by putting the colour in

    def add_shape(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.block[row][col] == "B" and (self.y + row < ROWS and self.x + col < COLUMNS):
                    # add colour as integer
                    self.stored_board[self.y + row][self.x + col] = self.colour

    # remove the previous location of the shape
    def remove_shape(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.block[row][col] == "B" and (self.y + row < ROWS and self.x + col < COLUMNS):
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

        if board_right < len(self.stored_board[0]):
            self.block = rotation
            self.width = len(self.block[0])
            self.height = len(self.block)

        block.add_shape()

    # check if there will be a collision between current block and row below
    def check_collision(self):
        collision = False
        # iterate through the shape
        for x in range(self.width):
            if self.y + self.height < ROWS:
                if(self.block[self.height-1][x] == "B") and self.stored_board[self.y + self.height][self.x + x] != ".":
                    # collision detected
                    collision = True
        return collision


class TetrisBoard:

    def __init__(self):
        self.board = self.create_board()
        self.score = 0

    # create the board
    def create_board(self):
        board = []
        for rows in range(ROWS):
            row = []
            for cols in range(COLUMNS):
                row.append('.')
            board.append(row)
        return board

    # check if a row has been cleared
    def check_full_row(self):
        count = 0
        filled = True
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.board[y][x] != ".":
                    count += 1
            if count == COLUMNS:
                for col in range(COLUMNS):
                    self.board[y][col] = "."
                self.move_blocks_down()
                self.score += 10
            count = 0

    # Call this function to move the row above
    # the cleared row down by one
    def move_blocks_down(self):
        for y in range(ROWS-1, 0, -1):
            for x in range(COLUMNS):
                self.board[y][x] = self.board[y-1][x]

    # def check_game_over(self):
    #       full_board = False
    #       for x in range(ROWS):
    #             if self.board[0][x] != ".":
    #                   full_board = True
    #       return full_board

    def draw_board(self, display):
        left = 0
        top = 0
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                draw_x = left + (x * 25)
                draw_y = top + (y * 25)
                colour = self.board[y][x]

                if colour == ".":
                    # colour in black
                    pygame.draw.rect(display, pygame.Color(
                        "#FFFFFF"), (draw_x, draw_y, 25, 25))

                else:
                    # colour in specified colour
                    pygame.draw.rect(display, pygame.Color(
                        colours[colour]), (draw_x, draw_y, 25, 25))


# Main game loop
if __name__ == "__main__":
    # set display
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    game_board = TetrisBoard()
    block = TetrisBlock(game_board.board)

    game_board.board[block.y][block.x] = block.colour

    clock = pygame.time.Clock()

    fall_time = 0
    threshold = 1000

    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("Right key pressed")
                    block.move_right()
                elif event.key == pygame.K_LEFT:
                    print("Left key pressed")
                    block.move_left()
                elif event.key == pygame.K_SPACE:
                    block.rotate_shape()

        # keep track of how much time has elapsed
        fall_time += clock.tick()

        if fall_time > threshold:
            # check if the current piece is at the bottom
            if block.y == ROWS - block.height:
                block = TetrisBlock(game_board.board)
                game_board.check_full_row()

            # check for collision with next row
            elif not block.check_collision():
                # remove shape
                block.remove_shape()
                block.y += 1
                # redraw the shape
                block.add_shape()

            else:
                block = TetrisBlock(game_board.board)
                game_board.check_full_row()

            fall_time %= threshold
            # draw the board
        game_board.draw_board(display)

        pygame.display.update()
