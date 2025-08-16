class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        sp = 1

        while sp < len(nums):
            if nums[sp] == nums[sp - 1]:
                nums.pop(sp)
                k += 1
            else:
                sp += 1
        'can do with for loop = faster'

nums = [1,1,2]
solution = Solution()
k = solution.removeDuplicates(nums)
print(k)