n = int(input("Enter the value of N"))

def formatBoard(board):
    s = []
    for row in board:
        s.append(''.join(row))
    return s

def isValid(board, row, col):
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    # Check the column above
    i = row
    while i >= 0:
        if board[i][col] == "Q":
            return False
        i -= 1

    return True

def NQ(board, row, result):
    if row == len(board):
        result.append(formatBoard(board))
        return

    for i in range(len(board[0])):
        if isValid(board, row, i):  # Place queen only if position is valid
            board[row][i] = "Q"
            NQ(board, row + 1, result)
            board[row][i] = "."  # Remove queen for backtracking

# Initialize the board
board = [["." for _ in range(n)] for _ in range(n)]

# List to store solutions
result = []
NQ(board, 0, result)

# Print all solutions
if result:
    for soln in result:
        for row in soln:
            print(row)
        print()
else:
    print("No solutions found.")
