grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

print("Grid:")
for row in grid:
    print(row)

position = [0, 0]
goal = [2, 2]
internal_state = []

print("Agent start at:", position)

while position != goal:
    row, col = position[0], position[1]

    if col + 1 < 3 and grid[row][col + 1] == 0:
        position[1] += 1
    elif row + 1 < 3 and grid[row + 1][col] == 0:
        position[0] += 1
    else:
        print("Agent is blocked")
        break
    
    internal_state.append(position.copy())

if position == goal:
    print("Goal reached")

print("Internal states:", internal_state)