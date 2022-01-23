def bitwiseChar(ch):
	return 1 << (ord(ch) - ord('a'))

def countOnes(num):
	res = 0
	while num > 0:
		if num & 1:
			res += 1
		num /= 2
	return res

def canMakePaliQueries(s, queries):
	ans = []
	F = [0]*len(s)
	F[0] = bitwiseChar(s[0])
	for i in range(1, len(s)):
		F[i] = F[i-1] ^ bitwiseChar(s[i])
	
	for query in queries:
		x, y, k = query[0], query[1], query[2]
		if x == 0:
			my_str = F[y]
		else:
			my_str = F[x-1] ^ F[y]
		num1s = countOnes(my_str)

		if num1s - k*2 > 1:
			ans.append(False)
		else:
			ans.append(True)
	return ans

print(canMakePaliQueries("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))