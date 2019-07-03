import math


def repeatedSubstringPattern(s):
    if not s:
        return False

    n = len(s)
    primes = getPrimes()
    for k in primes:
        if n < k:
            break
        if n % k == 0:
            strDict = {}
            lenSubstr = n / k
            for i in range(k):
                start = int(lenSubstr*i)
                end = int(lenSubstr*(i+1))
                strS = s[start:end]
                if strDict.get(strS) is None:
                    strDict[strS] = 1
                else:
                    strDict[strS] += 1
            if len(strDict.keys()) == 1:
                return True

    return False


def getPrimes():
    result = [2, 3]
    for i in range(4, 101):
        isPrime = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                isPrime = False
        if isPrime:
            result.append(i)
    return result


print(repeatedSubstringPattern("abcabcabcabc"))
