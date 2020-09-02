import pygame

from tetris_block import TetrisBlock
from tetris_board import TetrisBoard
from tetris_info import TetrisInfo

# class for running the game
class TetrisGame:
    
    def __init__(self):
        self.info = TetrisInfo()
        self.display = pygame.display.set_mode((self.info.width, self.info.height))
        self.game_board = TetrisBoard()
        self.block = TetrisBlock(self.game_board.board)
        self.clock = pygame.time.Clock()
        self.fall_time = 0
        self.threshold = 500
        self.game_over = False

    # run the game
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
            # increase fall time
            self.fall_time += self.clock.tick()

            if self.fall_time > self.threshold:
                # check if the current piece is at the bottom
                if self.block.y == self.info.rows - self.block.height:
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