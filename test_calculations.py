# test_calculations.py

import unittest
import calculations  # This imports our calculations.py file

class TestCalculations(unittest.TestCase):
    """
    This class inherits from unittest.TestCase and contains
    our test methods.
    """

    def test_add(self):
        """Test the add function."""
        result = calculations.add(10, 5)
        self.assertEqual(result, 15, "The add function did not return 15")

        # Test with negative numbers
        self.assertEqual(calculations.add(-1, -1), -2)
        
        # Test with mixed numbers
        self.assertEqual(calculations.add(-5, 5), 0)

    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(calculations.subtract(10, 5), 5)
        self.assertEqual(calculations.subtract(-1, 1), -2)
        self.assertEqual(calculations.subtract(5, 10), -5)

    def test_divide(self):
        """Test the divide function for valid inputs."""
        self.assertEqual(calculations.divide(10, 2), 5)
        self.assertEqual(calculations.divide(-6, 3), -2)
        
        # Test floating point division
        self.assertAlmostEqual(calculations.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises a ValueError."""
        
        # We use assertRaises as a context manager to check for expected errors
        with self.assertRaises(ValueError) as context:
            calculations.divide(10, 0)
        
        # Optionally, check the error message
        self.assertEqual(str(context.exception), "Cannot divide by zero")

# This block allows the test script to be run directly
if __name__ == '__main__':
    unittest.main()