import pygame
import random

rows = 10
columns = 24

OBlock = ['.....',
          '.....',
          '.BB..',
          '.BB..',
          '.....']

IBlock = [['..B..',
           '..B..',
           '..B..',
           '..B..',
           '.....'],
           ['.....',
            'BBBB.',
            '.....',
            '.....',
            '.....']
          ]

SBlock = [['.....',
          '.....',
          '..BB.',
          '.BB..',
          '.....'],
          ['.....',
          '..B..',
          '..BB.',
          '...B.']]

ZBlock = [['.....',
           '.....',
           '.BB..',
           '..BB.',
           '.....'],
          ['.....',
           '..B..',
           '.BB..',
           '.B...',
           '.....']]

JBlock = [['.....',
           '.B...',
           '.BBB.',
           '.....',
           '.....'],
          ['.....',
           '..BB.',
           '..B..',
           '..B..',
           '.....'],
          ['.....',
           '.....',
           '.BBB.',
           '...B.',
           '.....'],
          ['.....',
           '..B..',
           '..B..',
           '.BB..',
           '.....']]
 
LBlock = [['.....',
           '...B.',
           '.BBB.',
           '.....',
           '.....'],
          ['.....',
           '..B..',
           '..B..',
           '..BB.',
           '.....'],
          ['.....',
           '.....',
           '.BBB.',
           '.B...',
           '.....'],
          ['.....',
           '.BB..',
           '..B..',
           '..B..',
           '.....']]
 
TBlock = [['.....',
           '..B..',
           '.BBB.',
           '.....',
           '.....'],
          ['.....',
           '..B..',
           '..BB.',
           '..B..',
           '.....'],
          ['.....',
           '.....',
           '.BBB.',
           '..B..',
           '.....'],
          ['.....',
           '..B..',
           '.BB..',
           '..B..',
           '.....']]

all_shapes = [OBlock, IBlock, ZBlock, SBlock, JBlock, LBlock, TBlock]

class TetrisBlock:
      def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.rotation = 0

# get the next shape
def get_random_shape():
      return TetrisBlock(5,0,random.choice(all_shapes))

# return the initial board
def create_board():
      board=[] 
      for cols in range(columns): 
            col = [] 
            for row in range(rows): 
                  col.append('.') 
            board.append(col) 
      print(board) 
      return board

# move the shape left
def move_left(shape):
      if valid_move(shape, "left"):
            shape.x -= 1
      return shape

# move the shape right
def move_right(shape):
      if valid_move(shape, "right"):
            shape.x += 1
      return shape

# sees if the move is valid
def valid_move(shape, direction):
      valid = False
      if direction == "left" and shape.x > 0:
            valid = True
      elif direction == "right" and shape.x < rows:
            valid = True
      return valid

if __name__ == "__main__":
      game_running = True
      # set up board and get the initial shape
      first_shape = get_random_shape()
      board = create_board()
      
      # main game loop
      # while game_running:


