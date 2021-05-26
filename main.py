import pygame
import math
from queue import PriorityQueue
from colors import *

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinder")


class Node:
    def __init__(self, row, col, width, total_rows):
        # Initialize node
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def getPos(self):
        # Get position of node
        return self.row, self.col

    def isClosed(self):
        # Check if node is closed
        return self.color == CLOSED_COLOR

    def isOpen(self):
        # Check if node is open
        return self.color == OPEN_COLOR

    def isBarrier(self):
        # Check if node is a barrier
        return self.color == BARRIER_COLOR

    def isStart(self):
        # Check if node is the start node
        return self.color == START_COLOR

    def isEnd(self):
        # Check if node if the end node
        return self.color == END_COLOR

    def reset(self):
        # Reset node color
        self.color == WHITE

    def makeClosed(self):
        # Make node a closed node
        self.color == CLOSED_COLOR

    def makeOpen(self):
        # Make node a open node
        self.color == OPEN_COLOR

    def makeBarrier(self):
        # Make node a barrier
        self.color == BARRIER_COLOR

    def makeStart(self):
        # Make node a start node
        self.color == START_COLOR

    def makeEnd(self):
        # Make node a end node
        self.color == END_COLOR

    def makePath(self):
        self.color == PATH_COLOR

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbors(self, grid):
        pass

    def __lt__(self, other):
        return False
