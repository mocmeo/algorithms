def isPowerOfTwo(n):
    if (n == 1):
        return True

    checkNum = 1
    while (checkNum < n):
        checkNum *= 2
        if (checkNum == n):
            return True
    return False


print(isPowerOfTwo(2))
