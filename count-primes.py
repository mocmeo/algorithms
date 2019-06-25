def countPrimes(n):
    prime = [True for i in range(0, n+1)]
    p = 2

    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1

    result = 0
    for i in range(2, n):
        if (prime[i]):
            result += 1
    return result


print(countPrimes(999983))
