import math

def checkValid(length, s):
	if length > len(s):
		return False

	mapper = {}
	counter = 0
	for i in range(length):
		ch = s[i]

		if ch in mapper:
			mapper[ch] += 1
		else:
			counter += 1
			mapper[ch] = 1

	if counter == length:
		return True

	for i in range(len(s)-length):
		head = i + length
		tail = i
		charHead = s[head]
		charTail = s[tail]

		if ((charTail in mapper) and (mapper[charTail] > 0)):
			mapper[charTail] -= 1
			if mapper[charTail] == 0:
				counter -= 1

		if ((charHead in mapper) and (mapper[charHead] > 0)):
			mapper[charHead] += 1
		else:
			mapper[charHead] = 1
			counter += 1

		if counter == length:
			return True

	return False


def lengthOfLongestSubstring(s):
	res = 0
	l = 1
	r = len(s)+1
	while l <= r:
		mid = (l + r)//2
		if checkValid(mid, s):
			l = mid+1
			res = max(res, mid)
		else:
			r = mid - 1
	return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("abcdef"))
print(lengthOfLongestSubstring("abcdefgheaaabbbasdf"))
print(lengthOfLongestSubstring(""))




        