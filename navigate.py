grid = [
    ['S', '.', '#', '.'],
    ['.', '.', '#', '.'],
    ['#', '.', '.', '.'],
    ['.', '.', '.', 'G']
]

rows = len(grid)
cols = len(grid[0])
visited = set()

def navigate(x, y):
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return False

    if grid[x][y] == '#' or (x, y) in visited:
        return False

    visited.add((x, y))

    if grid[x][y] == 'G':
        print("Goal reached!")
        return True

    if navigate(x + 1, y):
        print("Move Down")
        return True
    if navigate(x, y + 1):
        print("Move Right")
        return True
    if navigate(x - 1, y):
        print("Move Up")
        return True
    if navigate(x, y - 1):
        print("Move Left")
        return True

    return False

print("Grid:")
for row in grid:
    print(" ".join(row))

if not navigate(0, 0):
    print("No path found!")