def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
def main():
    print("Welcome to Calculator")
    print("Available operations: add, subtract, multiply, divide")
if __name__ == "__main__":
    main()