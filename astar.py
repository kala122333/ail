import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1

            row = abs(i // 3 - goal_pos // 3)
            col = abs(i % 3 - goal_pos % 3)

            distance += row + col

    return distance

def get_neighbors(state):
    neighbors = []
    pos = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:
        new_pos = pos + move

        if 0 <= new_pos < 9:
            if abs(pos // 3 - new_pos // 3) + abs(pos % 3 - new_pos % 3) == 1:
                new_state = list(state)

                new_state[pos] = state[new_pos]
                new_state[new_pos] = 0

                neighbors.append(tuple(new_state))

    return neighbors

def astar(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path)
                )

    return None

start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split()))

solution = astar(start)

if solution:
    for step, state in enumerate(solution):
        print("\nStep", step)
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])

    print("Puzzle solved!")
else:
    print("No solution found!")