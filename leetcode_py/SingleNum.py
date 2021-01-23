class Testing():
    def mihoy(self, listyboi):
        a = 0
        for i in listyboi:
            a ^= i
        return a

example = Testing()

print(example.mihoy([1,1,2]))