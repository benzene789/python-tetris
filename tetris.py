import random
import pygame

COLUMNS = 10
ROWS = 24

WIDTH = 500
HEIGHT = 750

OBlock = [["B", "B"],
          ["B", "B"]]

IBlock1 = [["B", "B", "B", "B"]]

JBlock = [["B", ".", "."],
          ["B", "B", "B"]]

LBlock = [[".", ".", "B"],
          ["B", "B", "B"]]

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
            if self.x + self.width < COLUMNS:
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
                    if (self.y + row < ROWS and self.x + col < COLUMNS):
                        # add colour as integer
                        self.stored_board[self.y+row][self.x+col] = self.colour

    # remove the previous location of the shape
    def remove_shape(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.block[row][col] == "B":
                    if (self.y + row < ROWS and self.x + col < COLUMNS):
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
                    # If one of the blocks can't move in
                    # that direction, then the whole shape cannot move
                    if self.stored_board[self.y+y+dy][self.x+x+dx] != ".":
                        can_move = False
                        break

        self.add_shape()  # Place the shape back on the grid
        return can_move


class TetrisBoard:

    def __init__(self):
        self.board = self.create_board()
        self.score = 0
        self.level = 1
        self.current_lines_cleared = 0
        self.total_lines_cleared = 0

    # create the board
    def create_board(self):
        board = []
        for rows in range(ROWS):
            row = []
            for cols in range(COLUMNS):
                row.append('.')
            board.append(row)
        return board

    # see if you should advance to the next level
    def count_cleared_lines(self):
        while self.current_lines_cleared >= 5 * self.level:
            self.current_lines_cleared -= 5 * self.level
            self.level += 1

    def increase_score(self, cleared_lines):
        if cleared_lines == 1:
            self.score += 40 * self.level
        elif cleared_lines == 2:
            self.score += 100 * self.level
        elif cleared_lines == 3:
            self.score += 300 * self.level
        elif cleared_lines == 4:
            self.score += 1200 * self.level

    # check if a row has been cleared
    def check_full_row(self):
        # counts number of squares in each row
        # if the counter is equal to the amount of columns then
        # the row is full
        count = 0

        # lines cleared at a time
        lines_cleared_per_drop = 0

        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.board[y][x] != ".":
                    count += 1
            if count == COLUMNS:
                for col in range(COLUMNS):
                    self.board[y][col] = "."
                self.move_blocks_down(y)

                # increment amount of lines cleared
                self.current_lines_cleared += 1
                self.total_lines_cleared += 1
                lines_cleared_per_drop += 1

            count = 0
        self.increase_score(lines_cleared_per_drop)
        self.count_cleared_lines()
        lines_cleared_per_drop = 0

    # Call this function to move the row above
    # the cleared row down by one
    def move_blocks_down(self, row):
        for y in range(row, 0, -1):
            for x in range(COLUMNS):
                self.board[y][x] = self.board[y-1][x]

    def check_game_over(self, piece):
        if piece.y == 0:
            return True
        return False

    def draw_board(self, display):
        display.fill(pygame.Color("white"))

        pygame.font.init()
        left = 100
        top = 5
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                draw_x = left + (x * 25)
                draw_y = top + (y * 25)
                colour = self.board[y][x]

                if colour == ".":
                    # colour in black
                    pygame.draw.rect(display, pygame.Color(
                        "black"), (draw_x, draw_y, 25, 25))

                else:
                    # colour in specified colour
                    pygame.draw.rect(display, pygame.Color(
                        colours[colour]), (draw_x, draw_y, 25, 25))
                
                pygame.draw.rect(display, pygame.Color('grey'), (draw_x, draw_y, 25, 0))
                pygame.draw.rect(display, pygame.Color('grey'), (draw_x, draw_y, 0, 25))
        
        for i in range(len(self.board[0])):
            x = 100 + (i * 25)
            pygame.draw.rect(display, pygame.Color('black'), (x, 5, 25, 25))
            pygame.draw.rect(display, pygame.Color('grey'), (x, 5, 25, 0))
            pygame.draw.rect(display, pygame.Color('grey'), (x, 5, 0, 25))
        

        FONT = pygame.font.SysFont("Arial", 20)

        level_text = FONT.render("Level: "+f"{self.level}", True, pygame.Color("green"))

        display.blit(level_text, (400, 200))

        lines_cleared_text = FONT.render("Lines Cleared: "+f"{self.total_lines_cleared}", True, pygame.Color("red"))

        display.blit(lines_cleared_text, (375, 300))

        score_text = FONT.render("Score: "+f"{self.score}", True, pygame.Color("black"))

        display.blit(score_text, (400, 250))


class TetrisGame:
    
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_board = TetrisBoard()
        self.block = TetrisBlock(self.game_board.board)
        self.clock = pygame.time.Clock()
        self.fall_time = 0
        self.threshold = 500
        self.game_over = False

    def run_game(self):
        self.game_board.board[self.block.y][self.block.x] = self.block.colour

        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.block.move_right()
                    elif event.key == pygame.K_LEFT:
                        print("Left key pressed")
                        self.block.move_left()
                    elif event.key == pygame.K_SPACE:
                        self.block.rotate_shape()
                    # add the shape back
                    self.block.add_shape()

            self.fall_time += self.clock.tick()

            if self.fall_time > self.threshold:
                # check if the current piece is at the bottom
                if self.block.y == ROWS - self.block.height:
                    self.block = TetrisBlock(self.game_board.board)
                    self.game_board.check_full_row()

                # check for collision with next row
                elif self.block.check_collision(0, 1):
                    # remove shape
                    self.block.remove_shape()
                    self.block.y += 1
                    # redraw the shape
                    self.block.add_shape()

                else:
                    if self.game_board.check_game_over(self.block):
                        self.game_over = True

                    self.block = TetrisBlock(self.game_board.board)
                    self.game_board.check_full_row()

                self.fall_time %= self.threshold
            # draw the board
            self.game_board.draw_board(self.display)

            pygame.display.update()


# Main game loop
if __name__ == "__main__":
    tetris_game = TetrisGame()
    tetris_game.run_game()
