import sys


def maxProfit(prices):
    if (not prices):
        return 0

    result = 0
    current_min = prices[0]
    for i in range(1, len(prices)):
        result = max(result, prices[i] - current_min)
        current_min = min(current_min, prices[i])
    return result


print(maxProfit([1]))
