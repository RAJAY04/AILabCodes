class Solution:
    def solveNQueens(self, n):
        res = []
        board = self.create_and_initialize_board(n)
        self.backtrack(board, 0, res)
        return res

    def backtrack(self, board, row, res):
        if row == len(board):
            res.append(self.format_board(board))
            return
        for col in range(len(board)):
            if self.is_valid(board, row, col):
                board[row][col] = 'Q'
                self.backtrack(board, row + 1, res)
                board[row][col] = '.'

    def format_board(self, board):
        return [''.join(row) for row in board]

    def create_and_initialize_board(self, n):
        return [['.' for _ in range(n)] for _ in range(n)]

    def is_valid(self, board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # Check top-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # Check top-right diagonal
        i, j = row, col
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

# Example usage
n = int(input("Enter the number of queens: "))
solution = Solution()
results = solution.solveNQueens(n)
for result in results:
    for row in result:
        print(row)
    print()
