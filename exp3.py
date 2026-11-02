import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = blank // 3, blank % 3

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[blank], new_state[new_pos] = \
                new_state[new_pos], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors

queue = [(heuristic(start), 0, start)]
best_cost = {start: 0}
parent = {start: None}

while queue:
    f, g, current = heapq.heappop(queue)

    if current == goal:
        break

    if g > best_cost[current]:
        continue

    for neighbor in get_neighbors(current):
        new_g = g + 1

        if neighbor not in best_cost or new_g < best_cost[neighbor]:
            best_cost[neighbor] = new_g
            parent[neighbor] = current
            new_f = new_g + heuristic(neighbor)

            heapq.heappush(queue, (new_f, new_g, neighbor))

if goal in parent:
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Solution found in", len(path) - 1, "moves:")

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")