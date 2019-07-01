def lastStoneWeight(stones):
    stones.sort()

    while len(stones) >= 2:
        s1, s2 = stones.pop(), stones.pop()
        newStone = abs(s1 - s2)
        if (newStone > 0):
            stones.append(newStone)
            stones.sort()

    return stones[0] if len(stones) else 0


print(lastStoneWeight([2, 3]))
