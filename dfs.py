# Water Jug Problem using DFS

def dfs(x, y, visited):
    if (x, y) in visited:
        return False

    visited.add((x, y))
    print(x, y)

    if x == 2:
        return True

    moves = [
        (4, y), (x, 3), (0, y), (x, 0),
        (x - min(x, 3-y), y + min(x, 3-y)),
        (x + min(y, 4-x), y - min(y, 4-x))
    ]

    for a, b in moves:
        if dfs(a, b, visited):
            return True

    return False


print("Jug capacities: 4L and 3L")
print("Target: 2L in the 4L jug")
print("States (4L jug, 3L jug):")

if not dfs(0, 0, set()):
    print("Solution not found")