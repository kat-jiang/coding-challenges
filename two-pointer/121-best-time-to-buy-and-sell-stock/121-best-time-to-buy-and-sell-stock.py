# have left and right pointer
# variable to save max profit
# if left < right (means profit), calculate profit
# if not, set left to right, reason for this is we want to set left to the lowest price
# increment right counter to check next price
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        
        return max_profit