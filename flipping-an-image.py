def flipAndInvertImage(A):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        A[i] = list(reversed(A[i]))
        for j in range(n):
            A[i][j] = 1-A[i][j]
    return A


print(flipAndInvertImage(
    [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
