import heapq
print("Enter initial state (use 0 for blank):")
start = tuple(map(int, input().split()))
print("Enter goal state (use 0 for blank):")
goal = tuple(map(int, input().split()))
def manhattan(state):
    d = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(j, 3)
            d += abs(x1 - x2) + abs(y1 - y2)
    return d
def neighbors(state):
    result = []
    z = state.index(0)
    x, y = divmod(z, 3)
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            nz = nx * 3 + ny
            s = list(state)
            s[z], s[nz] = s[nz], s[z]
            result.append(tuple(s))
    return result
def solve(start):
    pq = [(manhattan(start), 0, start, [])]
    visited = set()
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal:
            return path
        for s in neighbors(state):
            if s not in visited:
                heapq.heappush(
                    pq, (g + 1 + manhattan(s), g + 1, s, path)
                )
    return None
path = solve(start)
if path:
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
    print("Total moves:", len(path) - 1)
else:
    print("No solution found")
