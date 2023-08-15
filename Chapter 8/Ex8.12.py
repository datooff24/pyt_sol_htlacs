from TestsChap8 import test


def remove(substring, string):
    """removes first instance of substring from string"""
    # find the position of the substring, then glue the ends of the letters before and after the substring together
    position = string.find(substring)
    if substring in string:
        pre_string = string[0:position]
        post_string = string[position+len(substring):]
        new_string = pre_string + post_string
        return new_string
    else:
        return string


test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")


# -------- Alt solution ---------

def remove(piece, word):
    location = word.find(piece)
    if location == -1:
        return word
    else:
        new_word = word[:location] + word[location+len(piece):]
        return new_word
