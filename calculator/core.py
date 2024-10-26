"""
This module contains the core arithmetic operations for the calculator.
"""

class Calculator:
    """
    A class to perform basic arithmetic operations.
    """

    def add(self, a, b):
        """
        Adds two numbers.
        
        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first number.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the subtraction.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return a * b

    def divide(self, a, b):
        """
        Divides the first number by the second number.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The quotient of the division.

        Raises:
            ValueError: If the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
