from TestsChap8 import test


def remove_letter(letter, text):
    """removes letter from text"""
    new_text = ""
    for item in text:
        if item != letter:
            new_text += item
    return new_text


test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")