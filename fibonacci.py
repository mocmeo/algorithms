def fib(N):
    F = [0 for i in range(N+1)]
    F[0], F[1] = 0, 1

    for i in range(2, N+1):
        F[i] = F[i-1] + F[i-2]
    return F[N]


print(fib(4))
