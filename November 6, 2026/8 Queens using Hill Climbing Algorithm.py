import random
def generate_random_board():
    return [random.randint(0, 7) for _ in range(8)]
def calculate_heuristic(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts
def get_best_neighbor(state):
    n = len(state)
    current_h = calculate_heuristic(state)
    best_neighbors = []
    best_h = current_h
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                neighbor = list(state)
                neighbor[col] = row
                neighbor_h = calculate_heuristic(neighbor)
                if neighbor_h < best_h:
                    best_h = neighbor_h
                    best_neighbors = [neighbor]
                elif neighbor_h == best_h:
                    best_neighbors.append(neighbor)
    if best_neighbors:
        return random.choice(best_neighbors), best_h
    return state, current_h
def hill_climbing(initial_state):
    current_state = list(initial_state)
    current_h = calculate_heuristic(current_state)
    while True:
        neighbor, neighbor_h = get_best_neighbor(current_state)
        if neighbor_h >= current_h:
            break
        current_state = neighbor
        current_h = neighbor_h
    return current_state, current_h
def solve_8_queens():
    attempt = 1
    while True:
        initial_board = generate_random_board()
        initial_conflicts = calculate_heuristic(initial_board)
        print(f"--- Attempt #{attempt} ---")
        print(f"Generated Initial Board Array: {initial_board} (Conflicts: {initial_conflicts})")
        print("Initial Board Visual:")
        print_board(initial_board)
        final_state, final_conflicts = hill_climbing(initial_board)
        if final_conflicts == 0:
            print(f"\n🎉 SUCCESS! Solution found on attempt #{attempt}!")
            print(f"Final Solution Array: {final_state}")
            print("Final Board Visual:")
            print_board(final_state)
            break
        else:
            print(f"❌ Stuck in local minimum (Conflicts remaining: {final_conflicts}). Restarting...\n")
            attempt += 1
def print_board(state):
    for row in range(8):
        line = ""
        for col in range(8):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
if __name__ == "__main__":
    solve_8_queens()
