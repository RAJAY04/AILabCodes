class Solution:
    def solve(self, board):
        # Convert the 2D board into a 1D tuple for easy comparison and storage
        flattened_board = tuple(j for i in board for j in i)
        goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

        # Check if the board is already in the solved state
        if flattened_board == goal_state:
            print("Initial board is already solved.")
            return 0

        # Dictionary to track the moves and parent states for each state
        states = {flattened_board: (0, None)}
        queue = [flattened_board]

        while queue:
            current_state = queue.pop(0)
            move_count, parent = states[current_state]

            for next_state in self.find_next(current_state):
                if next_state not in states:  # If this state hasn't been visited
                    states[next_state] = (move_count + 1, current_state)  # Track moves and parent
                    queue.append(next_state)

                    if next_state == goal_state:
                        # Print each step from the start to the solution
                        self.print_solution_path(states, next_state)
                        return move_count + 1

        # If no solution found, return -1
        print("No solution exists.")
        return -1

    def find_next(self, node):
        # Possible moves for each position on a 3x3 grid
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7]
        }

        pos_0 = node.index(0)
        next_states = []

        for move in moves[pos_0]:
            new_state = list(node)
            new_state[move], new_state[pos_0] = new_state[pos_0], new_state[move]
            next_states.append(tuple(new_state))

        return next_states

    def print_solution_path(self, states, goal_state):
        # Trace back from the goal state to the initial state to retrieve the path
        path = []
        current_state = goal_state
        while current_state:
            path.append(current_state)
            current_state = states[current_state][1]  # Move to the parent state

        # Print each board configuration from start to goal
        for step in reversed(path):
            self.print_board(step)
            print("\n---\n")  # Separator between steps

    def print_board(self, state):
        for i in range(3):
            print(state[i * 3:(i + 1) * 3])


# Example usage
ob = Solution()
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]
print("Number of moves:", ob.solve(matrix))
