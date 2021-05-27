from Node import Node


class DijkstraNode(Node):
    def __init__(self, row, col, width, totalRows, distance):
        super().__init__(row, col, width, totalRows)
        self.distance = distance

    def __lt__(self, other):
        return True if self.distance < other.distance else False
