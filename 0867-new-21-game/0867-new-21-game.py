class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k + maxPts - 1:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        windowSum = 1.0
        result = 0.0

        for x in range(1, n+1):
            dp[x] = windowSum / maxPts

            if x < k:
                windowSum += dp[x]
            else:
                result += dp[x]
            if x - maxPts >= 0:
                windowSum -= dp[x - maxPts]
        return result

n = 10
k = 1
maxPts = 10
solution = Solution()
print(solution.new21Game(n,k,maxPts))        