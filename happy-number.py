def sumSquares(n):
    result = 0
    while (n > 0):
        lastDigit = n % 10
        result += lastDigit * lastDigit
        n = int(n / 10)
    return result


def isHappy(n):
    happyArr = [False for i in range(0, 10000)]
    while (n != 1):
        n = sumSquares(n)
        if (happyArr[n] == True):
            return False
        else:
            happyArr[n] = True
    return True


print(isHappy(19))
