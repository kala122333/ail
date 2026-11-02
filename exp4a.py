from collections import deque

start = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))

queue = deque([(start, [])])
visited = {start}

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("\n".join(path))
        break

    for i in range(3):
        if state[i]:
            disk = state[i][-1]

            for j in range(3):
                if i != j and (not state[j] or state[j][-1] > disk):
                    new = [list(r) for r in state]
                    new[i].pop()
                    new[j].append(disk)
                    new = tuple(tuple(r) for r in new)

                    if new not in visited:
                        visited.add(new)
                        move = f"Move disk {disk} from {'ABC'[i]} to {'ABC'[j]}"
                        queue.append((new, path + [move]))
else:
    print("No solution found")