class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        minPrice=prices[0]
        maxProfit=0
        for price in range(len(prices)):
            minPrice=min(minPrice, prices[price])
            maxProfit=max(maxProfit, prices[price]-minPrice)
        return maxProfit
