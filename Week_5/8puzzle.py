# Define the initial state and goal state
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def create(initial_state, level):
    def is_valid_move(x, y):
        return 0 <= x < 3 and 0 <= y < 3

    def calculate_heuristic(state):
        # Calculate the heuristic value (number of tiles misplaced)
        misplaced_tiles = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state[i][j]:
                    misplaced_tiles += 1
        return misplaced_tiles

    def print_state(state, heuristic):
        for row in state:
            print(row)
        print("Heuristic:", heuristic)
        print("--------")

    def move_blank(state, x, y):
        # Create a copy of the current state
        new_state = [row[:] for row in state]

        # Move the blank tile to the specified position
        new_state[x][y], new_state[blank_x][blank_y] = new_state[blank_x][blank_y], new_state[x][y]

        return new_state

    def generate_states(state, current_level):
        if current_level == level:
            return

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = blank_x + dx, blank_y + dy

            if is_valid_move(new_x, new_y):
                new_state = move_blank(state, new_x, new_y)
                heuristic_value = calculate_heuristic(new_state)
                print_state(new_state, heuristic_value)
                generate_states(new_state, current_level + 1)

    # Find the position of the blank tile in the initial state
    for i in range(3):
        for j in range(3):
            if initial_state[i][j] == 0:
                blank_x, blank_y = i, j

    # Print the initial state and its heuristic value
    initial_heuristic = calculate_heuristic(initial_state)
    print("Initial State:")
    print_state(initial_state, initial_heuristic)

    # Generate states up to the specified level
    generate_states(initial_state, 0)

# Example usage:
create(initial_state, 2)
