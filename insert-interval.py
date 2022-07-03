def insert(intervals, newInterval):
	start = -1
	end = -1
	for i in range(len(intervals)):
		cur = intervals[i]
		if cur[1] >= newInterval[0] and start == -1:
			start = i
		if newInterval[1] >= cur[0]:
			end = i
	
	if start == -1:
		intervals.append(newInterval)
		return intervals
	if end == -1:
		intervals.insert(0, newInterval)
		return intervals

	if start > 0:
		left = intervals[0:start]
	else:
		left = []

	if end < len(intervals):
		right = intervals[end+1:len(intervals)]
	else:
		right = []
	mid = [min(intervals[start][0], newInterval[0]), max(intervals[end][1], newInterval[1])]
	return left + [mid] + right

print(insert([[1,3],[6,9]], [2,5]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))