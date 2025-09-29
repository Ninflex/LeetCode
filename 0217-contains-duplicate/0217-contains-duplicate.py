class Solution(object):
    def containsDuplicate(self, nums):
        dupe = len(nums) != len(set(nums))
        return dupe
        