from TestsChap11 import test

def replace(s, old, new):
    string_list = s.split(old)
    new_string = new.join(string_list)
    return new_string

replace("Mississippi", "i", "I")

test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")