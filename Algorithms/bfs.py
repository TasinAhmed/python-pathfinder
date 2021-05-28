from queue import PriorityQueue
import math
from reconstructPath import reconstructPath
import pygame


def bfs(draw, grid, start, end):
    count = 0
    openNodes = PriorityQueue()
    openNodes.put((count, start))
    prevNode = {}
    visited = set()

    while not openNodes.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = openNodes.get()[1]

        if current == end:
            reconstructPath(prevNode, current, start, draw)
            return True

        for neighbor in current.neighbors:
            if (
                not neighbor.isBarrier()
                and neighbor not in visited
                and not neighbor.isOpen()
            ):
                count += 1
                prevNode[neighbor] = current
                openNodes.put((count, neighbor))

                if neighbor != end:
                    neighbor.makeOpen()

        draw()

        visited.add(current)
        if current != start:
            current.makeClosed()

    return False
