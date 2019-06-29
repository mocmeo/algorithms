class NumArray(object):

    def __init__(self, nums):
        if (len(nums) == 0):
            self.sumList = []
        else:
            self.sumList = [0 for i in range(-1, len(nums))]
            self.sumList[0] = nums[0]

            for i in range(1, len(nums)):
                self.sumList[i] = self.sumList[i-1] + nums[i]

    def sumRange(self, i, j):
        if (len(self.sumList) == 0):
            return 0
        return self.sumList[j] - self.sumList[i-1]


obj = NumArray([])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
