from collections import deque

grid = [
    ['S', '.', '#', '.'],
    ['.', '.', '#', '.'],
    ['.', '.', '.', '.'],
    ['#', '#', '.', 'G']
]

start = (0, 0)
goal = (3, 3)

queue = deque([(start, [start])])
visited = {start}

while queue:
    current, path = queue.popleft()

    if current == goal:
        print("Path found:")
        for position in path:
            print(position)
        print("Goal reached!")
        break

    x, y = current

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 4 and 0 <= ny < 4:
            if grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
else:
    print("No path found!")