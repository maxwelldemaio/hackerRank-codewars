with open("days/brian8.txt", "r") as AoC:
    file = AoC.read()

data = file.split('\n')
acc = 0
instr_list = []

for instruction in data:
    operation, value = instruction.split(" ")
    instr_list.append((operation, value))
spot = 0
stop = False
ilist = []
switched_list = []
switched = False
count = 0
while not stop:
    for i in range(spot, len(instr_list)):
        op = instr_list[i][0]
        val = instr_list[i][1]
        if op == "nop":
            if i not in switched_list and switched is False:
                count += 1
                print(i, acc, op, val, count)
                switched = True
                ilist.append(i)
                switched_list.append(i)
                spot = i + int(val)
                break
            else:
                count += 1
        elif op == "acc":
            count += 1
            acc += int(val)
        elif op == "jmp":
            if i not in switched_list and switched is False:
                count += 1
                switched = True
                switched_list.append(i)
            else:
                count += 1
                ilist.append(i)
                spot = i + int(val)
                break
        if i in ilist:
            count += 1
            print("Cleared", i, spot, op, val, switched_list, count)
            print(ilist)
            spot = 0
            count = 0
            ilist.clear()
            acc = 0
            switched = False
            break
        if i == len(instr_list) - 1:
            stop = True
            break

        ilist.append(i)
print("acc: ", acc)