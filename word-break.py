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


def wordBreak(s, wordDict):
	F = [[False for i in range(len(s))] for j in range(len(s))] 
	t = Trie()
	for word in wordDict:
		t.insert(word)

	for i in range(len(s)):
		for j in range(i, len(s)):
			if len(s[i:j+1]):
				F[i][j] = t.search(s[i:j+1])

	for i in range(len(s)-1):
		for j in range(i+1, len(s)):
			if F[0][i] and t.search(s[i+1:j+1]):
				F[0][j] = True

	return F[0][len(s)-1]

print(wordBreak("leetcode", ["leet","code"]))
print(wordBreak("applepenapple", ["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(wordBreak("ab", ["a", "b"]))
print(wordBreak("baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))