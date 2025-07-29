"""
Examples of recursion and backtracking.
Includes: Factorial, N-Queens problem.
"""
class RecursionBacktracking:
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        return n * RecursionBacktracking.factorial(n-1)
    @staticmethod
    def solve_n_queens(n):
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or \
                   board[i] - i == col - row or \
                   board[i] + i == col + row:
                    return False
            return True
        def solve(row, board, res):
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row+1, board, res)
        res = []
        solve(0, [0]*n, res)
        return res
# Example usage:
# print(RecursionBacktracking.factorial(5))
# print(RecursionBacktracking.solve_n_queens(4)) 