# Find a 6 digit number that starts with 100, and is divisble by 9127
for i in range(100000, 101000):
    if i % 9127 == 0:
        print(i)
print("Done!")