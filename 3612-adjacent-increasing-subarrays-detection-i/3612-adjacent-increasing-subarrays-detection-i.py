class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        inc = 1
        prevInc = 0
        maxLen = 0

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                prevInc = inc
                inc = 1
            maxLen = max(maxLen, max(inc >> 1, min(prevInc,inc)))
            if maxLen >= k:
                return True
        return False
        