

# a = input()
# b = input()


class SuperCalculator:
    def __init__(self, value1, prefix1, value2, prefix2):
        self.value1 = value1
        self.prefix1 = prefix1
        self.value2 = value2
        self.prefix2 = prefix2

    def sum(self):
        return self.value1+self.value2

    def sub(self):
        return self.value1-self.value2

    def mul(self):
        return self.value1*self.value2

    def div(self):
        return self.value1/self.value2


num = SuperCalculator(456, 10, 2, 10)

print(SuperCalculator.sum(num))
print(SuperCalculator.sub(num))
print(SuperCalculator.mul(num))
print(SuperCalculator.div(num))
