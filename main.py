from Algorithms.bfs import bfs
from Algorithms.dijkstra import dijkstra
from Algorithms.astar import astar
import pygame
from colors import *
from tkinter import *
from Node import Node

ALGORITHM_NUM = 1
PADDING_X = 30
PADDING_Y = 30
WIDTH = 800


def showVal(root, v):
    val = v.get()
    if val:
        global ALGORITHM_NUM
        ALGORITHM_NUM = val
        root.destroy()


# A* functions


def algorithm(draw, grid, start, end, algoNum):
    # A* Algorithm
    if algoNum == 1:
        astar(draw, grid, start, end)

    # Dijkstra Algorithm
    elif algoNum == 2:
        dijkstra(draw, grid, start, end)

    # BFS Algorithm
    elif algoNum == 3:
        bfs(draw, grid, start, end)


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


def main(width):
    root = Tk()
    root.title("Settings")
    v = IntVar()

    myLabel = Label(root, text="Select Pathfinding Algorithm:")
    astarInput = Radiobutton(root, text="A*", variable=v, value=1)
    dijkstraInput = Radiobutton(root, text="Dijkstra's", variable=v, value=2)
    bfsAlgorithm = Radiobutton(root, text="Breadth-First Search", variable=v, value=3)
    submit = Button(root, text="Submit", command=lambda: [showVal(root, v)])

    myLabel.grid(row=0, sticky="W", padx=PADDING_X, pady=(PADDING_Y, 0))
    astarInput.grid(row=1, sticky="W", padx=(10 + PADDING_X, 0))
    dijkstraInput.grid(row=2, sticky="W", padx=(10 + PADDING_X, 0))
    bfsAlgorithm.grid(row=3, sticky="W", padx=(10 + PADDING_X, 0))
    submit.grid(row=4, pady=(10, PADDING_Y))

    root.mainloop()

    if not v.get():
        return False

    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Pathfinder")

    ROWS = 50
    grid = makeGrid(ROWS, width)

    start = None
    end = None
    done = False

    restart = False
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0] and not done:
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

            elif pygame.mouse.get_pressed()[2] and not done:
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
                if event.key == pygame.K_RETURN and start and end and not done:
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
                    done = True

                elif event.key == pygame.K_c:
                    done = False
                    start = None
                    end = None
                    grid = makeGrid(ROWS, width)

                elif event.key == pygame.K_r:
                    run = False
                    restart = True

    pygame.quit()
    if restart:
        main(width)


main(WIDTH)
