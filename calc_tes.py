import unittest
from calc import add, subtract, multiply, divide
class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        # Test cases for addition
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(3.5, 2.5), 6)

    def test_subtract(self):
        # Test cases for subtraction
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(3.5, 2.5), 1)

    def test_multiply(self):
        # Test cases for multiplication
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 2), 5)

    def test_divide(self):
        # Test cases for division
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(10, 2.5), 4)
        self.assertEqual(divide(0, 5), 0)
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=4)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
if __name__=='__main__':
    unittest.main()




