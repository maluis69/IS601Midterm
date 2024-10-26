from calculator.plugin_loader import load_plugins

def repl():
    calc = Calculator()
    plugins = load_plugins()
    while True:
        command = input("Enter command (add, sub, mul, div, plugins) or 'quit' to exit: ").strip().lower()
        if command == 'quit':
            break

        if command == 'plugins':
            print("Available plugins:", list(plugins.keys()))
            continue

        if command in plugins:
            try:
                a = float(input("Enter a number: "))
                result = plugins[command].execute(a)
                print(f"Result: {result}")
            except Exception as ex:
                print(f"Error: {ex}")
            continue

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
