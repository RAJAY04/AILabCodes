def findNextStates(curState):
    # Define possible moves for each position of the zero tile
    index = {
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

    # Find the position of zero in the current state
    indexOfZero = curState.index(0)

    # Generate all possible states by moving zero to its adjacent positions
    nextStates = []
    for i in index[indexOfZero]:
        curState[i], curState[indexOfZero] = curState[indexOfZero], curState[i]
        nextStates.append(tuple(curState))
        curState[i], curState[indexOfZero] = curState[indexOfZero], curState[i]  # Restore the original state

    return nextStates


def print_path(goal_state, state_dict):
    # Reconstruct and print the path from the initial state to the goal state
    path = []
    current_state = goal_state

    # Trace back from goal to start using parent references
    while current_state is not None:
        path.append(current_state)
        current_state = state_dict[current_state][1]

    # Print the path from start to goal
    path.reverse()
    print("Solution Path:")
    for state in path:
        print_state(state)


def print_state(state):
    # Print a 3x3 board representation of a given state
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()  # Add a newline for better readability


def main(board):
    # Flatten the 2D board into a 1D tuple
    flattenBoard = tuple(col for row in board for col in row)

    # Initialize the queue and the state dictionary with move count and parent state
    queue = [flattenBoard]
    state_dict = {flattenBoard: (0, None)}  # Dictionary to store moves and parent state

    # Perform BFS to find the shortest path
    while queue:
        # Get the current state and the number of moves taken to reach it
        curState = queue.pop(0)
        move_count = state_dict[curState][0]

        # Generate possible next states
        nextStates = findNextStates(list(curState))

        for state in nextStates:
            if state not in state_dict:  # Only explore new states
                state_dict[state] = (move_count + 1, curState)
                queue.append(state)

                # Check if the goal state is reached
                if state == (0, 1, 2, 3, 4, 5, 6, 7, 8):
                    print_path(state, state_dict)
                    return move_count + 1

    return -1  # Return -1 if no solution is found


# Test board
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]

# Solve the puzzle and print the number of moves
print("Number of Moves:", main(matrix))
