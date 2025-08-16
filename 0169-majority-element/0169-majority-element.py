class Solution(object):
    def majorityElement(self, nums):
        count = {}

        for i in nums:
            count[i] = count.get(i,0)+1

        x = max(count, key=count.get)
        return x

nums = [3,2,3]
solution = Solution()
print(solution.majorityElement(nums))