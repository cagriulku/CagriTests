# tests/test_string_operations.py
import unittest
from src.string_operations import reverse_string, capitalize_string, is_palindrome


class TestStringOperations(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))


if __name__ == '__main__':
    unittest.main()
