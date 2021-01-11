"""
Return number that doesn't follow the cypher
"""
with open("days/day9.txt", "r") as aoc:
    data = aoc.read()
    numbers = [int(number) for number in data.split('\n')]

def getOddball(numbers):
    # Create array of previous 25
    for x in range(25, len(numbers[25:])):
        compHash = []
        last25 = numbers[(x - 25):x]
        currNum = numbers[x]
        found = False

        for y in range(0, len(last25)):
            # Add compliment to array
            if last25[y] not in compHash:
                compHash.append(currNum - last25[y])
            else:
                # Compliment seen before, checks out
                found = True
        if found:
            pass
        else:
            # Cypher broken
            return currNum
    return None

def getWeakness(target, numbers):
    # Change numbers into a set (unique)
    mySet = []
    for x in numbers:
        if x not in mySet:
            mySet.append(x)
    sum = mySet[0]
    start = 0 # left pointer
    end = 1 # right pointer
    size = len(mySet)

    while end <= size:
        if sum == target:
            solution = mySet[start:end]
            return min(solution) + max(solution)
        # Check if we move right/left pointer
        # Increment or decrement sum
        if sum > target and start < end:
            sum -= mySet[start]
            start += 1
        elif sum < target and end < size:
            sum += mySet[end]
            end += 1
    return None

print(getWeakness(33, [1, 4, 20, 3, 10, 5]))
print(getWeakness(getOddball(numbers), numbers))
