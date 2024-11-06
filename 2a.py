from queue import PriorityQueue

def haeuristic(current, goal):
    """Calculate the heuristic distance to the goal string."""
    dist = 0
    for i in range(len(goal)):
        dist += abs(i - current.index(goal[i]))
    return dist

def generate_children(state):
    """Generate all possible states by swapping adjacent characters."""
    children = []
    for i in range(len(state) - 1):
        # Swap adjacent characters
        new_state = list(state)
        new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
        children.append("".join(new_state))
    return children

def a_star(start, goal):
    """Perform A* search to find the shortest path from start to goal."""
    priority_queue = PriorityQueue()
    visited = set()
    priority_queue.put((0, start))  # (cost, state)
    visited.add(start)
    path_map = {start: []}  # Map to track the path taken

    while not priority_queue.empty():
        current_state = priority_queue.get()[1]

        # If the goal is reached, return the transformation steps
        if current_state == goal:
            return path_map[current_state] + [goal]

        # Generate children states
        for child in generate_children(current_state):
            if child not in visited:
                visited.add(child)
                # Calculate total cost for A*
                cost = heuristic(child, goal)
                priority_queue.put((cost, child))
                path_map[child] = path_map[current_state] + [current_state]  # Track path

    return None  # Transformation is not possible

# Main function to run the solver
if __name__ == "__main__":
    # Input
    start_string = input("Enter the start string: ")
    goal_string = input("Enter the goal string: ")

    # Check if both strings have the same characters
    if sorted(start_string) != sorted(goal_string):
        print("Transformation is not possible!")
    else:
        # Perform A* search
        result_path = a_star(start_string, goal_string)

        # Output
        if result_path is not None:
            print("Transformation steps:")
            for step in result_path:
                print(step)
        else:
            print("Transformation is not possible!")
