import pygame

from .block import Block
from .board import Board
from .info import Info

# class for running the game
class Game:
    
    def __init__(self):
        self.high_score = self.current_high_score()
        self.info = Info()
        self.display = pygame.display.set_mode((self.info.width, self.info.height))
        self.game_board = Board()
        self.block = Block(self.game_board.board)
        self.clock = pygame.time.Clock()
        self.fall_time = 0
        self.threshold = 1000 * (0.8 - (self.game_board.level-1)*0.007)**(self.game_board.level-1)
        self.game_over = False
        self.held_shape = None
        self.soft_speed = self.threshold * 0.5
        # placeholder for threshold 
        # needed for setting threshold back after soft drop
        self.current_threshold = self.threshold

    # write the high score to the file
    def write_high_score(self):
        with open('tetris_high_score.txt', 'w') as file:
            score = file.write(str(self.game_board.score))

    # get the current high score from the file
    def current_high_score(self):
        pygame.font.init()
        # try open it
        try:
            with open('tetris_high_score.txt') as file:
                return int(file.read())
        except:
            print('Problem reading file...')
            # If the file doesn't exist or contains nothing then
            # highscore = 0
            return 0

    # create new block function
    def new_block(self):
        return Block(self.game_board.board)

    # create hold block function
    def hold_shape(self, shape):
        self.block.remove_shape()
        self.held_shape = shape
    
    # run the game
    def run_game(self):
        next_block = self.new_block()

        while not self.game_over:
            hold = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.block.move_right()
                    elif event.key == pygame.K_LEFT:
                        self.block.move_left()
                    elif event.key == pygame.K_SPACE:
                        self.block.rotate_shape()
                    elif event.key == pygame.K_DOWN:
                        self.block.y = self.block.hard_drop()
                    elif event.key == pygame.K_UP:
                        # check if no shapes are currently held
                        if self.held_shape is None:
                            # hold the shape
                            hold = True
                            self.hold_shape(self.block)
                        else:
                            self.block.remove_shape()
                            self.block = self.held_shape
                            self.block.y = 0
                            # set back to none
                            self.held_shape = None
                        break
                    # soft drop
                    elif event.key == pygame.K_s:

                        self.threshold = self.soft_speed

                    # add the shape back
                    self.block.add_shape()

            # terminate the program
            if self.game_over:
                break

            # increase fall time
            self.fall_time += self.clock.tick()

            if self.fall_time > self.threshold:
                
                # check if the current piece is at the bottom
                if self.block.y == self.info.rows - self.block.height:                     
                    self.block = next_block
                    self.game_board.check_full_row()
                    # Set up the next block
                    next_block = self.new_block()                    

                # check for collision with next row
                elif self.block.check_collision(0, 1):
                    # end the soft drop
                    self.threshold = self.current_threshold
                    # remove shape
                    self.block.remove_shape()
                    self.block.y += 1
                    # redraw the shape
                    self.block.add_shape()
                    

                else:
                    if self.game_board.check_game_over(self.block):
                        self.game_over = True

                    self.block = next_block
                    self.game_board.check_full_row()
                    next_block = self.new_block()
                    

                self.fall_time %= self.threshold
            
            # hold the block
            if hold:
                self.block = next_block
                self.block.y = 0
                # get the next block
                next_block = self.new_block()
                continue
                
            # draw the board
            self.game_board.draw_board(self.display, self.high_score)
            # draw held block
            self.game_board.draw_shape_info(self.held_shape, self.display, 400, 5, "Held shape: ")
            # draw the next block
            self.game_board.draw_shape_info(next_block, self.display, 1, 5, "Next shape: ")

            pygame.display.update()

        # save score to a file
        if self.game_board.score > self.high_score:
            self.write_high_score()