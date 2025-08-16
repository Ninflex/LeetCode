class Solution(object):
    def strStr(self, haystack, needle):
        s = haystack.find(needle)
        return s

haystack = "sadbutsad"
needle = "sad"
solution = Solution()
print(solution.strStr(haystack,needle))