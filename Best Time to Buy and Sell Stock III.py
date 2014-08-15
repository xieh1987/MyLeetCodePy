class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        minprice, DP = prices[0], []
        for i in range(len(prices)):
            if i==0:
                DP.append(0)
            else:
                minprice = min(minprice, prices[i])
                DP.append(max(prices[i]-minprice, DP[i-1]))
        maxprice, maxprofit, profit2 = prices[-1], 0, 0
        for j in reversed(range(1,len(prices))):
            if j==len(prices)-1:
                maxprofit = DP[len(prices)-1]
            else:
                maxprice = max(maxprice, prices[j])
                profit2 = max(profit2, maxprice-prices[j])
                maxprofit=max(maxprofit, profit2+DP[j-1])
        return maxprofit
