from TestsChap8 import test


def reverse(text):
    """reverses each letter in text"""
    new_text = ""
    for i in range(1, len(text)+1):
        new_text = new_text+text[-i]
    return new_text

test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")


