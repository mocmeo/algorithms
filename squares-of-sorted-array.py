def sortedSquares(A):
    squares = list(map(lambda x: x*x, A))
    squares.sort()
    return squares


def sortedSquares2(A):
    answer = []
    l, r = 0, len(A) - 1
    while (l <= r):
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.append(left * left)
            l += 1
        else:
            answer.append(right * right)
            r -= 1
    answer.reverse()
    return answer


print(sortedSquares2([-7, -3, 2, 3, 11]))
