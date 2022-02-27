def parseStr(domain):
	res = [domain]
	for i in range(len(domain)):
		if domain[i] == '.':
			res.append(domain[i+1:])
	return res

def subdomainVisits(cpdomains):
	mapper = {}
	for cpdomain in cpdomains:
		cnt, domain = cpdomain.split(" ")
		arr = parseStr(domain)

		for item in arr:
			mapper[item] = mapper.get(item, 0) + int(cnt)

	res = []
	for item in mapper:
		res.append(str(mapper[item]) + " " + item)
	return res

print(subdomainVisits(["9001 discuss.leetcode.com"]))
print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

