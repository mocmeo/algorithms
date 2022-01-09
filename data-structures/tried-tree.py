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
			index = self.charToIndex(word[level])

			if not pt.children[index]:
				pt.children[index] = self.getNode()
			pt = pt.children[index]

		pt.isEndOfWord = True

	def search(self, word):
		pt = self.root 
		length = len(word)

		for level in range(length):
			index = self.charToIndex(word[level])

			if not pt.children[index]:
				return False
			pt = pt.children[index]

		return pt.isEndOfWord
			
	def startsWith(self, prefix):
		pt = self.root 
		length = len(prefix)

		for level in range(length):
			index = self.charToIndex(prefix[level])

			if not pt.children[index]:
				return False
			pt = pt.children[index]

		return True

keys = ["the","a","there","anaswe","any",
            "by","their"]
t = Trie()
for key in keys:
  t.insert(key)

print(t.search('theres'))

