def find_value(word, assigned):
    """Converts a word to a number based on the assigned letter-to-digit mapping."""
    num = 0
    for char in word:
        num = num * 10 + assigned[char]
    return num


def is_valid_assignment(word1, word2, result, assigned):
    """Checks if the assignment is valid. Specifically, the first letter of any word cannot be zero."""
    return assigned[word1[0]] != 0 and assigned[word2[0]] != 0 and assigned[result[0]] != 0


def _solve(word1, word2, result, letters, assigned, solutions):
    """Recursively tries all digit assignments for the letters and checks if the equation holds."""
    if not letters:
        if is_valid_assignment(word1, word2, result, assigned):
            num1 = find_value(word1, assigned)
            num2 = find_value(word2, assigned)
            num_result = find_value(result, assigned)
            if num1 + num2 == num_result:
                solutions.append((f'{num1} + {num2} = {num_result}', dict(assigned)))
        return

    for num in range(10):
        if num not in assigned.values():
            cur_letter = letters.pop()
            assigned[cur_letter] = num
            _solve(word1, word2, result, letters, assigned, solutions)
            assigned.pop(cur_letter)
            letters.append(cur_letter)


def solve(word1, word2, result):
    """Solves the cryptarithmetic puzzle by finding valid digit assignments for the letters."""
    letters = sorted(set(word1 + word2 + result))

    if len(letters) > 10:
        print('0 Solutions!')
        return

    solutions = []
    _solve(word1, word2, result, letters, {}, solutions)

    if solutions:
        print('\nSolutions:')
        for soln in solutions:
            print(f'{soln[0]}\t{soln[1]}')
    else:
        print('No solutions found.')


if __name__ == '__main__':
    print('CRYPTARITHMETIC PUZZLE SOLVER')
    print('WORD1 + WORD2 = RESULT')

    word1 = input('Enter WORD1: ').upper()
    word2 = input('Enter WORD2: ').upper()
    result = input('Enter RESULT: ').upper()

    if not all(word.isalpha() for word in (word1, word2, result)):
        raise TypeError('Inputs should only consist of alphabets.')

    solve(word1, word2, result)
