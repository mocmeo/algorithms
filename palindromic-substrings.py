def countSubstrings(s):
    if not s:
        return 0
    n = len(s)
    F = [[1]*n for i in range(n)]
    A = [[False]*n for i in range(n)]

    # Base cases
    A[0][0] = True
    for i in range(1, n):
        A[i][i] = True
        if s[i-1] == s[i]:
            A[i-1][i] = True

    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                if A[i+1][j-1]:
                    A[i][j] = True
                if length == 2:
                    F[i][j] = 3
                else:
                    F[i][j] = F[i+1][j] + F[i][j-1] - \
                        F[i+1][j-1] + (1 if A[i+1][j-1] else 0)
            else:
                F[i][j] = F[i+1][j] + F[i][j-1] - \
                    (0 if length == 2 else F[i+1][j-1])
    return F[0][-1]


print(countSubstrings(""))
