class Solution(object):
    def maxFrequencyElements(self, nums):
        count = {}

        for i in nums:
            count[i] = count.get(i,0)+1
        maxFreq = max(count.values())
        res = sum(count for count in count.values() if count == maxFreq)
        return res