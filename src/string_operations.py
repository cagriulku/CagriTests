# src/string_operations.py
def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def is_palindrome(s):
    return s == s[::-1]
