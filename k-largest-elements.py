# class MaxHeap:
# 	def __init__(self):
# 		self.heap = []

# 	def push(self, data):
# 		self.heap.append(data)
# 		self.heapifyUp()

# 	def parent(self, i):
# 		return (i-1)//2

# 	def heapifyUp(self):
# 		i = len(self.heap) - 1
# 		while i != 0 and self.heap[i] > self.heap[self.parent(i)]:
# 				self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
# 				i = self.parent(i)

# 	def pop(self):
# 		if not self.heap:
# 			return False

# 		data = self.heap[0]
# 		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
# 		self.heap.pop()
# 		self.heapifyDown(0)
# 		return data

# 	def heapifyDown(self, k):
# 		smallest = k
# 		n = len(self.heap)
# 		l = 2*k + 1
# 		r = 2*k + 2

# 		if l < n and self.heap[l] > self.heap[k]:
# 			smallest = l
# 		if r < n and self.heap[r] > self.heap[smallest]:
# 			smallest = r
# 		if smallest != k:
# 			self.heap[k], self.heap[smallest] = self.heap[smallest], self.heap[k]
# 			self.heapifyDown(smallest)

# def findKthLargest(nums, k):
# 	myheap = MaxHeap()
# 	res = 0

# 	for num in nums:
# 		myheap.push(num)

# 	while k > 0:
# 		k -= 1
# 		res = myheap.pop()
# 	return res




import heapq

def findKthLargest(nums, k):
	heap = []
	for num in nums:
		heapq.heappush(heap, num)
		if len(heap) > k:
			heapq.heappop(heap)
	return heap[0]

# print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))

