def processList(myList, freq):
    for i in range(len(myList)):
        if freq.get(myList[i]) is None:
            freq[myList[i]] = [1, i]
        else:
            freq[myList[i]][0] += 1
            freq[myList[i]][1] += i
    return freq


def findRestaurant(list1, list2):
    freq = {}
    freq = processList(list1, freq)
    freq = processList(list2, freq)

    minSumIndex = 3000
    result = []
    for item in freq.keys():
        if freq[item][0] == 2:
            if minSumIndex > freq[item][1]:
                minSumIndex = freq[item][1]

    for item in freq.keys():
        if freq[item][0] == 2 and freq[item][1] == minSumIndex:
            result.append(item)

    return result


print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], [
      "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))

print(findRestaurant(["Shogun", "Tapioca Express",
                      "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))
