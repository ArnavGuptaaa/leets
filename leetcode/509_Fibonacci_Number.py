"""
Name: Fibonacci Number (#509)
URL: https://leetcode.com/problems/fibonacci-number/
"""

class Solution:
    def fib(self, n: int) -> int:
        cache = [-1] * (n + 1)

        """
        Time Complexity: O(N)
        Space Complexity: O(N + N)
        """
        def memo_fib(n):
            if n <= 1:
                return n

            if cache[n] != -1:
                return cache[n]

            cache[n] = memo_fib(n - 1) + memo_fib(n - 2)

            return cache[n]

        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        def tab_fib(n):
            if n <= 1:
                return n

            cache[0] = 0
            cache[1] = 1

            for idx in range(2, n + 1):
                cache[idx] = cache[idx - 1] + cache[idx - 2]

            return cache[n]

        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        def so_fib(n):
            if n <= 1:
                return n

            prev2 = 0
            prev = 1

            for idx in range(2, n + 1):
                result = prev + prev2

                prev2 = prev
                prev = result

            return prev

        # Memoized
        return memo_fib(n)

        # Tabulated
        return tab_fib(n)

        # Space optimized
        return so_fib(n)