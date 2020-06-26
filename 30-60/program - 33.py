# Best Time to Buy and Sell Stock II

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 0: return 0
#         profit = 0
#         for i in range(1, len(prices)):
#             localMaxima = prices[i] - prices[i - 1]
#             if localMaxima > 0:
#                 profit += localMaxima
#         return profit


def maxProfit(prices:list):
    i = 0
    valley = prices[0]
    peak = prices[0]
    profit = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i+1]:
            i += 1
        valley = prices[i]
        while i < len(prices) - 1 and prices[i] <= prices[i+1]:
            i += 1
        peak = prices[i]
        profit += peak - valley
    return profit

lis_ = [int(x) for x in input().split()]
print(maxProfit(lis_))