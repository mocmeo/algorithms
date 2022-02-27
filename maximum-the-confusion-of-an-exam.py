def maxAnswer(key, answers, k):
	sum_arr = 0
	S = []
	left = -1
	res = 0
	for i in range(len(answers)):
		if answers[i] == key:
			sum_arr += 1
		S.append(sum_arr)

		if (i - left - sum_arr) > k:
			left += 1
			sum_arr -= 1 if answers[left] == key else 0
		res = max(res, i - left)
	return res

def maxConsecutiveAnswers(answerKey, k):
	ans = 0
	ans = max(ans, maxAnswer('T', answerKey, k))
	ans = max(ans, maxAnswer('F', answerKey, k))

	return ans

print(maxConsecutiveAnswers("TTFTTFTT", 1))
print(maxConsecutiveAnswers("TFFT", 1))
print(maxConsecutiveAnswers("TTFF", 2))
