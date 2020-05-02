marksheet = []
scoresheet = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name, score])
        scoresheet.append(score)

    # Make a set so there are no duplicate scores
    # Obtain the second lowest grade (index 1) descending
    x = sorted(set(scoresheet))[1]

    for name, score in sorted(marksheet):
        # If score is equal to the second lowest, print
        if score == x:
            print(name)
