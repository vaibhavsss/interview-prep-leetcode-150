"""
You are given an integer array prices 
where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time. 
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold than one share of the stock.

Find and return the maximum profit you can achieve.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))