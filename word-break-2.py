class TrieNode:
	def __init__(self):
		self.children = [None]*26
		self.isEndOfWord = False

class Trie:
	def __init__(self):
		self.root = self.getNode()

	def getNode(self):
		return TrieNode()

	def charToIndex(self, ch):
		return ord(ch) - ord('a')

	def insert(self, word):
		pt = self.root
		
		for level in range(len(word)):
			index = self.charToIndex(word[level])

			if not pt.children[index]:
				pt.children[index] = self.getNode()
			pt = pt.children[index]

		pt.isEndOfWord = True

	def search(self, word):
		pt = self.root

		for level in range(len(word)):
			index = self.charToIndex(word[level])

			if not pt.children[index]:
				return False
			pt = pt.children[index]
		
		return pt.isEndOfWord

def backtrack(F, s, idx, cache, res):
	for i in range(idx, -1, -1):
		if F[i][idx]:
			cache.append(s[i:idx+1])

			if i == 0:
				res.append(" ".join(cache[::-1]))
			else:
				backtrack(F, s, i-1, cache, res)
			cache.pop()

def wordBreak(s, wordDict):
	F = [[False for i in range(len(s))] for j in range(len(s))] 
	t = Trie()
	for word in wordDict:
		t.insert(word)

	for i in range(len(s)):
		for j in range(i, len(s)):
			if len(s[i:j+1]):
				F[i][j] = t.search(s[i:j+1])

	res = []
	backtrack(F, s, len(s)-1, [], res)

	return res

print(wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
print(wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))