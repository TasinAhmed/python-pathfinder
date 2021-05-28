from queue import PriorityQueue
import math
from reconstructPath import reconstructPath
import pygame


def h(p1, p2):
    # Heuristic function
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def astar(draw, grid, start, end):
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))
    prevNode = {}
    gScore = {node: math.inf for row in grid for node in row}
    gScore[start] = 0
    fScore = {node: math.inf for row in grid for node in row}
    fScore[start] = h(start.getPos(), end.getPos())
    openSetHash = {start}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = openSet.get()[2]
        openSetHash.remove(current)

        if current == end:
            reconstructPath(prevNode, current, start, draw)
            return True

        for neighbor in current.neighbors:
            tempGScore = gScore[current] + 1

            if tempGScore < gScore[neighbor]:
                prevNode[neighbor] = current
                gScore[neighbor] = tempGScore
                fScore[neighbor] = tempGScore + h(neighbor.getPos(), end.getPos())

                if neighbor not in openSetHash:
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    openSetHash.add(neighbor)
                    if neighbor != end:
                        neighbor.makeOpen()

        draw()

        if current != start:
            current.makeClosed()

    return False
