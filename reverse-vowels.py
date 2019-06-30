def reverseVowels(s):
    vowelIndex = []
    reverse_s = list(s)

    for i in range(0, len(s)):
        if (s[i] in "ueoaiUEOAI"):
            vowelIndex.append(i)

    for x in range(0, int(len(vowelIndex) / 2)):
        i = vowelIndex[x]
        j = vowelIndex[len(vowelIndex)-x-1]
        reverse_s[i], reverse_s[j] = reverse_s[j], reverse_s[i]
    return "".join(reverse_s)


print(reverseVowels("ae"))
