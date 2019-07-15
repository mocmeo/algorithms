def toGoatLatin(S):
    words = S.strip().split()
    suffix = ""

    result = []
    for word in words:
        suffix += "a"
        if word.lower()[0] in "ueoai":
            result.append(word + "ma" + suffix)
        else:
            result.append(word[1:] + word[0] + "ma" + suffix)
    return " ".join(result)


# print(toGoatLatin("I speak Goat Latin"))
# print(toGoatLatin("The quick brown fox jumped over the lazy dog"))
print(toGoatLatin(""))
