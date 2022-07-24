# 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
import sys
import numpy
import pygame
from constants import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(bgColor)


class BOARD:

    def __init__(self):
        self.place = numpy.zeros((rows, cols))
        self.empty_sqrs = self.place
        self.marked_sqrs = 0
        print(self.place)

    def final_states(self):

        # vertical wins
        for col in range(cols):
            if self.place[0][col] == self.place[1][col] == self.place[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.place[0][col]

        # horizontal wins
        for row in range(rows):
            if self.place[row][0] == self.place[row][1] == self.place[row][2] != 0:
                if show:
                    color = circleColor if self.place[row][0] == 2 else crossColor
                    iPos = (20, row * sqSize + sqSize // 2)
                    fPos = (width - 20, row * sqSize + sqSize // 2)
                    pygame.draw.line(screen, color, iPos, fPos, lineWidth)
                return self.place[row][0]

        # desc diagonal
        if self.place[0][0] == self.place[1][1] == self.place[2][2] != 0:
            if show:
                color = circleColor if self.place[1][1] == 2 else crossColor
                iPos = (20, 20)
                fPos = (width - 20, height - 20)
                pygame.draw.line(screen, color, iPos, fPos, lineWidth)
            return self.place[1][1]

    def mark_place(self, row, col, player):
        self.place[row][col] = player
        self.marked_sqrs += 1

    def isPlaceFree(self, row, col):
        return self.place[row][col] == 0

    def isFull(self):
        return self.marked_sqrs == 9

    def isEmpty(self):
        return self.marked_sqrs == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(rows):
            for col in range(cols):
                if self.isEmpty(row, col):
                    empty_sqrs.append(row, col)


class Game:

    def __init__(self):
        self.board = BOARD()
        self.show_lines()
        self.player = 1
        self.gamemode = 'ai'  # pvp or ai
        self.running = True



    def show_lines(self):
        # vetical lines
        pygame.draw.line(screen, lineColor, (sqSize, 0), (sqSize, height), lineWidth)
        pygame.draw.line(screen, lineColor, (width - sqSize, 0), (width - sqSize, height), lineWidth)
        # horizontal lines
        pygame.draw.line(screen, lineColor, (0, sqSize), (width, sqSize), lineWidth)
        pygame.draw.line(screen, lineColor, (0, height - sqSize), (width, height - sqSize), lineWidth)

    def draw_fig(self, row, col):
        if self.player == 1:
            # draw cross

            desStart = (col * sqSize + offSet, row * sqSize + offSet)
            desEnd = (col * sqSize + sqSize - offSet, row * sqSize + sqSize - offSet)
            pygame.draw.line(screen, crossColor, desStart, desEnd, lineWidth)

            enStart = (col * sqSize + offSet, row * sqSize + sqSize - offSet)
            enEnd = (col * sqSize + sqSize - offSet, row * sqSize + offSet)
            pygame.draw.line(screen, crossColor, enStart, enEnd, lineWidth)

            pass

        elif self.player == 2:
            # draw circle
            center = (col * sqSize + sqSize // 2, row * sqSize + sqSize // 2)
            pygame.draw.circle(screen, circleColor, center, radius, lineWidth)

    def NextPlayer(self):
        self.player = self.player % 2 + 1


class main:

    def loop(self):
        game = Game()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    row = pos[1] // sqSize
                    col = pos[0] // sqSize
                    if game.board.isPlaceFree(row, col):
                        game.board.mark_place(row, col, game.player)
                        game.draw_fig(row, col)
                        game.NextPlayer()
                        print(game.board.place)
            pygame.display.update()


l = main()
l.loop()
