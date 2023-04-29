from TestsChap8 import test


def remove_all(substring, string):
    """removes all instances of substring from string"""
    # use the split method on substring and then glue all the elements in the resulting list together
    if substring in string:
        string_list = string.split(substring)
        new_string = ""
        for letter in string_list:
            new_string += letter
        return new_string
    else:
        return string

test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")