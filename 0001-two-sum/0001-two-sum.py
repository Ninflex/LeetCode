class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement],i]
            lookup[num] = i
        return []

nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums,target))