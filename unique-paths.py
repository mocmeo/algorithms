def uniquePaths(m, n):
    F = [[0]*n for i in range(m)]
    for i in range(m):
        F[i][0] = 1
    for j in range(n):
        F[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            F[i][j] = F[i-1][j] + F[i][j-1]
    return F[-1][-1]


print(uniquePaths(1, 1))
