import pygame
import random

rows = 10
columns = 24

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

class TetrisBlock:
      def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.height = len(shape)
            self.width = len(shape[0])

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

def rotate_shape(shape_matrix, x, y):
      rotation = []
      # iterate through the width of the matrix
      for row in range(len(shape_matrix[0])):
            new_row = []
            # iterate through the height of the matrix  
            for column in range(len(shape_matrix)-1,-1,-1):
                  # create a new row
                  new_row.append(shape_matrix[column][row])
            # add each new row to the new rotation
            rotation.append(new_row)
      # return a new Tetrisblock object
      return TetrisBlock(x,y,rotation)

if __name__ == "__main__":
      game_running = True
      # set up board and get the initial shape
      first_shape = get_random_shape()
      print(first_shape.shape)
      board = create_board()
      print(rotate_shape(first_shape.shape, first_shape.x, first_shape.y).shape)
      # main game loop
      # while game_running:


