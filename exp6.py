maze = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

visited = set()
path = []

def dfs(x, y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False

    if maze[x][y] == 1 or (x, y) in visited:
        return False

    visited.add((x, y))
    path.append((x, y))

    if (x, y) == goal:
        return True

    if (dfs(x+1, y) or dfs(x-1, y) or
        dfs(x, y+1) or dfs(x, y-1)):
        return True

    path.pop()
    return False

print("Initial maze:")
for row in maze:
    print(row)

if dfs(0, 0):
    print("Path found:", path)
else:
    print("No Path Found")