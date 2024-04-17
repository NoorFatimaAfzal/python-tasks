class calculator():
    def __init__(self):
        self.x=0
        self.y=0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        self.result = x / y
        return self.result
    
calc=calculator()
print(calc.add(5, 10))
print(calc.subtract(5, 10))
print(calc.multiply(5, 10))
print(calc.divide(5, 10))