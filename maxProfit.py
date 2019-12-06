class Solution:
    def maxProfit(self, prices):
        #objective: find i and j with largest difference where i < j
        if len(prices) < 2:
            return 0
            
        maxDiff = prices[1] - prices[0]
        minPrice = prices[0]

        #check difference each iteration and update the minimum element
        for price in prices:
            if (price - minPrice > maxDiff):
                maxDiff = price - minPrice

            if (price < minPrice):
                minPrice = price
        
        return maxDiff