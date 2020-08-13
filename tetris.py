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
      def __init__(self, x, y):
            self.x = x
            self.y = y
            self.block = random.choice(all_shapes)
            self.height = len(shape)
            self.width = len(shape[0])
            self.colour = random.randint(0, 6)

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
      
      def valid_move(self, board, direction):
            valid_move = True
            
            if direction == "left" and board[self.y][self.x - self.width - 1] != "." :
                  valid_move = False
            elif direction == "right" and board[self.y][self.x + self.width + 1] != ".":
                  valid_move = False

            return valid_move

      # add the shape to the board by putting the colour in
      def add_shape(self, board):
            for col in range(self.height):
                  for row in range(self.width):
                        if board[y][x] == "B":
                              # add colour as integer
                              grid[self.y + col][self.x + row] = self.colour
      
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




            


            

