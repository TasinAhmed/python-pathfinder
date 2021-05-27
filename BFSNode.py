from Node import Node
from colors import *


class BFSNode(Node):
    def __lt__(self, other):
        # Check if a node is less than other
        return False
