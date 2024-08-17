# Write a program to solve the 8-puzzle problem using Heuristics (h(n)) for A*

from queue import PriorityQueue

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class PuzzleState:
    def __init__(self, board, zero_pos, moves=0, parent=None):
        self.board = board
        self.zero_pos = zero_pos
        self.moves = moves
        self.parent = parent

    # Heuristic function: Manhattan Distance
    def heuristic(self):
        distance = 0
        for r in range(3):
            for c in range(3):
                value = self.board[r][c]
                if value != 0:
                    goal_r, goal_c = divmod(value - 1, 3)
                    distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    # Priority function for PriorityQueue
    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

    def get_neighbors(self):
        neighbors = []
        r, c = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_board = [row[:] for row in self.board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                neighbors.append(PuzzleState(new_board, (nr, nc), self.moves + 1, self))
        return neighbors

def a_star_algorithm(start_state):
    open_list = PriorityQueue()
    closed_set = set()
    open_list.put(start_state)
    
    while not open_list.empty():
        current_state = open_list.get()
        
        if current_state.board == goal_state:
            return current_state
        
        closed_set.add(tuple(map(tuple, current_state.board)))
        
        for neighbor in current_state.get_neighbors():
            if tuple(map(tuple, neighbor.board)) not in closed_set:
                open_list.put(neighbor)
                
    return None

def print_solution(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    for board in reversed(path):
        for row in board:
            print(row)
        print()

if __name__ == "__main__":
    start_board = [
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    
    zero_pos = (2, 0)
    start_state = PuzzleState(start_board, zero_pos)
    solution = a_star_algorithm(start_state)
    
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")
