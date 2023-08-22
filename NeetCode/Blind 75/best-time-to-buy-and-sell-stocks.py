class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            potentialProfit = prices[i] - minPrice
            if maxProfit < potentialProfit:
                maxProfit = potentialProfit

            if prices[i] < minPrice:
                minPrice = prices[i]

        return maxProfit
