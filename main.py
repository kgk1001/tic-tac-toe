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


class GAME:

    def __init__(self):
        self.board = BOARD()
        self.show_lines()
        self.player = 1

    @staticmethod
    def show_lines():
        # vetical lines
        pygame.draw.line(screen, lineColor, (sqSize, 0), (sqSize, height), lineWidth)
        pygame.draw.line(screen, lineColor, (width - sqSize, 0), (width - sqSize, height), lineWidth)
        # horizontal lines
        pygame.draw.line(screen, lineColor, (0, sqSize), (width, sqSize), lineWidth)
        pygame.draw.line(screen, lineColor, (0, height - sqSize), (width, height - sqSize), lineWidth)


def main():
    g = GAME()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // sqSize
                col = pos[0] // sqSize
                GAME.board.mark_place(row, col, 1)
                
        pygame.display.update()


main()
