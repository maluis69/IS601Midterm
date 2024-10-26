from calculator.core import Calculator

def repl():
    calc = Calculator()
    while True:
        command = input("Enter command (add, sub, mul, div) or 'quit' to exit: ").strip().lower()
        if command == 'quit':
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if command == 'add':
                print(f"Result: {calc.add(a, b)}")
            elif command == 'sub':
                print(f"Result: {calc.subtract(a, b)}")
            elif command == 'mul':
                print(f"Result: {calc.multiply(a, b)}")
            elif command == 'div':
                print(f"Result: {calc.divide(a, b)}")
            else:
                print("Unknown command")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")
