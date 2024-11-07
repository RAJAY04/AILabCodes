# List of subjects and their corresponding possible days
subjects = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
days = ["Monday", "Tuesday", "Wednesday"]

# Constraints between subjects (i.e., subjects that can't be assigned the same day)
subject_constraints = [
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


def backtrack(assigned_days):
    """Assigns days to subjects using backtracking."""

    # Base case: if all subjects have been assigned a day, return the assignment
    if len(assigned_days) == len(subjects):
        return assigned_days

    # Select the next unassigned subject
    subject = select_unassigned_subject(assigned_days)

    # Try each day from the list of days
    for day in days:
        # Check if the assignment is consistent with constraints
        if is_consistent(subject, day, assigned_days):
            assigned_days[subject] = day  # Assign the day to the subject

            # Recurse to assign days to the remaining subjects
            result = backtrack(assigned_days)

            # If a valid result is found, return it
            if result is not None:
                return result

            # If no valid result is found, remove the current assignment and try the next day
            del assigned_days[subject]

    # If no valid assignment can be found, return None
    return None


def select_unassigned_subject(assigned_days):
    """Selects the next subject that hasn't been assigned a day yet."""
    for subject in subjects:
        if subject not in assigned_days:
            return subject


def is_consistent(subject, day, assigned_days):
    """
    This function checks if assigning a specific 'day' to a 'subject' is
    consistent with the constraints between subjects.

    Constraints: Certain subjects cannot share the same day.
    """

    # Step 1: Check each pair of subjects that have constraints.
    for subject1, subject2 in subject_constraints:


            # Step 3: Check if the other subject in the constraint already has the same day assigned
        if subject1 == subject:
                # If subject1 is the current subject, check if subject2 has been assigned the same day
            if subject2 in assigned_days and assigned_days[subject2] == day:
                return False  # Conflict found: subject2 has the same day as subject1

        elif subject2 == subject:
                # If subject2 is the current subject, check if subject1 has been assigned the same day
            if subject1 in assigned_days and assigned_days[subject1] == day:
                return False  # Conflict found: subject1 has the same day as subject2

    # Step 4: If no conflicts were found, the assignment is consistent.
    return True


# Start the backtracking search with an empty assignment of subjects to days
solution = backtrack({})

# Print the solution if a valid assignment is found
if solution:
    print("Valid subject-day assignment found:")
    for subject, day in solution.items():
        print(f"{subject}: {day}")
else:
    print("No valid subject-day assignment found.")
