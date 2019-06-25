def reverseNumber(n):
    result = 0
    while (n > 0):
        lastDigit = n % 10
        result = result*10 + lastDigit
        n = int(n / 10)

    if (result > 2**31 - 1):
        return 0
    return result


def reverse(x):
    sign = 1
    if (x < 0):
        sign = -1
        x = abs(x)
    return reverseNumber(x) * sign


print(reverse(1534236469))
