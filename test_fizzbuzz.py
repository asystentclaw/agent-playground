import unittest

from fizzbuzz import fizzbuzz_value, generate_fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_individual_values(self):
        self.assertEqual(fizzbuzz_value(1), "1")
        self.assertEqual(fizzbuzz_value(3), "Fizz")
        self.assertEqual(fizzbuzz_value(5), "Buzz")
        self.assertEqual(fizzbuzz_value(15), "FizzBuzz")

    def test_full_sequence(self):
        result = generate_fizzbuzz()
        self.assertEqual(len(result), 100)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "Fizz")
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[14], "FizzBuzz")
        self.assertEqual(result[-1], "Buzz")


if __name__ == "__main__":
    unittest.main()
