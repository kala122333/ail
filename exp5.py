from collections import deque

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

print("Grid:")
for row in grid:
    print(row)

start = (0, 0)
goal = (2, 2)

queue = deque([[start]])
visited = [start]

while queue:
    path = queue.popleft()
    x, y = path[-1]

    if (x, y) == goal:
        print("Shortest path:", path)
        break

    moves = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

    for nx, ny in moves:
        if (0 <= nx < 3 and 0 <= ny < 3
                and grid[nx][ny] == 0
                and (nx, ny) not in visited):

            visited.append((nx, ny))
            queue.append(path + [(nx, ny)])

else:
    print("No path found")