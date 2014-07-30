class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<=1:
            return 0
        low=0
        high=0
        profit=0
        for curr in range(1,len(prices)):
            if prices[curr]>prices[high]:
                high=curr
            elif high==low:
                high=curr
                low=curr
            else:
                profit=profit+prices[high]-prices[low]
                high=curr
                low=curr
        return profit+prices[high]-prices[low]
