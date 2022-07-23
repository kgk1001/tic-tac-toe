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
        print(self.place)

    def mark_place(self, row, col, player):
        self.place[row][col] = player

    def IsPlaceFree(self, row, col):
        return self.place[row][col] == 0


class Game:

    def __init__(self):
        self.board = BOARD()
        self.show_lines()
        self.player = 1

    def show_lines(self):
        # vetical lines
        pygame.draw.line(screen, lineColor, (sqSize, 0), (sqSize, height), lineWidth)
        pygame.draw.line(screen, lineColor, (width - sqSize, 0), (width - sqSize, height), lineWidth)
        # horizontal lines
        pygame.draw.line(screen, lineColor, (0, sqSize), (width, sqSize), lineWidth)
        pygame.draw.line(screen, lineColor, (0, height - sqSize), (width, height - sqSize), lineWidth)

    def NextPlayer(self):
        self.player = self.player % 2 +1

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
                    if game.board.IsPlaceFree(row, col):
                        game.board.mark_place(row, col, game.player)
                        game.NextPlayer()
                        print(game.board.place)
            pygame.display.update()


l = main()
l.loop()
