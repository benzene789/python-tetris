import pygame
import random

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
      return TetrisBlock(6,0,random.choice(all_shapes))