import unittest

from palindrome import is_palindrome


class PalindromeTests(unittest.TestCase):
    def test_ignores_case_and_spaces(self):
        self.assertTrue(is_palindrome('Never odd or even'))
        self.assertTrue(is_palindrome('A man a plan a canal Panama'))

    def test_rejects_non_palindrome(self):
        self.assertFalse(is_palindrome('hello world'))


if __name__ == '__main__':
    unittest.main()
