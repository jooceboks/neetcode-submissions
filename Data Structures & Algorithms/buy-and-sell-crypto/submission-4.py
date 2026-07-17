class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #profit = j - i
        curr = 0
        low = 0
        maxprofit = 0 
        for curr in range(len(prices)):
            profit = prices[curr] - prices[low]
            maxprofit = max(profit, maxprofit)
            if prices[low] > prices[curr]:
                low = curr
            curr += 1

        return maxprofit
            
                