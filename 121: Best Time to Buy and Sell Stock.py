class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit from one buy and one sell.
        
        Approach: Track the minimum price seen so far and compute max profit at each step.
        Single pass ensures efficiency.
        """
        if not prices:
            return 0  # Edge case: empty array
        
        min_price = prices[0]  # Track minimum price seen
        max_profit = 0  # Track maximum profit possible
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price  # Update buy point
            else:
                max_profit = max(max_profit, price - min_price)  # Update profit if selling here
        
        return max_profit