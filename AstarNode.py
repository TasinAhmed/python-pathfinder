from Node import Node
from colors import *


class AstarNode(Node):
    def isClosed(self):
        # Check if node is closed
        return self.color == CLOSED_COLOR

    def isOpen(self):
        # Check if node is open
        return self.color == OPEN_COLOR

    def makeClosed(self):
        # Make node a closed node
        self.color = CLOSED_COLOR

    def makeOpen(self):
        # Make node a open node
        self.color = OPEN_COLOR

    def __lt__(self, other):
        # Check if a node is less than other
        return False
