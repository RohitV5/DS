"""
String operations and utilities.
Description: Strings are immutable sequences of characters.
Real-life analogy: Like a sentence written on paper; you can't change a letter without rewriting.
"""
class StringOps:
    @staticmethod
    def reverse(s):
        return s[::-1]
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]
# Example usage:
# print(StringOps.reverse("hello"))
# print(StringOps.is_palindrome("racecar")) 