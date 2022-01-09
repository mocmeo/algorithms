def capitalizeTitle(title):
	words = title.lower().split(" ")
	res = []
	for word in words:
		if len(word) < 3:
			res.append(word.lower())
		else:
			res.append(word.capitalize())
	return " ".join(res)

print(capitalizeTitle("First leTTeR of EACH Word"))
print(capitalizeTitle("capiTalIze tHe titLe"))