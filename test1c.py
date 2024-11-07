def isValid(ass, w1, w2, res):
    """Checks if the assignment is valid, i.e., no leading zeros."""
    if ass[w1[0]] == 0 or ass[w2[0]] == 0 or ass[res[0]] == 0:
        return False
    return True

def value(word, ass):
    """Converts a word to a number based on the assigned letter-to-digit mapping."""
    val = 0
    for c in word:
        val = val * 10 + ass[c]
    return val

def helper(w1, w2, res, ass, letters, ans):
    """Recursively tries all digit assignments for the letters and checks if the equation holds."""
    if not letters:  # Base case: if all letters are assigned
        if isValid(ass, w1, w2, res):
            v1 = value(w1, ass)
            v2 = value(w2, ass)
            r = value(res, ass)
            if v1 + v2 == r:
                ans.append((f"{v1} + {v2} = {r}", dict(ass)))  # Store the solution
        return

    # Try assigning each digit to the next letter
    for num in range(10):
        if num not in ass.values():
            curL = letters.pop()  # Get the next letter
            ass[curL] = num
            helper(w1, w2, res, ass, letters, ans)
            del ass[curL]  # Backtrack
            letters.append(curL)  # Add the letter back for the next iteration

def solve(word1, word2, res):
    """Solves the cryptarithmetic puzzle by finding valid digit assignments for the letters."""
    letters = sorted(set(word1 + word2 + res))  # Unique letters from all words
    if len(letters) > 10:
        print("No solutions found: More than 10 unique letters.")
        return

    ans = []  # List to store solutions
    assigned = {}  # Dictionary to store the letter-to-digit mapping
    helper(word1, word2, res, assigned, letters, ans)

    # If solutions are found, print them
    if ans:
        print("Solutions found:")
        for solution in ans:
            print(f'{solution[0]}\t{solution[1]}')
    else:
        print("No solutions found.")

# Main driver code
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
