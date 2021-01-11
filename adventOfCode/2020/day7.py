"""
How many bag colors contain at least one shiny gold bag?
"""

with open("day7.txt", "r") as aoc:
    data = aoc.read()
    data = data.split('\n')

# Returns a list of how many bags hold this color
def get_bags(color):
    # Lines that contain color
    lines = [line for line in data if color in line and line.index(color) != 0]
    
    
    # All colors we've checked
    allCol = []

    # No bags contain color
    if len(lines) == 0:
        return []

    # Get bags that contain our color
    else:
        for line in lines:
            print(line)
        colors = [line.split(' bags')[0] for line in lines]
        # Only colors that haven't been checked before
        colors = [color for color in colors if color not in allCol ]

        for color in colors:
            print(color)
            # Start off with our unique bags
            allCol.append(color)
            bags = get_bags(color)

            # Merge together
            allCol += bags

        # Get unique bags
        uniqueColors = []
        for color in allCol:
            if color not in uniqueColors:
                uniqueColors.append(color)

        return uniqueColors

colors = get_bags('shiny gold')
print(len(colors))
