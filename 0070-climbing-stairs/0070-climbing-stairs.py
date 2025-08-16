class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        fib = [1,2]
        while len(fib) <= 45 and n-1 >= len(fib):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]

n=4
solution = Solution()
print(solution.climbStairs(n))
        