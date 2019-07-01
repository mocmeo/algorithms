import math


def judgeSquareSum(c):
    for x in range(int(math.sqrt(c) + 1)):
        y = c - x*x
        sqrt_y = int(math.sqrt(y))
        if sqrt_y*sqrt_y == y:
            return True
    return False


print(judgeSquareSum(3))
