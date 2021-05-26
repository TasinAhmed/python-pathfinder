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
        # Make node a path
        self.color == PATH_COLOR

    def draw(self, win):
        # Draw the node onto the window
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbors(self, grid):
        pass

    def __lt__(self, other):
        # Check if a node is less than other
        return False


# A* functions
def h(p1, p2):
    # Heuristic function
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# Grid functions
def makeGrid(rows, width):
    gap = width // rows
    grid = [[Node(i, j, gap, rows) for j in range(rows)] for i in range(rows)]

    return grid


def drawGrid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (i * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    drawGrid(win, rows, width)
    pygame.display.update()
