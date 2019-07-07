def validNums(nums):
    for num in nums:
        if num < 1 or num > 9:
            return False
    return True


def numMagicSquaresInside(grid):
    count = 0
    m = len(grid)
    n = len(grid[0])
    if m*n < 9:
        return 0
    for i in range(0, m-2):
        for j in range(0, n-2):
            nums = []
            nums.append(grid[i][j])
            nums.append(grid[i+1][j])
            nums.append(grid[i+2][j])
            nums.append(grid[i][j+1])
            nums.append(grid[i+1][j+1])
            nums.append(grid[i+2][j+1])
            nums.append(grid[i][j+2])
            nums.append(grid[i+1][j+2])
            nums.append(grid[i+2][j+2])
            if len(set(nums)) != 9:
                continue
            if not validNums(nums):
                continue

            sumGrid = grid[i][j] + grid[i+1][j] + grid[i+2][j]
            if (grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] == sumGrid and
                grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] == sumGrid and
                grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] == sumGrid and
                grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] == sumGrid and
                grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == sumGrid and
                    grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] == sumGrid):
                count += 1
    return count


# print(numMagicSquaresInside([[4, 3, 8, 4],
#                              [9, 5, 1, 9],
#                              [2, 7, 6, 2]]))

print(numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]]))
