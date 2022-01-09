def canBeValid(s, locked):
	cur_sum = 0
	new_s = ""
	for i in range(len(s)):
		if s[i] == ")":
			cur_sum -= 1
			if cur_sum < 0 and locked[i] == '1':
				return False
			if cur_sum < 0 and locked[i] == '0':
				cur_sum += 2
				new_s += "("
			else:
				new_s += ")"
		else:
			cur_sum += 1
			new_s += "("

	if cur_sum == 0: return True
	# cur_sum > 0

	for i in range(len(new_s)-1,-1,-1):
		if s[i] == "(":
			cur_sum += 1
			if cur_sum > 0 and locked[i] == '1':
				return False
			if cur_sum > 0 and locked[i] == '0':
				cur_sum -= 2
		else:
			cur_sum -= 1

	if cur_sum == 0: return True
	return False

# print(canBeValid("))()))", "010100"))
# print(canBeValid("()()", "0000"))
# print(canBeValid(")", "0"))
# print(canBeValid("((()", "0000"))
# print(canBeValid(")(", "00"))
print(canBeValid("(", "0"))