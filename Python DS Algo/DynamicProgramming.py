"""
Examples of DP: memoization and tabulation.
Includes: Fibonacci with memoization and tabulation.
"""
class DynamicProgramming:
    @staticmethod
    def fib_memo(n, memo=None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = DynamicProgramming.fib_memo(n-1, memo) + DynamicProgramming.fib_memo(n-2, memo)
        return memo[n]
    @staticmethod
    def fib_tab(n):
        if n <= 2:
            return 1
        dp = [0]*(n+1)
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# Example usage:
# print(DynamicProgramming.fib_memo(10))
# print(DynamicProgramming.fib_tab(10)) 