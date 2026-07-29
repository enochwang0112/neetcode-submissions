class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_so_far = 0

        for price in prices:
            min_so_far = min(min_so_far, price)
            max_so_far = max(max_so_far, price - min_so_far)
        
        return max_so_far