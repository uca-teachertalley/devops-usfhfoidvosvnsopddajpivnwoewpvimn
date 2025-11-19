"""Author: Joshua Sano"""
# calculations.py
# Author: Nate Hazeslip
"""A module for basic arithmetic calculations. An example of unit testing and automated testing"""

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def divide(a, b):
    """
    Returns the division of a by b.
    Raises a ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def main():
    """Main function to demonstrate the calculations module."""
    print("Addition of 10 and 5:", add(10, 5))
    print("Subtraction of 10 and 5:", subtract(10, 5))
    try:
        print("Division of 10 by 0:", divide(10, 0))
    except ValueError as e:
        print("Error:", e)

# This block allows the script to be run directly
if __name__ == '__main__':
    main()