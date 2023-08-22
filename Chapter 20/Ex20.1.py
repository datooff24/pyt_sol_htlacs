def string_to_dic(string):
    """converts a string into a table with letters and how frequently they occur"""
    dictionary = {}
    string = string.lower()
    string_list = "".join(string.split())
    for letter in string_list:
        dictionary[letter] = dictionary.get(letter, 0) + 1
    dic_list = list(dictionary.items())
    dic_list.sort()
    for item in dic_list:
        print(item[0], item[1])


string_to_dic("ThiS is String with Upper and lower case Letters")

# ------ Alt sol ------

def string_to_dic(strng):
    dictionary = {}
    strng = strng.lower()
    for letter in strng:
        if letter == " ":
            continue
        dictionary[letter] = dictionary.get(letter, 0) + 1
    dict_list = list(dictionary.items())
    dict_list.sort()
    for key_value in dict_list:
        print(key_value[0], key_value[1])

string_to_dic("ThiS is String with Upper and lower case Letters")
