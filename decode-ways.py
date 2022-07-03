def numDecodings(s):
	N = len(s)
	dp = [0]*(N+2)
	dp[N] = 1
	for i in range(N-1,-1,-1):
		if s[i] == '0':
				dp[i] = 0
		elif s[i] == '1':
			dp[i] += dp[i+1] + dp[i+2]
		elif s[i] == '2':
			dp[i] = dp[i+1]
			if i+1 < len(s) and s[i+1] <= '6':
				dp[i] += dp[i+2]
		else:
			dp[i] = dp[i+1]
	return dp[0]

print(numDecodings("1"))


	

	
