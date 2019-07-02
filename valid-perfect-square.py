def isPerfectSquare(num):
    for x in range(1, 100000):
        if x*x == num:
            return True
    return False


print(isPerfectSquare(15))
