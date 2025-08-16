class Solution(object):
    def plusOne(self, digits):
        numDigits = int(''.join(str(d) for d in digits)) + 1
        numDigits = [int(d) for d in str(numDigits)]
        return numDigits

digits = [1,2,3]
solution = Solution()
print(solution.plusOne(digits))