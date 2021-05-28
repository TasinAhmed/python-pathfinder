from colors import *
import pygame


class Node:
    def __init__(self, row, col, width, totalRows):
        # Initialize node
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.totalRows = totalRows

    def getPos(self):
        # Get position of node
        return self.row, self.col

    def isBarrier(self):
        # Check if node is a barrier
        return self.color == BARRIER_COLOR

    def isStart(self):
        # Check if node is the start node
        return self.color == START_COLOR

    def isEnd(self):
        # Check if node if the end node
        return self.color == END_COLOR

    def isClosed(self):
        # Check if node is closed
        return self.color == CLOSED_COLOR

    def isOpen(self):
        # Check if node is open
        return self.color == OPEN_COLOR

    def reset(self):
        # Reset node color
        self.color = WHITE

    def makeBarrier(self):
        # Make node a barrier
        self.color = BARRIER_COLOR

    def makeStart(self):
        # Make node a start node
        self.color = START_COLOR

    def makeEnd(self):
        # Make node a end node
        self.color = END_COLOR

    def makeClosed(self):
        # Make node a closed node
        self.color = CLOSED_COLOR

    def makeOpen(self):
        # Make node a open node
        self.color = OPEN_COLOR

    def makePath(self):
        # Make node a path
        self.color = PATH_COLOR

    def draw(self, win):
        # Draw the node onto the window
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbors(self, grid):
        self.neighbors = []

        if (
            self.row < self.totalRows - 1
            and not grid[self.row + 1][self.col].isBarrier()
        ):
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if (
            self.col < self.totalRows - 1
            and not grid[self.row][self.col + 1].isBarrier()
        ):
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        # Check if a node is less than other
        return False
