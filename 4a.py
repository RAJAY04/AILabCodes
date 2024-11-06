VARIABLES = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
DOMAIN = ["Monday", "Tuesday", "Wednesday"]
CONSTRAINTS = [
    ("csc", "maths"),
    ("csc", "phy"),
    ("maths", "phy"),
    ("maths", "che"),
    ("maths", "tam"),
    ("phy", "tam"),
    ("phy", "eng"),
    ("che", "eng"),
    ("tam", "eng"),
    ("tam", "bio"),
    ("eng", "bio")
]


def backtrack(assignment):
    """Finds an assignment of days to subjects using backtracking."""

    # Check if all variables have been assigned
    if len(assignment) == len(VARIABLES):
        return assignment  # Return the complete assignment

    # Select the next unassigned variable (subject)
    var = select_unassigned_variable(assignment)

    # Try each possible value in the DOMAIN (days)
    for value in DOMAIN:
        # Check if the current assignment is consistent with the constraints
        if is_consistent(var, value, assignment):
            assignment[var] = value  # Assign the value (day) to the variable (subject)

            # Recurse to assign days to the next subjects
            result = backtrack(assignment)

            # If the result is valid, return the valid assignment
            if result is not None:
                return result

            # If no solution is found, remove the current assignment and try the next value
            del assignment[var]

    # Return None if no assignment is found
    return None


def select_unassigned_variable(assignment):
    """Selects a variable (subject) that has not been assigned a value yet."""
    for var in VARIABLES:
        if var not in assignment:
            return var  # Return the first unassigned variable (subject)


def is_consistent(var, value, assignment):
    """Checks if assigning 'value' (a day) to 'var' (a subject) is consistent."""
    # Check all constraints
    for var1, var2 in CONSTRAINTS:
        if var1 == var or var2 == var:  # If the current variable is part of a constraint
            # Check if the other variable in the constraint already has the same value (day)
            for assigned_var, assigned_day in assignment.items():
                if (assigned_var == var1 or assigned_var == var2) and assigned_day == value:
                    return False  # Inconsistent assignment (same day assigned to constrained subjects)

    # If no conflicts, the assignment is consistent
    return True


# Start the backtracking search with an empty assignment
solution = backtrack({})

# Print the solution if found
if solution:
    print("Assignment found:")
    for subject, day in solution.items():
        print(f"{subject}: {day}")
else:
    print("No valid assignment found.")
