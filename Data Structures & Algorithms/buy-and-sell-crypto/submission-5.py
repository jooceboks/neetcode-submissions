class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        mins = prices[0]
        for curr in prices:
            if curr < mins:
                mins = curr

            profit = curr - mins
            maxprofit = max(profit, maxprofit)
        return maxprofit
