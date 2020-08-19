import pygame
import random

ROWS = 10
COLUMNS = 24

WIDTH = 500
HEIGHT = 500

OBlock = [["B","B"],
          ["B","B"]]
          
IBlock1 = [["B","B","B","B"]]

JBlock = [["B",".",".","."],
          ["B","B","B","B"]]

LBlock = [[".",".",".","B"],
          ["B","B","B","B"]]

SBlock = [[".","B","B"],
          ["B","B","."]]

ZBlock = [["B","B","."],
          [".","B","B"]]

TBlock = [[".","B","."],
          ["B","B","B"]]

all_shapes = [OBlock, IBlock1, ZBlock, SBlock, JBlock, LBlock, TBlock]

colours = ["", "blue", "green", "pink", "orange", "purple", "yellow", "red"]

class TetrisBlock:
      def __init__(self):
            self.x = 5
            self.y = 0
            self.block = random.choice(all_shapes)
            self.height = len(self.block)
            self.width = len(self.block[0])
            self.colour = random.randint(1, 7)


      def move_left(self, board):
            if self.valid_move(board, "left"):
                  # erase the shape from the board
                  remove_shape(board)
                  # move left
                  shape.x -= 1
      
      def move_right(self, board):
            if self.valid_move(board, "right"):
                  # erase shape from board
                  remove_shape(board)
                  # move right
                  shape.x += 1

      # Huge shout out to WilliamWFLee!, helped me on this function
      def valid_move(self, board, direction):
            valid_move = True
            # check if block is within the boundary of the board
            if direction == "right":
                  for y in range(self.height):  # Top-to-bottom
                        for x in range(self.width, -1, -1):  # Right-to-left
                              if self.block[y][x] == "B":
                                    if board[self.y][self.x + 1] != ".":
                                          valid_move = False
            else:
                  for y in range(self.height):  # Top-to-bottom
                        for x in range(self.width):  # left-to-right
                              if self.block[y][x] == "B":
                                    if board[self.y][self.x - 1] != ".":
                                          valid_move = False
            return valid_move


      # add the shape to the board by putting the colour in
      def add_shape(self, board):
            for col in range(self.height):
                  for row in range(self.width):
                        if board[col][row] == "B":
                              # add colour as integer
                              grid[self.y + col][self.x + row] = self.colour
      
      # remove the previous location of the shape
      def remove_shape(self, board):
            for col in range(self.height):
                  for row in range(self.width):
                        if board[col][row] == "B":
                              board[self.y + col][self.x + row] = "."
      
      # rotate the shape
      def rotate_shape(self, board):
            # perform a rotation
            rotation = []
            # iterate through the width of the matrix
            for row in range(self.width):
                  new_row = []
                  # iterate through the height of the matrix  
                  for column in range(len(self.block)-1,-1,-1):
                        # create a new row
                        new_row.append(self.block[column][row])
                  # add each new row to the new rotation
                  rotation.append(new_row)
            
            board_right = self.x + len(rotation[0])
            board_left = self.x - len(rotation[0])

            if (board_right < len(board[0])) and (board_left > len(board[0][0])):
                  self.block = rotation
                  self.width = len(self.block[0])
                  self.height = len(self.block)
      
      # check if there will be a collision between current block and row below
      def check_collision(self, board):
            collision = False
            # iterate through the shape
            for x in range(self.width):
                  if(self.block[self.height-1][x] =="B") and board[self.y + self.height][self.x + x] != ".":
                        # collision detected
                        collision = True
            return collision

class TetrisBoard:

      def __init__(self):
            self.board = self.create_board()
            self.score = 0

      # create the board
      def create_board(self):
            board=[] 
            for cols in range(COLUMNS): 
                  col = [] 
                  for row in range(ROWS): 
                        col.append('.')
                  board.append(col)
            return board

      # check if a row has been cleared
      def check_full_row(self):
            filled = True
            for y in range(COLUMNS):
                  for x in range(ROWS):
                        if self.board[y][x] == ".":
                              row  = x
                              filled = False
                  if filled:
                        for row in range(ROWS):
                              self.board[y][row] = "."
                        self.move_blocks_down()
                        self.score += 10

      # Call this function to move the row above
      # the cleared row down by one
      def move_blocks_down(self):
            for y in range(COLUMNS,0,-1):
                  for x in range(ROWS):
                        self.board[y][x] = self.board[y-1][x]
      
      # def check_game_over(self):
      #       full_board = False
      #       for x in range(ROWS):
      #             if self.board[0][x] != ".":
      #                   full_board = True
      #       return full_board
      
      def draw_board(self, display):
            left = -100
            top = 250
            for y in range(len(self.board)):
                  for x in range(len(self.board[0])):
                        draw_x = left + (x * 50)
                        draw_y = top - (y * 50)
                        colour = self.board[y][x]
                        
                        if colour == ".":
                              # colour in black
                              pygame.draw.rect(display, pygame.Color("#000000"), (draw_x, draw_y, 10, 10))
                              
                        else:
                              print(colours[colour])
                              # colour in specified colour
                              pygame.draw.rect(display, pygame.Color(colours[colour]), (draw_x, draw_y, 10, 10))

# Main game loop
if __name__ == "__main__":
      # set display
      display = pygame.display.set_mode((WIDTH, HEIGHT))
      block = TetrisBlock()
      game_board = TetrisBoard()
      game_board.board[block.y][block.x] = block.colour

      game_over = False
      while not game_over:
            collision_detected = False

            for event in pygame.event.get():

                  if event.type == pygame.QUIT:
                        raise SystemExit
                  elif event.type == pygame.KEYDOWN:
                        if event.key == K_RIGHT:
                              print("Right key pressed")
                              block.move_right(game_board.board)

                        elif event.key == K_LEFT:
                              print("Left key pressed")
                              block.move_left(game_board.board)
                        elif event.key == K_SPACE:
                              block.rotate_shape(game_board.board)

            # check for collision
            collision_detected = block.check_collision(game_board.board)
            if not collision_detected:
                  # remove shape
                  block.remove_shape(game_board.board)
                  block.y += 1
                  # redraw the shape
                  block.add_shape(game_board.board)
            # if a collision with the next row is detected, create a new shape
            else:
                  end_of_game = game_board.check_game_over()

            # if game_board.check_game_over():
            #       game_over = True
            #       print("Game over")
            #       print(game_board.score)
            # else:
            block = TetrisBlock()
            game_board.check_full_row()
            #print(game_board.board)
            # draw the board
            game_board.draw_board(display)
                  
