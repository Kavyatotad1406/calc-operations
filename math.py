# calculator.py
# Program to perform addition and subtraction of two numbers

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Main program
if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
