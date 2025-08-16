class Solution(object):
    def maximum69Number (self, num):
        best = str(num)
        best = best.replace('6', '9', 1)
        return int(best)

num = 9669
solution = Solution()
print(solution.maximum69Number(num))

        