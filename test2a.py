from queue import PriorityQueue

def heuristic(cur, goal):
    """Calculate the heuristic distance to the goal string."""
    val = 0
    for i in range(len(goal)):
        val += abs(i - cur.index(goal[i]))  # Corrected index logic
    return val

def genAllChild(s):
    """Generate all possible states by swapping adjacent characters."""
    child = []
    for i in range(len(s) - 1):
        new = list(s)
        new[i], new[i + 1] = new[i + 1], new[i]
        child.append(''.join(new))
    return child

def a_star(s, g):
    """Perform A* search to find the shortest path from start to goal."""
    q = PriorityQueue()
    vis = set()
    q.put((0, s))  # Start with 0 cost for the initial state
    vis.add(s)
    path_map = {s: []}  # Dictionary to track the path taken

    while not q.empty():
        # Get the state with the lowest cost (heuristic)
        dis, curState = q.get()

        # If the goal is reached, return the transformation steps
        if curState == g:
            return path_map[curState] + [g]

        # Generate all possible child states by swapping adjacent characters
        child = genAllChild(curState)
        for c in child:
            if c not in vis:
                vis.add(c)
                # Calculate the heuristic cost for this child state
                cost = heuristic(c, g)
                q.put((cost, c))  # Add to the priority queue with heuristic as priority
                path_map[c] = path_map[curState] + [curState]  # Track the path to the child

    return None  # No transformation is possible

# Main function to run the solver
if __name__ == "__main__":
    start_string = input("Enter the start string: ")
    goal_string = input("Enter the goal string: ")

    # Check if both strings have the same characters
    if sorted(start_string) != sorted(goal_string):
        print("Transformation is not possible!")
    else:
        # Perform A* search
        result_path = a_star(start_string, goal_string)

        # Output the result
        if result_path is not None:
            print("Transformation steps:")
            for step in result_path:
                print(step)
        else:
            print("Transformation is not possible!")
