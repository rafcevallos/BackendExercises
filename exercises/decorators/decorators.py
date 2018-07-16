def interior_decorator(func):
    def add_curtains(): # function reference?
        func()
        print("now my house has purple curtains")

        return add_curtains # returns the instructions for add_curtains

def move_in():
    print("My house was emtpy, but...")

# bind returned function from interior_decorator to new variable
new_house = (interior_decorator(move_in)) #new_house now equals the value of add_curtains which is a reference to interior decorator
new_house()


def add(num1, num2)
    return num1 + num2

def subtract(num1, num2)
    return num1 - num2

def calculator(func):
    return func(3, 4)

result = calculator(add)
print(result)