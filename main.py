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


class board:

    def __init__(self):
        self.place = numpy.zeros((3, 3))
        print(self.place)


class game:

    def __init__(self):
        self.board = board()
        self.show_lines()

    def show_lines(self):
        # vetical lines
        pygame.draw.line(screen, lineColor, (sqSize, 0), (sqSize, height), lineWidth)
        pygame.draw.line(screen, lineColor, (width - sqSize, 0), (width - sqSize, height), lineWidth)
        # horizontal lines
        pygame.draw.line(screen, lineColor, (0, sqSize), (width, sqSize), lineWidth)
        pygame.draw.line(screen, lineColor, (0, height - sqSize), (width, height - sqSize), lineWidth)


def main():
    g = game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()
