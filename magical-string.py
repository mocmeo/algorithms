def genStr(my_str):
	new_str = ""
	flag = True # T=1, F=2
	for ch in my_str:
		if flag:
			new_str += "1" if ch == "1" else "11"
		else:
			new_str += "2" if ch == "1" else "22"
		flag = not flag
	return new_str

def magicalString(n):
	my_str = "1221121221221121122"
	res = 0
	while len(my_str) < 100000:
		my_str = genStr(my_str)

	for ch in my_str[0:n]:
		if ch == "1":
			res += 1

	return res

print(magicalString(1000))
