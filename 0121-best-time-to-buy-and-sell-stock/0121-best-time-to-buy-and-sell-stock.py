class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_price= 0
        for price in prices:
            if min_price > price:
                min_price = price
            if price - min_price > max_price :
                max_price = price - min_price
        return max_price   