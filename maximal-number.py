def solve(n, string):
    result = "-1"
    if not string:
        return result

    result = "".join(sorted(string))
    print(result[::-1])


solve(3, "321")
