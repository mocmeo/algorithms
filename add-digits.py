def sumDigits(n):
    result = 0
    while (n > 0):
        lastDigit = n % 10
        result += lastDigit
        n = int(n / 10)
    return result


def addDigits(n):
    while (n >= 10):
        n = sumDigits(n)
    return n


print(addDigits(38))
