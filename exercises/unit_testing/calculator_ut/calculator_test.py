import unittest
from calculator import Calculator


def setUpModule():
    print('set up module')


def tearDownModule():
    print('tear down module')


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        # Create an instance of the calculator that can be used in all tests
        self.calc = Calculator()

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)
        self.assertNotEqual(self.calc.subtract(2, 3), 6)


    # Write test methods for subtract, multiply, and divide
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertNotEqual(self.calc.subtract(10, 3), 8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertNotEqual(self.calc.multiply(2, 2), 5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertNotEqual(self.calc.divide(9, 3), 2)


if __name__ == '__main__':
    unittest.main()
