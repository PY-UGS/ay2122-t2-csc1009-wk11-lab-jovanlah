#Q1
class Calculator:
    def __init__(self):
        self.input1 = input1
        self.input2 = input2

    def adder(self,input1,input2):
        #add both inputs
        return input1 + input2

    def subtractor(self,input1,input2):
        #subtract both user inputs
        return input1 - input2

    def multiplier(self,input1,input2):
        #multiply both user inputs
        return input1 * input2

    def divider(self,input1,input2):
        #divide both user inputs
        return input1 / input2

    def clear(self):
        #reset to 0
        self.input1 = 0
        self.input2 = 0
        return self.input1, self.input2

input1 = int(input('Please enter number 1: '))
input2 = int(input('Please enter number 2: '))

c = Calculator()

print("Adder method result: " + str(c.adder(input1, input2)))
print("Subtractor method result: " + str(c.subtractor(input1, input2)))
print("Multiplier method result: " + str(c.multiplier(input1, input2)))
print("Divider method result: " + str(c.divider(input1, input2)))
print("Clear method result: " + str(c.clear()))