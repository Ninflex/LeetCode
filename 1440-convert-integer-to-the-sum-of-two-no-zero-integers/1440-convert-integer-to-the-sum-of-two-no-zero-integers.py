class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1,n):
            left = i
            right = n - i
            if '0' not in str(left) and '0' not in str(right):
                return [left,right]
        return []