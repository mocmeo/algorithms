def divisiveFunc(num, base):
    while (True):
        if (num % base == 0):
            num /= base
        else:
            return num


def isUgly(num):
    if (num <= 0):
        return False
    num = divisiveFunc(num, 30)
    num = divisiveFunc(num, 15)
    num = divisiveFunc(num, 10)
    num = divisiveFunc(num, 6)
    num = divisiveFunc(num, 5)
    num = divisiveFunc(num, 3)
    num = divisiveFunc(num, 2)
    if (num > 1):
        return False
    else:
        return True


print(isUgly(2**31-1))
