class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        maxprofit = 0
        
        for price in prices:
            profit = price - lowest
            maxprofit = max(maxprofit,profit)
            lowest = min(lowest, price)
        
        return maxprofit



        
