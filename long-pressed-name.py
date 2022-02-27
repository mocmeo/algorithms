def isLongPressedName(name, typed):
	i = 0
	j = 0
	while i < len(name) and j < len(typed):
		if name[i] == typed[j]:
			i += 1
			j += 1
		else:
			if j > 0 and typed[j] == typed[j-1]:
				while j < len(typed) and typed[j] == typed[j-1]:
					j += 1
			else:
				return False
	if i < len(name):
		return False
	for i in range(j, len(typed)):
		if typed[i] != name[-1]:
			return False
	return True


print(isLongPressedName("alex", "aaleex"))
print(isLongPressedName("saeed", "ssaaedd"))
print(isLongPressedName("alex", "alexa"))
print(isLongPressedName("alex", "aaleelx"))
print(isLongPressedName("leelee", "lleeelleee"))
print(isLongPressedName("a", "b"))
print(isLongPressedName("alex", "aaleexeex"))
print(isLongPressedName("alex", "aaleex"))