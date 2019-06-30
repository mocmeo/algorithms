import math


def checkPerfectNumber(num):
    if (num < 0):
        return False

    if num <= 1:
        return True

    sumNum = 0
    for i in range(1, int(math.sqrt(num)+1)):
        if i == 1:
            sumNum += i
        elif num % i == 0:
            sumNum += i + int(num / i)
    return sumNum


print(checkPerfectNumber(6))
