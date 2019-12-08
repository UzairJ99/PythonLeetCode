class Solution:
    def maxProfit(self, prices):
        profit = 0
        
        #add up all the rises in the stock pricings
        for price in range(1, len(prices)):
            if prices[price] > prices[price - 1]:
                profit += prices[price] - prices[price - 1]
        
        return profit