from tetris_info import TetrisInfo

import pygame

class TetrisBoard:
    pygame.font.init()

    def __init__(self):
        self.info = TetrisInfo()
        self.board = self.create_board()
        self.score = 0
        self.level = 1
        self.current_lines_cleared = 0
        self.total_lines_cleared = 0

    # create the board
    def create_board(self):
        board = []
        for rows in range(self.info.rows):
            row = []
            for cols in range(self.info.columns):
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

        for y in range(self.info.rows):
            for x in range(self.info.columns):
                if self.board[y][x] != ".":
                    count += 1
            if count == self.info.columns:
                for col in range(self.info.columns):
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
            for x in range(self.info.columns):
                self.board[y][x] = self.board[y-1][x]

    def check_game_over(self, piece):
        if piece.y == 0:
            return True
        return False

    def draw_shape_info(self, next_shape, display, x, y):

        FONT = pygame.font.SysFont("Arial", 20)
        next_shape_text = FONT.render("Next shape: " , True, pygame.Color("red"))
        display.blit(next_shape_text, (x, y))
        
        for row in range(next_shape.height):
            for col in range(next_shape.width):
                if next_shape.block[row][col] == "B":
                    draw_x = x + (col * 25)
                    draw_y = (y + 25) + (row * 25)
                    # draw the block
                    pygame.draw.rect(display, pygame.Color(
                        self.info.colours[next_shape.colour]), (draw_x, draw_y, 25, 25))
                    pygame.draw.rect(display, pygame.Color('grey'), (draw_x, draw_y, 25, 0))
                    pygame.draw.rect(display, pygame.Color('grey'), (draw_x, draw_y, 0, 25))

    def draw_board(self, display, high_score):
        display.fill(pygame.Color("white"))

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
                        self.info.colours[colour]), (draw_x, draw_y, 25, 25))
                
                pygame.draw.rect(display, pygame.Color('grey'), (draw_x, draw_y, 25, 0))
                pygame.draw.rect(display, pygame.Color('grey'), (draw_x, draw_y, 0, 25))
        
        # stop the top from displaying a random sub block
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

        hs_text = FONT.render("High Score: "+f"{high_score}", True, pygame.Color("purple"))

        display.blit(hs_text, (140, 650))
        