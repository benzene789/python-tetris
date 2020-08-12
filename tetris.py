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

colours = ["red", "blue", "green", "pink", "orange", "purple", "yellow"]

class TetrisBlock:
      def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.block = shape
            self.height = len(shape)
            self.width = len(shape[0])
            self.colour = random.randint(0, 6)

# get the next shape
def get_random_shape():
      return TetrisBlock(5,0,random.choice(all_shapes))

# return the initial board
def create_board(display):
      board=[] 
      for cols in range(COLUMNS): 
            col = [] 
            for row in range(ROWS): 
                  col.append('.')
                  pygame.draw.rect(display, pygame.Color("#000000"), ((WIDTH/2+row)-50,0+cols,WIDTH/10,HEIGHT/10))
            #pygame.draw.rect(display, pygame.Color('#000000'), (70+cols,20+row,10,10))
            board.append(col)
      return board

# move the shape left
def move_left(shape, board, display):
      if shape.x > 0 and board[shape.y][shape.x -1] == ".":
            # erase the shape from the board
            # remove_shape(board, display)
            shape.x -= 1

def move_right(shape, board, display):
      if shape.x < (COLUMNS - shape.width) and board[shape.y][shape.x +1] == ".":
            # erase shape from board
            # remove_shape(board, display)
            shape.x += 1

def remove_shape(board, display, shape):
      for col in range(shape.height):
            for row in range(shape.width):
                  if shape.block[col][row] == "B":
                        board[shape.y + col][shape.x + row] = "."
                        pygame.draw.rect(display, pygame.Color("#000000"), shape.x+row, shape.y+col)

def draw_shape(board, display, shape):
      for col in range(shape.height):
            for row in range(shape.width):
                  if shape.block[col][row] == "B":
                        board[shape.y + col][shape.x + row] = shape.colour
                        colour = colours[shape.colour]
                        pygame.draw.rect(display, pygame.Color(colour), shape.x+row, shape.y+col)



def rotate_shape(block):
      rotation = []
      # iterate through the width of the matrix
      for row in range(block.width):
            new_row = []
            # iterate through the height of the matrix  
            for column in range(len(block.shape)-1,-1,-1):
                  # create a new row
                  new_row.append(block.shape[column][row])
            # add each new row to the new rotation
            rotation.append(new_row)
      # return a new Tetrisblock object
      return TetrisBlock(block.x,block.y,rotation)

if __name__ == "__main__":
      pygame.init()
      
      WINDOW_SIZE = (WIDTH,HEIGHT)
      display = pygame.display.set_mode(WINDOW_SIZE)
      display.fill((255,255,255))

      running = True
      while running:
            for event in pygame.event.get():
                  # Deal with events here
                  if running:
                        # Draw/blit onto the display surface
                        pygame.display.update()
                        create_board(display)
      pygame.quit()


      '''game_running = True
      # set up board and get the initial shape
      first_shape = get_random_shape()
      print(first_shape.shape)
      board = create_board()
      print(board)
      a = rotate_shape(first_shape)
      print(a.shape)
      print(rotate_shape(a).shape)
      # main game loop
      # while game_running:'''


