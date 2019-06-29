import sys


def maxProfit(prices):
    if (len(prices) == 1):
        return 0

    result = 0
    current_max = -sys.maxsize
    arr = [0 for x in range(-10, len(prices))]

    for i in range(1, len(prices)):
        current_max = max(current_max, arr[i-2] - prices[i-1])
        arr[i] = max(arr[i], arr[i-1], current_max + prices[i])
        result = max(result, arr[i])
    return result


print(maxProfit([7, 6, 4, 3, 1]))
