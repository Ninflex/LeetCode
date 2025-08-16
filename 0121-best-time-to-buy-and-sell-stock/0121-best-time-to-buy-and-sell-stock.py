class Solution(object):
    def maxProfit(self, prices):
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit


prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))   