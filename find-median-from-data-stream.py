import heapq

class MedianFinder(object):
    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num):
        heapq.heappush(self.small_heap, 0-num)

        if self.small_heap and self.large_heap and -self.small_heap[0] > self.large_heap[0]:
            heapq.heappush(self.large_heap, 0-heapq.heappop(self.small_heap))

        if len(self.small_heap) > len(self.large_heap) + 1:
            heapq.heappush(self.large_heap, 0-heapq.heappop(self.small_heap))

        if len(self.large_heap) > len(self.small_heap) + 1:
            heapq.heappush(self.small_heap, 0-heapq.heappop(self.large_heap))
        

    def findMedian(self):
        if len(self.small_heap) > len(self.large_heap):
            return 0-self.small_heap[0]
        if len(self.small_heap) < len(self.large_heap):
            return self.large_heap[0]
        return (0-self.small_heap[0] + self.large_heap[0])*0.5

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
print(obj.findMedian())