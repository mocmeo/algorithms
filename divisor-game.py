def divisorGame(N):
    arr = [False]*(N+1)
    arr[2] = True
    arr[3] = False
    if (N <= 3):
        return arr[N]

    for i in range(4, N+1):
        for j in range(1, i):
            if (j != 0 and i % j == 0):
                arr[i] = arr[i] or (not arr[i-j])
    return arr[N]


print(divisorGame(10))
