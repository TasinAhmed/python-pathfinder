def reconstructPath(prevNode, current, start, draw):
    while current in prevNode:
        current = prevNode[current]
        if current != start:
            current.makePath()
            draw()
