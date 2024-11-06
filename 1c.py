def find_value(word, assigned):
    """
    Converts a word into a number based on the assigned letter-to-digit mapping.

    Each character in the word is replaced by its corresponding digit from the `assigned` dictionary,
    and the resulting sequence of digits is then treated as a number.
    """
    # Start with an initial value of 0
    value = 0

    # Iterate over each character in the word
    for char in word:
        # Multiply the current value by 10 (shift left by one decimal place) and add the digit assigned to the character
        digit = assigned[char]
        value = value * 10 + digit  # Add the digit to the number being formed

    # Return the formed number
    return value


def is_valid_assignment(word1, word2, result, assigned):
    """
    Checks if the current assignment is valid.

    A valid assignment does not assign a 0 to the first letter of any word.
    """
    # Check if any of the first letters of the words are assigned 0
    if assigned[word1[0]] == 0 or assigned[word2[0]] == 0 or assigned[result[0]] == 0:
        return False

    # If no first letter is assigned 0, then it's a valid assignment
    return True


def solve(word1, word2, result):
    """
    Solves the cryptarithmetic puzzle by assigning digits to the letters and checking the equation.
    """
    # Step 1: Find all unique letters in the input words
    unique_letters = set(word1 + word2 + result)

    # If there are more than 10 unique letters, it's impossible to solve (since there are only 10 digits)
    if len(unique_letters) > 10:
        print("0 Solutions!")
        return

    # Step 2: Sort the letters for consistent iteration (helps in backtracking)
    unique_letters = sorted(unique_letters)

    # Initialize an empty dictionary to store the digit assignments
    assigned = {}

    # Step 3: Prepare a list to store valid solutions
    solutions = []

    def try_assignment(index):
        """
        Attempts to assign digits to the letters using backtracking.
        """
        # Base case: If all letters have been assigned, check if the equation is valid
        if index == len(unique_letters):
            # Check if the current assignment is valid
            if is_valid_assignment(word1, word2, result, assigned):
                # Convert words to numbers based on the current assignment
                num1 = find_value(word1, assigned)
                num2 = find_value(word2, assigned)
                num_result = find_value(result, assigned)

                # Check if the equation holds true
                if num1 + num2 == num_result:
                    # If valid, store the solution
                    solution_str = f'{num1} + {num2} = {num_result}'
                    solutions.append((solution_str, dict(assigned)))  # Save the solution along with the assignments
            return

        # Recursive case: Try assigning digits to the current letter
        letter = unique_letters[index]

        # Try all possible digits (from 0 to 9)
        for num in range(10):
            # Ensure the digit has not been assigned already
            if num not in assigned.values():
                # Assign the digit to the letter
                assigned[letter] = num

                # Recur to assign digits to the next letter
                try_assignment(index + 1)

                # Backtrack: remove the current letter's assignment
                del assigned[letter]

    # Step 4: Start the assignment process from the first letter
    try_assignment(0)

    # Step 5: Print the results
    if solutions:
        print("\nSolutions:")
        for solution, mapping in solutions:
            print(f'{solution} {mapping}')
    else:
        print('No solutions found.')


if __name__ == '__main__':
    print('CRYPTARITHMETIC PUZZLE SOLVER\nWORD1 + WORD2 = RESULT')

    # Take input for the words
    word1 = input('Enter WORD1: ').upper()
    word2 = input('Enter WORD2: ').upper()
    result = input('Enter RESULT: ').upper()

    # Ensure the input consists only of alphabetic characters
    if not all(word.isalpha() for word in (word1, word2, result)):
        raise TypeError('Inputs should only consist of alphabets.')

    # Call the solver function
    solve(word1, word2, result)
