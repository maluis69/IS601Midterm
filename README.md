Advanced Python Calculator

Overview
-This project is an advanced Python-based calculator application developed as part of a Software Engineering Graduate Course midterm. The calculator supports basic arithmetic operations, a flexible plugin system, calculation history management using Pandas, and a command-line interface (REPL) for real-time user interaction. It integrates professional software development practices, including design patterns, comprehensive logging, and dynamic configuration through environment variables.

Features
-Basic Arithmetic Operations: Add, Subtract, Multiply, and Divide.
-Command-Line Interface (REPL): A user-friendly interface for executing commands.
-Plugin System: Dynamically load and execute additional commands without modifying the core application.
-History Management with Pandas: Record, view, and manage calculation history.
-Professional Logging: Record key operations and errors with configurable log levels.
-Design Patterns: Implemented using Facade, Command, and other key design patterns.
-Testing and CI: Comprehensive tests with Pytest and CI integration using GitHub Actions.

Getting Started:
Prerequisites

-Python 3.x
-Git
-A virtual environment setup (recommended)

Setup Instructions
1. Clone the Repository:
git clone https://github.com/maluis69/IS601Midterm
cd midterm

2. Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:

pip install -r requirements.txt

4. Run the Calculator:

python main.py

Usage Instructions

Basic Commands:
-add: Add two numbers.
-sub: Subtract two numbers.
-mul: Multiply two numbers.
-div: Divide two numbers.
-Plugins: Type plugins to see the list of available plugins. Execute any plugin by typing its name.
-History: Type history to view the saved calculation history.
-Quit: Type quit to exit the calculator.

Example Usage:

Enter command (add, sub, mul, div, plugins, history) or 'quit' to exit: add
Enter first number: 5
Enter second number: 3
Result: 8.0

Enter command (add, sub, mul, div, plugins, history) or 'quit' to exit: history
             timestamp operation  operand1  operand2  result
0  2024-10-25 12:34:56      add        5.0       3.0     8.0

Plugin System
This calculator application includes a flexible plugin system that allows dynamically loading new features without modifying the core code. To add a new plugin, create a new file in the plugins/ directory and implement the PluginInterface.

Adding a New Plugin

1. Create a new plugin file, e.g., plugins/cube_plugin.py:

from plugins.plugin_interface import PluginInterface

class CubePlugin(PluginInterface):
    def execute(self, a):
        return a ** 3

2. Run the calculator and type plugins to see your new plugin listed.

Logging Configuration
This application uses a configurable logging system that records key operations, errors, and informational messages. The logging level can be set through an environment variable:

Set Log Level (example for Linux/macOS):

export LOG_LEVEL=INFO

Design Patterns

The project applies the following design patterns to achieve modularity, maintainability, and scalability:

-Facade Pattern: Simplifies interactions with the calculation history managed by Pandas.
-Command Pattern: Encapsulates commands within the REPL for structured handling of user actions.
-Factory Method & Singleton Patterns: Used to manage the plugin system and ensure efficient resource management.

Testing and Continuous Integration
-Unit Testing: Comprehensive tests are implemented using Pytest. Achieved a minimum of 90% test coverage.
-Code Quality: Code quality is ensured using Pylint.
-Continuous Integration: GitHub Actions is used to automate testing and code quality checks.

To run tests locally:

pytest --cov=calculator


Acknowledgements
This project was developed for the Software Engineering Graduate Course at NJIT. Special thanks to the instructor for providing detailed guidelines and support.
