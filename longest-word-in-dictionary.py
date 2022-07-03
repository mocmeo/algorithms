class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.isEnd = False

class Trie(object):
	def __init__(self):
		self.root = TrieNode()

	def addWord(self, word):
		cur = self.root
		for ch in word:
			if ch not in cur.children:
				cur.children[ch] = TrieNode()
			cur = cur.children[ch]
		cur.isEnd = True

def longestWord(words):
	tree = Trie()
	for word in words:
		tree.addWord(word)

	words = sorted(words)[::-1]
	res = ""
	for word in words:
		flag = True
		cur = tree.root
		for ch in word:
			if not cur.children[ch].isEnd:
				flag = False
				break
			else:
				cur = cur.children[ch]

		if flag:
			if len(res) <= len(word):
				res = word
	return res

# print(longestWord(["w","wo","wor","worl","world"]))
print(longestWord(["a","banana","app","appl","ap","apply","apple"]))