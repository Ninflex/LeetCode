class Solution(object):
    def longestSubarray(self, nums):
        dp =[]
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
            else:
                dp.append(count)
                count = 0 
        dp.append(count)
        
        if len(dp) == 1:
            return dp[0] - 1
        maxlen = 0
        for i in range(len(dp) - 1):
            maxlen = max(maxlen, dp[i] + dp[i + 1])
        return maxlen

        