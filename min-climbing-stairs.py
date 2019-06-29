import sys


def minCostClimbingStairs(cost):
    if not cost:
        return 0
    if (len(cost) <= 2):
        return cost[-1]

    F = [sys.maxsize for x in range(0, len(cost) + 1)]
    F[0], F[1] = cost[0], cost[1]

    for i in range(2, len(cost) + 1):
        if (i == len(cost)):
            current_cost = 0
        else:
            current_cost = cost[i]
        F[i] = min(F[i-1], F[i-2]) + current_cost
    return F[len(cost)]


print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
