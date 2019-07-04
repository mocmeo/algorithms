def mincostTickets(days, costs):
    # Prevent the assumption cost[0] < cost[1] < cost[2] not holds (e.g. [15, 2, 7])
    for i in range(len(costs)):
        costs[i] = min(costs[i:])

    # Note that F[i] represents the min cost of days[i-1]
    n = len(days)
    F = [float('inf')]*(n+1)
    F[0] = 0

    for i in range(1, n+1):
        for j in range(i):
            gap = days[i-1] - days[j] + 1
            if gap > 30:
                continue
            elif gap == 1:
                F[i] = min(F[i], F[j] + costs[0])
            elif gap <= 7:
                F[i] = min(F[i], F[j] + costs[1])
            else:
                F[i] = min(F[i], F[j] + costs[2])

    return F[-1]


print(mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
