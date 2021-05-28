from queue import PriorityQueue
import math
from reconstructPath import reconstructPath
import pygame


def dijkstra(draw, grid, start, end):
    distance = {node: math.inf for row in grid for node in row}
    distance[start] = 0
    openNodes = PriorityQueue()
    openNodes.put((0, start))
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
            totalDist = distance[current] + 1

            if (
                not neighbor.isBarrier()
                and totalDist < distance[neighbor]
                and neighbor not in visited
            ):
                distance[neighbor] = totalDist
                prevNode[neighbor] = current
                openNodes.put((distance[neighbor], neighbor))
                # visitingNodesHash.add(neighbor)
                if neighbor != end:
                    neighbor.makeOpen()
        draw()

        visited.add(current)
        if current != start:
            current.makeClosed()

    return False
