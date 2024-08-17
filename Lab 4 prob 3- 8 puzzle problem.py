# Write a program to solve the 8-puzzle problem using the DFS and BFS search algorithm


from collections import deque

# Define the goal state as a tuple of tuples.
GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Define possible moves as directions: Up, Down, Left, Right.
MOVES = {
    'U': (-1, 0),  # Move Up: Decrease row index
    'D': (1, 0),   # Move Down: Increase row index
    'L': (0, -1),  # Move Left: Decrease column index
    'R': (0, 1)    # Move Right: Increase column index
}

def get_blank_pos(state):
    """Find the position of the blank tile (0) in the state."""
    for i in range(3):  # Iterate over rows
        for j in range(3):  # Iterate over columns
            if state[i][j] == 0:  # If the tile is blank
                return i, j  # Return the position (row, column)
    return None  # Return None if not found (shouldn't happen)

def is_goal(state):
    """Check if the current state matches the goal state."""
    return state == GOAL_STATE  # Compare the state to the goal state

def get_neighbors(state):
    """Generate all possible next states from the current state."""
    neighbors = []  # List to store neighbor states
    x, y = get_blank_pos(state)  # Get the position of the blank tile
    
    # Try moving the blank tile in each possible direction
    for move, (dx, dy) in MOVES.items():
        new_x, new_y = x + dx, y + dy  # Calculate new position
        
        # Check if the new position is within bounds
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Create a new state by swapping the blank tile with its neighbor
            new_state = [list(row) for row in state]  # Convert tuple to list for mutability
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            # Append the new state and the move that resulted in it
            neighbors.append((move, tuple(tuple(row) for row in new_state)))
    
    return neighbors  # Return the list of neighbor states

def print_state(state, message):
    """Print the state of the puzzle with a message."""
    print(message)
    for row in state:  # Iterate over rows
        print(' '.join(str(x) for x in row))  # Print each row
    print()  # Print a blank line for separation

def dfs(initial_state):
    """Solve the puzzle using Depth-First Search (DFS)."""
    stack = [(initial_state, [])]  # Stack to store states and paths
    visited = set()  # Set to store visited states
    
    while stack:  # While there are states to process
        state, path = stack.pop()  # Get the last state and path from the stack
        print_state(state, f"DFS Current State (Path: {path}):")  # Print current state
        
        if is_goal(state):  # Check if the current state is the goal
            return path  # Return the path if goal is reached
        
        if state in visited:  # Skip states that have already been visited
            continue
        
        visited.add(state)  # Mark the current state as visited
        
        # Add all neighbors to the stack
        for move, neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [move]))  # Add new state and path to the stack

    return None  # Return None if no solution is found

def bfs(initial_state):
    """Solve the puzzle using Breadth-First Search (BFS)."""
    queue = deque([(initial_state, [])])  # Queue to store states and paths
    visited = set()  # Set to store visited states
    
    while queue:  # While there are states to process
        state, path = queue.popleft()  # Get the first state and path from the queue
        print_state(state, f"BFS Current State (Path: {path}):")  # Print current state
        
        if is_goal(state):  # Check if the current state is the goal
            return path  # Return the path if goal is reached
        
        if state in visited:  # Skip states that have already been visited
            continue
        
        visited.add(state)  # Mark the current state as visited
        
        # Add all neighbors to the queue
        for move, neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path + [move]))  # Add new state and path to the queue

    return None  # Return None if no solution is found

# Example usage
initial_state = ((1, 2, 3), (4, 5, 6), (0, 7, 8))  # Define an initial state for testing

print("DFS Solution:")
dfs_solution = dfs(initial_state)  # Find solution using DFS
if dfs_solution is not None:
    print("DFS Moves:", dfs_solution)  # Print the sequence of moves
else:
    print("DFS No solution found.")  # Print if no solution was found

print("\nBFS Solution:")
bfs_solution = bfs(initial_state)  # Find solution using BFS
if bfs_solution is not None:
    print("BFS Moves:", bfs_solution)  # Print the sequence of moves
else:
    print("BFS No solution found.")  # Print if no solution was found

