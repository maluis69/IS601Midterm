"""
This module implements the Read-Eval-Print Loop (REPL) interface for user interaction.
"""

from calculator.core import Calculator
from calculator.plugin_loader import load_plugins
from calculator.history_facade import HistoryFacade

def repl():
    calc = Calculator()
    plugins = load_plugins()
    history = HistoryFacade()
    
    while True:
        command = input("Enter command (add, sub, mul, div, plugins, history) or 'quit' to exit: ").strip().lower()
        print(f"Received command: {command}")  # Debugging line
        
        if command == 'quit':
            print("Exiting REPL...")  # Debugging line
            break

        if command == 'plugins':
            print("Available plugins:", list(plugins.keys()))
            continue

        if command == 'history':
            print(history.get_history())
            continue

        if command in plugins:
            try:
                plugin = plugins[command]
                params = plugin.execute.__code__.co_argcount - 1
                
                if params == 1:
                    a = float(input("Enter a number: "))
                    result = plugin.execute(a)
                elif params == 2:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    result = plugin.execute(a, b)
                else:
                    print("Unknown command")
                    continue

                print(f"Result: {result}")
                continue
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as ex:
                print(f"Unexpected error: {ex}")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = None

            if command == 'add':
                result = calc.add(a, b)
            elif command == 'sub':
                result = calc.subtract(a, b)
            elif command == 'mul':
                result = calc.multiply(a, b)
            elif command == 'div':
                result = calc.divide(a, b)

            if result is not None:
                print(f"Result: {result}")
                history.add_operation(command, a, b, result)
            else:
                print("Unknown command")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")        
               