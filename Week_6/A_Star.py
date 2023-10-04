import heapq
import numpy as np

# Define the goal state
goal_state = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 0]])

# Define the initial state
initial_state = np.array([[2, 8, 3],
                          [1, 6, 4],
                          [7, 0, 5]])

# Define the possible moves (up, down, left, right)
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_position = np.where(goal_state == state[i][j])
                distance += abs(i - goal_position[0][0]) + abs(j - goal_position[1][0])
    return distance

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_neighbors(state):
    neighbors = []
    zero_position = np.where(state == 0)
    x, y = zero_position[0][0], zero_position[1][0]
    
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(new_x, new_y):
            neighbor = state.copy()
            neighbor[x][y], neighbor[new_x][new_y] = neighbor[new_x][new_y], neighbor[x][y]
            neighbors.append(neighbor)
    
    return neighbors

def astar(initial_state):
    open_list = [(manhattan_distance(initial_state), 0, initial_state)]
    closed_set = set()
    
    while open_list:
        _, level, current_state = heapq.heappop(open_list)
        
        if np.array_equal(current_state, goal_state):
            return level, current_state
        
        closed_set.add(tuple(map(tuple, current_state)))
        
        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in closed_set:
                heapq.heappush(open_list, (manhattan_distance(neighbor) + level + 1, level + 1, neighbor))
    
    return None

level, final_state = astar(initial_state)

if final_state is not None:
    print("Solution found in", level, "steps:")
    print(final_state)
else:
    print("No solution found.")
