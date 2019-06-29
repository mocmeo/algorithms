def swap(str, i, j):
    c = list(str)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)


def buddyStrings(A, B):
    if (len(A) != len(B)):
        return False
    if (A == B):
        if len(set(A)) < len(A):
            return True
        else:
            return False

    indexArr = []
    for i in range(0, len(A)):
        if (A[i] != B[i]):
            indexArr.append(i)

    if (len(indexArr) != 2):
        return False

    i, j = indexArr[0], indexArr[1]
    return swap(A, i, j) == B


def buddyStrings2(A, B):
    if (A == B):
        if len(set(A)) < len(A):
            return True
        else:
            return False

    a = []
    b = []
    for i in range(len(A)):
        if A[i] != B[i]:
            a.append(A[i])
            b.append(B[i])

    a.reverse()
    if len(a) == len(b) == 2 and a == b:
        return True
    return False


print(buddyStrings2("ba", "ab"))
