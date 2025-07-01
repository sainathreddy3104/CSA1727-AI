import numpy as np
from queue import PriorityQueue

def heuristic(state):
    return sum((state[i] != goal[i]) for i in range(9))

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(new_state)
    return neighbors

def a_star(start):
    global goal
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    pq = PriorityQueue()
    pq.put((0, start))
    visited = set()
    
    while not pq.empty():
        cost, current = pq.get()
        if current == goal:
            return True
        visited.add(tuple(current))
        
        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                pq.put((cost + heuristic(neighbor), neighbor))
    return False

if __name__ == "__main__":
    try:
        initial_state = list(map(int, input("Enter the initial state (0 for empty space): ").split()))
        if len(initial_state) != 9 or set(initial_state) != set(range(9)):
            raise ValueError("Invalid input. Please enter numbers from 0 to 8.")
        if a_star(initial_state):
            print("Solution found!")
        else:
            print("No solution exists.")
    except Exception as e:
        print(f"Error: {e}")
