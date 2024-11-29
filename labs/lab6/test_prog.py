import unittest
from labs.lab2.classes.calculator import Calculator, Memory
from labs.lab2.functions.ConvertNumberType import ConvertNumberType

class TestCalculatorAddition(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.Add(5, 10), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.Add(-5, -10), -15)

    def test_add_strings(self):
        with self.assertRaises(ValueError):
            self.calc.Add("test", 5)

class TestCalculatorSubtraction(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.Subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.Subtract(-10, -5), -5)

    def test_subtract_to_negative_result(self):
        self.assertEqual(self.calc.Subtract(5, 10), -5)

    def test_subtract_invalid_number(self):
        with self.assertRaises(ValueError):
            self.calc.Subtract(10, 'a')

    def test_subtract_lists(self):
        with self.assertRaises(ValueError):
            self.calc.Subtract([1, 2], 1)

class TestCalculatorMultiplication(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.Multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.Multiply(-3, -4), 12)

    def test_multiply_strings(self):
        with self.assertRaises(ValueError):
            self.calc.Multiply("test", 5)

    def test_multiply_lists(self):
        with self.assertRaises(ValueError):
            self.calc.Multiply([1, 2], 3)

class TestCalculatorDivision(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.Divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.Divide(-10, -2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.Divide(10, 0)

    def test_divide_strings(self):
        with self.assertRaises(ValueError):
            self.calc.Divide("test", 5)

class TestCalculatorMod(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_mod_positive_numbers(self):
        self.assertEqual(self.calc.Mod(10, 3), 1)

    def test_mod_negative_numbers(self):
        self.assertEqual(self.calc.Mod(-10, 3), 2)

    def test_mod_strings(self):
        with self.assertRaises(ValueError):
            self.calc.Mod("test", 5)

class TestCalculatorSquareRoot(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_square_root_positive_number(self):
        self.assertEqual(self.calc.SquareRoot(25), 5)

    def test_square_root_zero(self):
        self.assertEqual(self.calc.SquareRoot(0), 0)

    def test_square_root_negative_number(self):
        with self.assertRaises(ValueError):
            self.calc.SquareRoot(-25)

    def test_square_root_strings(self):
        with self.assertRaises(ValueError):
            self.calc.SquareRoot("test")

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_add_to_memory(self):
        self.memory.Add(5)
        self.assertEqual(self.memory.Read(), 5)

    def test_subtract_from_memory(self):
        self.memory.Add(20)
        self.assertEqual(self.memory.Subtract(5), 15)

    def test_clear_memory(self):
        self.memory.Add(10)
        self.memory.Clear()
        self.assertEqual(self.memory.Read(), 0)

    def test_memory_edge_case(self):
        self.memory.Add(1e+100)
        self.memory.Add(-1e+100)
        self.assertEqual(self.memory.Read(), 0)

class TestConvertNumberType(unittest.TestCase):

    def test_valid_float_with_dot(self):
        self.assertEqual(ConvertNumberType("3.14"), 3.14)

    def test_valid_float_with_comma(self):
        self.assertEqual(ConvertNumberType("3,14"), 3.14)

    def test_large_number(self):
        self.assertEqual(ConvertNumberType("1e+100"), 1e+100)

    def test_small_number(self):
        self.assertEqual(ConvertNumberType("1e-100"), 1e-100)

    def test_valid_integer(self):
        self.assertEqual(ConvertNumberType("42"), 42)

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            ConvertNumberType("abc")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            ConvertNumberType("")

    def test_float_to_int_conversion(self):
        self.assertEqual(ConvertNumberType("42.0"), 42)

    def test_non_integer_float(self):
        self.assertEqual(ConvertNumberType("3.14159"), 3.14159)

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            ConvertNumberType("42abc")

    def test_very_large_number(self):
        self.assertEqual(ConvertNumberType("1e+308"), 1e+308)

    def test_very_small_number(self):
        self.assertEqual(ConvertNumberType("1e-308"), 1e-308)

    def test_number_with_comma(self):
        self.assertEqual(ConvertNumberType("0,5"), 0.5)

    def test_invalid_number_with_commas(self):
        with self.assertRaises(ValueError):
            ConvertNumberType("1,000,000")


if __name__ == '__main__':
    unittest.main()

