from BFSNode import BFSNode
from DijkstraNode import DijkstraNode
import pygame
import math
from queue import PriorityQueue
from colors import *
from AstarNode import AstarNode

ALGORITHM_NUM = 1
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinder")


def reconstructPath(prevNode, current, start, draw):
    while current in prevNode:
        current = prevNode[current]
        if current != start:
            current.makePath()
            draw()


# A* functions
def h(p1, p2):
    # Heuristic function
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def algorithm(draw, grid, start, end, algoNum):
    # A* Algorithm
    if algoNum == 0:
        count = 0
        openSet = PriorityQueue()
        openSet.put((0, count, start))
        prevNode = {}
        gScore = {node: math.inf for row in grid for node in row}
        gScore[start] = 0
        fScore = {node: math.inf for row in grid for node in row}
        fScore[start] = h(start.getPos(), end.getPos())

        while not openSet.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = openSet.get()[2]

            if current == end:
                reconstructPath(prevNode, current, start, draw)
                return True

            for neighbor in current.neighbors:
                tempGScore = gScore[current] + 1

                if tempGScore < gScore[neighbor]:
                    prevNode[neighbor] = current
                    gScore[neighbor] = tempGScore
                    fScore[neighbor] = tempGScore + h(neighbor.getPos(), end.getPos())

                    if not neighbor.isOpen():
                        count += 1
                        openSet.put((fScore[neighbor], count, neighbor))
                        if neighbor != end:
                            neighbor.makeOpen()

            draw()

            if current != start:
                current.makeClosed()

        return False

    # Dijkstra Algorithm
    elif algoNum == 1:
        openNodes = PriorityQueue()
        grid[start.row][start.col].distance = 0
        openNodes.put(start)
        prevNode = {}
        visited = set()

        while not openNodes.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = openNodes.get()

            if current == end:
                reconstructPath(prevNode, current, start, draw)
                return True

            for neighbor in current.neighbors:
                totalDist = current.distance + 1

                if (
                    not neighbor.isBarrier()
                    and totalDist < neighbor.distance
                    and neighbor not in visited
                ):
                    neighbor.distance = totalDist
                    prevNode[neighbor] = current
                    openNodes.put(neighbor)
                    # visitingNodesHash.add(neighbor)
                    if neighbor != end:
                        neighbor.makeOpen()
            draw()

            visited.add(current)
            if current != start:
                current.makeClosed()

        return False

    # BFS Algorithm
    elif algoNum == 2:
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


# Grid functions
def makeGrid(rows, width, algoNum):
    # A*
    if algoNum == 0:
        gap = width // rows
        grid = [[AstarNode(i, j, gap, rows) for j in range(rows)] for i in range(rows)]

        return grid

    # Dijkstra
    elif algoNum == 1:
        gap = width // rows
        grid = [
            [DijkstraNode(i, j, gap, rows, math.inf) for j in range(rows)]
            for i in range(rows)
        ]

        return grid

    # BFS
    elif algoNum == 2:
        gap = width // rows
        grid = [[BFSNode(i, j, gap, rows) for j in range(rows)] for i in range(rows)]

        return grid


def drawGrid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    drawGrid(win, rows, width)
    pygame.display.update()


def getClickedPos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 50
    grid = makeGrid(ROWS, width, ALGORITHM_NUM)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                # Left mouse button click
                try:
                    pos = pygame.mouse.get_pos()
                    row, col = getClickedPos(pos, ROWS, width)
                    node = grid[row][col]
                    if not start and node != end:
                        start = node
                        start.makeStart()

                    elif not end and node != start:
                        end = node
                        end.makeEnd()

                    elif node != end and node != start:
                        node.makeBarrier()

                except AttributeError:
                    pass

            elif pygame.mouse.get_pressed()[2]:
                # Right mouse button click
                pos = pygame.mouse.get_pos()
                row, col = getClickedPos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None

                if node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and start and end:
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid)

                    algorithm(
                        lambda: draw(win, grid, ROWS, width),
                        grid,
                        start,
                        end,
                        ALGORITHM_NUM,
                    )

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = makeGrid(ROWS, width, ALGORITHM_NUM)

    pygame.quit()


main(WIN, WIDTH)
