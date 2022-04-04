#Q1
class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        #add both inputs
        return self.input1 + self.input2

    def subtractor(self):
        #subtract both user inputs
        return self.input1 - self.input2

    def multiplier(self):
        #multiply both user inputs
        return self.input1 * self.input2

    def divider(self):
        #divide both user inputs
        return self.input1 / self.input2

    def clear(self):
        #reset to 0
        self.input1 = 0
        self.input2 = 0
        return self.input1, self.input2

if __name__ == "__main__":
    x = int(input('Please enter number 1: '))  # take in user input and convert it to int
    y = int(input('Please enter number 2: '))  # take in user input and convert it to int

c = Calculator(x, y)
print("Adder method result: " + str(c.adder()))
print("Subtractor method result: " + str(c.subtractor()))
print("Multiplier method result: " + str(c.multiplier()))
print("Divider method result: " + str(c.divider()))
print("Clear method result: " + str(c.clear()))