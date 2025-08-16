class Solution(object):
    def largestGoodInteger(self, num):
      maxNum = ' '
      prev = ' '
      count = 1 
      
      for i in num:
        if i == prev:
            count += 1
        else:
            count = 1
        if count == 3:
            maxNum = max(i,maxNum)
        prev = i
      if maxNum == ' ':
        return ""
      return maxNum*3

num = "6777133339"
solution = Solution()
print(solution.largestGoodInteger(num))