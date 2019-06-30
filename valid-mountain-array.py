def validMountainArray(A):
    if (len(A) < 3):
        return False

    ascending = True
    for i in range(1, len(A)):
        if (ascending and A[i] < A[i-1]):
            ascending = False
            if i == 1:
                return False
        if (not ascending and A[i] >= A[i-1]):
            return False

    if (ascending):
        return False
    return True


print(validMountainArray([0, 3, 2, 1]))
