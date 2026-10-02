class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        for i in range(len(prices)-1):
            if prices[i]>=prices[i+1]:
                profit = profit + 0 
            else:
                profit += prices[i+1]-prices[i]

        return profit
