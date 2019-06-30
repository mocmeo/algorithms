def longestPalindromeSubseq(s):
    n = len(s)
    F = [[1]*n for i in range(n)]

    result = 1
    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                if (length == 2):
                    F[i][j] = 2
                else:
                    F[i][j] = max(F[i][j], F[i+1][j-1] + 2)
            else:
                F[i][j] = max(F[i+1][j], F[i][j-1])
            result = max(result, F[i][j])

    return result


print(longestPalindromeSubseq("aaa"))
# print(longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"))
