class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        low = 0
        maxprofit = 0
        for i in range(len(prices)):
            if prices[low] < prices[i]:
                profit = prices[i] - prices[low]
                maxprofit = max(profit, maxprofit) 
            else:
                low = i             
        return maxprofit      
               
                