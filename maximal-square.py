def initSumMatrix(matrix):
    n = len(matrix[0])
    m = len(matrix)
    F = [[0 for j in range(-1, n)] for i in range(-1, m)]
    F[0][0] = int(matrix[0][0])

    for i in range(1, m):
        F[i][0] = F[i-1][0] + int(matrix[i][0])
    for j in range(1, n):
        F[0][j] = F[0][j-1] + int(matrix[0][j])

    for i in range(1, m):
        for j in range(1, n):
            F[i][j] = F[i-1][j] + F[i][j-1] - F[i-1][j-1] + int(matrix[i][j])

    return F


def maximalSquare(matrix):
    if not matrix:
        return 0
    result = 0
    F = initSumMatrix(matrix)
    m = len(matrix)
    n = len(matrix[0])

    for size in range(1, min(m, n) + 1):
        for i in range(m-size+1):
            for j in range(n-size+1):
                x = i+size-1
                y = j+size-1
                subMatrix = F[x][y] - F[x][j-1] - F[i-1][y] + F[i-1][j-1]
                if subMatrix == size*size:
                    result = max(result, subMatrix)
    return result


myMatrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
# myMatrix = [["1"]]
print(maximalSquare(myMatrix))
