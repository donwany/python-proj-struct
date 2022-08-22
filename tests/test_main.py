from decoratorDemo import divide
import unittest

class TestDivide(unittest.TestCase):
    def test_divide(self):
        div = divide(20, 2)
        self.assertEqual(div, 10, "Success")

    def test_params_with_wrong_type(self):
        with self.assertRaises(TypeError):
            div = divide("20", "2")

    def test_with_zero_or_negative(self):
        with self.assertRaises(ZeroDivisionError):
            div = divide(20, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
