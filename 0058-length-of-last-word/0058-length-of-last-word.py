class Solution(object):
    def lengthOfLastWord(self, s):
        x = s.strip()
        l = 0

        for i in range(len(x)):
            if x[i] == " ":
                l = 0
            else:
                l += 1
        return l 

s = "hello world"
solution = Solution()
print(solution.lengthOfLastWord(s))
