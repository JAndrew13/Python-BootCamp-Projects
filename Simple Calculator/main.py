# JB's Calculator Program

# calculation brains
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Calculator splash screen
def start():
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("Welcome to JB's Simple Calculator!")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    menu()

# open menu to choose operand
def menu():
    print("\nWhat would you like to compute?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Please Enter 1, 2, 3, or 4 :")

    select = input(">")

    if select in ('1', '2', '3', '4'):
        if select == '1':
            print("Addition!")
            calc(select)
        elif select == '2':
            print("Subtraction!")
            calc(select)
        elif select == '3':
            print("Multiplication!")
            calc(select)
        elif select == '4':
            print("Division!")
            calc(select)
    else:
        print("Selection Invalid, Restarting..")

    menu()

# takes chosen operand, collects values, and returns result
def calc(select):
    Number_1 = int(input("Enter your First Number : "))
    Number_2 = int(input("Enter your Second Number : "))

    if select == '1':
        print(Number_1, "+", Number_2, "=", add(Number_1, Number_2))

    elif select == '2':
        print(Number_1, "-", Number_2, "=", subtract(Number_1, Number_2))

    elif select == '3':
        print(Number_1, "*", Number_2, "=", multiply(Number_1, Number_2))

    elif select == '4':
        print(Number_1, "/", Number_2, "=", divide(Number_1, Number_2))

    else:
        print("Error, try again!")
        start()


# Start the app
start()




