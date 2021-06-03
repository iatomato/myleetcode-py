class Solution:
    def max_profit(self, prices) -> int:
        count_profit = 0
        for _index in range(len(prices) - 1):
            if (prices[_index] < prices[_index + 1]):
                count_profit += prices[_index + 1] - prices[_index]
        return (prices, count_profit)
