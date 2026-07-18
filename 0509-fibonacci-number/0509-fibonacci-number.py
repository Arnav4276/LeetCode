class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def F(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            memo[n] = F(n-1) + F(n-2)
            return memo[n]

        return F(n)