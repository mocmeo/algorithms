def intersect(S1, S2):
    if (S1[1] >= S2[0] and S1[0] <= S2[0]) or (S1[0] <= S2[1] and S1[0] >= S2[0]):
        return True


def intervalIntersection(A, B):
    result = []

    for y in range(len(B)):
        tmp_x = 0
        for x in range(tmp_x, len(A)):
            if intersect(A[x], B[y]):
                i = max(A[x][0], B[y][0])
                j = min(A[x][1], B[y][1])
                result.append([i, j])
                tmp_x = x
            else:
                continue
    return result


print(intervalIntersection([[0, 2], [5, 10], [13, 23], [
      24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
