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
		length = len(word)

		for level in range(length):
			index = self.charToIndex[]