from TestsChap8 import test


def reverse(text):
    """reverses each letter in text"""
    new_text = ""
    for i in range(1, len(text)+1):
        new_text = new_text+text[-i]
    return new_text


def is_palindrome(word):
    if word == reverse(word):
        return True
    return False


test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))