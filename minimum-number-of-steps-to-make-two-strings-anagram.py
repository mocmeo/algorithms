from collections import Counter

def minSteps(s, t):
	cntS, cntT = Counter(s), Counter(t)
	res = 0
	for i in cntT:
		if cntT[i] >= cntS[i]:
			res += cntT[i] - cntS[i]

	return res

print(minSteps("leetcode", "practice"))
print(minSteps("bab", "aba"))

		
