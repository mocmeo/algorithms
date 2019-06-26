def climbStairs(n):
    arr = [0 for x in range(0, n+1)]
    arr[0] = 1
    arr[1] = 1
    for x in range(2, n+1):
        arr[x] = arr[x-1] + arr[x-2]
    return arr[n]


print(climbStairs(3))
