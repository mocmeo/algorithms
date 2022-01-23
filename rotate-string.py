def rotateString(s, goal):
	doubleS = s + s
	if goal in doubleS:
		return True

	return False

print(rotateString("abcde", "cdeab"))
print(rotateString("abcde", "abced"))
