import re
import math
from string import digits 

def day1p1():
    """ 
    Nums is our list of numbers, target is 2020 
    We return the product of the two numbers that add up to 2020
    """
    with open("day1.txt", "r") as aoc:
        data = aoc.read()
    nums = []
    for x in data.split('\n'):
        nums.append(int(x))
    
    target = 2020

    compHash = {}
    result = []
    for index, num in enumerate(nums):
        # Add compliment to dictionary with index
        if compHash.get(num) is None:
            compHash[target - num] = index
        else:
            # Compliment seen before, solution found [index of compliment, index of current num]
            result = [compHash[num], index]
            break

    return nums[result[0]] * nums[result[1]]


def day1p2():
    """ 
    Nums is our list of numbers, target is 2020 
    We return the product of the three numbers that add up to 2020
    """
    with open("day1.txt", "r") as aoc:
        data = aoc.read()
    nums = []
    for x in data.split('\n'):
        nums.append(int(x))
    target = 2020

    # For first element nums[0]
    for x in range(0, len(nums) - 2):
        # For second element nums[1]
            for y in range(x + 1, len(nums) - 1):
            # For third element nums[2]
                for z in range(y + 1, len(nums)):
                    if nums[x] + nums[y] + nums[z] == target:
                        threeNums = [nums[x], nums[y], nums[z]]
                        return threeNums[0] * threeNums[1] * threeNums[2]
    return False


def day2p1():
    """
    How many passwords are valid according to their policies?
    """
    with open("day2.txt", "r") as aoc:
        data = aoc.read()
    pass_policies = data.split('\n')

    validCount = 0
    for entry in pass_policies:
        print(entry)
        entrySplit = entry.split(' ')
        print(entrySplit)

        letter = entrySplit[1].split(':')[0]
        password = entrySplit[2]
        nums = entrySplit[0].split('-')
        minNum = int(nums[0])
        maxNum = int(nums[1])
        passCount = password.count(letter)
        print(f"Minimum number is {minNum}", f"Maximum number is {maxNum}",
            f"Password is {password}", f"Letter is {letter}")

        
        print(passCount)
        # Check if password is valid
        if passCount >= minNum and passCount <= maxNum:
            validCount += 1
        else:
            pass

    return validCount


def day2p2():
    """
    How many passwords are valid according to their policies?
    """
    with open("day2.txt", "r") as aoc:
        data = aoc.read()
    pass_policies = data.split('\n')

    # Our number of valid passwords
    validCount = 0
    # Check if letter occurs more than once
    passCheck = 1

    for entry in pass_policies:
        # Number of times letter occurs at indexes
        currLetterNum = 0
        entrySplit = entry.split(' ')
    
        letter = entrySplit[1].split(':')[0]
        password = entrySplit[2]
        nums = entrySplit[0].split('-')
        index1 = int(nums[0]) - 1
        index2 = int(nums[1]) - 1
        
        print(f"First index is {index1}", f"Second index is {index2}",
              f"Password is {password}", f"Letter is {letter}")

        # Check indexes for letter
        if password[index1] == letter:
            currLetterNum += 1
        if password[index2] == letter:
            currLetterNum += 1
    
        # Check if password is valid
        if currLetterNum == passCheck:
            validCount += 1

    return validCount


def day3p1():
    """
    Check how many trees we hit on the slope
    """
    with open("day3.txt", "r") as aoc:
        data = aoc.read()
    forest = data.split('\n')

    treesHit = 0
    wForest = len(forest[0]) - 1
    hForest = len(forest) - 1
    x, y = 0, 0

    print(f"height of forest is {hForest}, width of forest is {wForest}")

    while y < hForest:
        x += 3
        y += 1
        print(forest[y])
        # Extend forest
        if x > wForest:
            x = x - 31
        # Check if we hit a tree
        if forest[y][x] == "#":
            treesHit += 1
    return treesHit


def day3p2():
    """
    Check how many trees we hit on the slope
    """
    with open("day3.txt", "r") as aoc:
        data = aoc.read()
    forest = data.split('\n')

    treesHit = 0
    wForest = len(forest[0]) - 1
    hForest = len(forest) - 1
    x, y = 0, 0
    
    print(f"height of forest is {hForest}, width of forest is {wForest}")

    tests = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    product = 1
    for test in tests:
        # Reset trees hit for each test suite
        treesHit = 0
        x, y = 0, 0
        while y < hForest:
            x += test[0]
            y += test[1]

            print(forest[y])
            # Extend forest
            if x > wForest:
                x = x - 31
            # Check if we hit a tree
            if forest[y][x] == "#":
                treesHit += 1
        product *= treesHit

    return product


def day4p1():
    """
    Return valid passports
    Passport is valid if length is 8 or length is 7 and cid is missing
    """
    with open("day4.txt", "r") as aoc:
        data = aoc.read()
    passportData = data.split('\n\n')
    validPassports = 0

    for info in passportData:
        # Array of strings
        info = info.replace('\n', ' ')

        # Check if valid passport
        if len(info.split()) == 8:
            validPassports += 1
        elif len(info.split()) == 7 and 'cid' not in info:
            validPassports += 1

    return validPassports


def day4p2():
    """
    Return valid passports
    Passport validity is based on regex
    """

    with open("day4.txt", "r") as aoc:
        data = aoc.read()
    passportData = data.split('\n\n')
    validPassports = 0

    for info in passportData:
        # Array of strings
        info = info.replace('\n', ' ')

        # Check validity
        hcl = re.search("hcl:#[0-9a-f]{6}( |$)", info)
        pid = re.search("pid:[0-9]{9}( |$)", info)
        byr = re.search("byr:(19[2-9][0-9]|200[0-2])( |$)", info)
        iyr = re.search("iyr:(201[0-9]|2020)( |$)", info)
        eyr = re.search("eyr:(202[0-9]|2030)( |$)", info)
        hgt = re.search(
            "(1([5-8][0-9]|9[0-3])cm)|(([^1]59|[^1]6[0-9]|[^1]7[0-6])in)( |$)", info)
        ecl = re.search(
            "ecl:(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)( |$)", info)

        if byr and iyr and eyr and ecl and pid and hcl and hgt:
            print(info)
            validPassports += 1
    
    return validPassports


def day5p1():
    """
    Return highest boarding pass ID
    """
    with open("day5.txt", "r") as aoc:
        data = aoc.read()
    boardPassData = data.split('\n')
    results = []

    for ourPass in boardPassData:
        ### Binary search
        ## Establish variables
        lower1 = 0
        upper1 = 127
        lower2 = 0
        upper2 = 7

        ## Change upper/lower bounds
        for letter in ourPass:
            # if 'F' change the upper bound to be the mid point
            if letter == 'F':
                upper1 = (lower1 + upper1) // 2
                row = upper1
            # if 'B' change the lower bound to be the mid point
            if letter == 'B':
                lower1 = math.ceil((lower1 + upper1) / 2)
                row = lower1
            # if 'L' change the upper bound to be the mid point
            if letter == 'L':
                upper2 = (lower2 + upper2) // 2
                col = upper2
            # if 'R' change the lower bound to be the mid point
            if letter == 'R':
                lower2 = math.ceil((lower2 + upper2) / 2)
                col = lower2
        results.append(row * 8 + col)

    return max(results)


def day5p2():
    """
    Return highest boarding pass ID
    """
    with open("day5.txt", "r") as aoc:
        data = aoc.read()
    boardPassData = data.split('\n')
    results = []

    for ourPass in boardPassData:
        ### Binary search
        ## Establish variables
        lower1 = 0
        upper1 = 127
        lower2 = 0
        upper2 = 7

        ## Change upper/lower bounds
        for letter in ourPass:
            # if 'F' change the upper bound to be the mid point
            if letter == 'F':
                upper1 = (lower1 + upper1) // 2
                row = upper1
            # if 'B' change the lower bound to be the mid point
            if letter == 'B':
                lower1 = math.ceil((lower1 + upper1) / 2)
                row = lower1
            # if 'L' change the upper bound to be the mid point
            if letter == 'L':
                upper2 = (lower2 + upper2) // 2
                col = upper2
            # if 'R' change the lower bound to be the mid point
            if letter == 'R':
                lower2 = math.ceil((lower2 + upper2) / 2)
                col = lower2
        results.append(row * 8 + col)

    results.sort()
    for x in range(0, len(results) - 1):
        if results[x] + 1 != results[x + 1]:
            return results[x] + 1
    return None


def day6p1():
    """
    Return total unique survey questions answered
    """
    with open("day6.txt", "r") as aoc:
        data = aoc.read()
    surveyData = data.split('\n\n')
    # Total unique answers
    total = 0
    for group in surveyData:
        surveyExample = group.split()
        letters = []
        
        for survey in surveyExample:
            for letter in survey:
                if letter not in letters:
                    letters.append(letter)
                    total += 1
                else:
                    pass
        
    return total


def day6p2():
    """
    Return total unique survey questions answered
    """
    with open("day6.txt", "r") as aoc:
        data = aoc.read()
    answers = data.split('\n\n')
    total = 0
    
    # Loop over array of strings
    for answer in answers:
        list = answer.split('\n')
        answer_dict = {}

        # Loop over array of strings
        for person in list:
            # Loop over the string
            for letter in person:
                # Check if letter already in dictionary
                if answer_dict.get(letter) is None:
                    answer_dict[letter] = 1
                # If already exists, add one
                else:
                    answer_dict[letter] += 1

        # Check if the values are equal to the height of the array
        for key in answer_dict:
            if answer_dict[key] == len(list):
                total += 1

    return total


def main():
    # Note: day 7, 9 are in a different python files
    print(day9p1())

if __name__ == '__main__':
    main()
