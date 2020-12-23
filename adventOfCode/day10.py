"""
What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
"""

def count_jolts(chain):
    chain.sort()
    # Count 1-jolt and 3-jolt differences
    jolt1 = 0
    jolt3 = 0
    for x in range(0, len(chain) - 1):
        if chain[x] + 1 == chain[x + 1]:
            jolt1 += 1
        elif chain[x] + 3 == chain[x + 1]:
            jolt3 += 1
        else:
            pass
    # Count the source and device connection
    jolt1 = jolt1 + 1
    jolt3 = jolt3 + 1
    
    print(f"1-jolt differences: {jolt1}", f"3-jolt differences: {jolt3}")
    return jolt1 * jolt3

with open("textFiles/day10.txt", "r") as AoC:
    file = AoC.read()
    data = [int(line) for line in file.split()]  
print(count_jolts(data))
