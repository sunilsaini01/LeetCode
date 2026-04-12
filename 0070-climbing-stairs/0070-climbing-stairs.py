class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def sumway(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 1
            
            memo[n] = sumway(n-1) + sumway(n-2)
            return memo[n]
        
        return sumway(n)