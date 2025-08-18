class Solution(object):
    def singleNumber(self, nums):
        visited = {}
        for i in nums:
            visited[i] = visited.get(i,0) + 1
        x = min(visited, key=visited.get)
        return x
            

        