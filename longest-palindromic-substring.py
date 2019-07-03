def longestPalindrome(s):
    if not s:
        return ""
    n = len(s)
    F = [[False]*n for i in range(n)]

    # Base cases
    F[0][0] = True
    for i in range(1, n):
        F[i][i] = True
        if s[i-1] == s[i]:
            F[i-1][i] = True

    result = 0
    x = y = 0
    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                if (F[i+1][j-1]):
                    F[i][j] = True
            if F[i][j] and result < length:
                result = length
                x, y = i, j

    return s[x:y+1]


print(longestPalindrome("babad"))
