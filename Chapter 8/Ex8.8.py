from TestsChap8 import test


def mirror(text):
    new_text = text
    for i in range(1, len(text)+1):
        new_text += text[-i]
    return new_text

test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")