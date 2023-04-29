# Ex 20.3

# Idea: use code from chapter 14 to create an alphabetical list of all the words in Alice in Wonderland.
# Create a dictionary that goes through this list with key:value pair word:frequency.
# Use the key "Alice" to find out how often this word appears in the dictionary


# Code chapter 14:
def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


# ---------------------------------------------------------------------------------------------------------------------

def list_to_dic(lst):
    """converts a list into a dictionary with key:value pair word:frequency"""
    dic = {}
    for word in lst:
        # Get the value of dic[word]. If there is none, set it to zero.
        # Add +1 for each time word is encountered
        dic[word] = dic.get(word, 0) + 1
    return dic


alice_words_list = get_words_in_book("AliceInWonderland.txt")
alice_words_list.sort()
alice_dic = list_to_dic(alice_words_list)
print("The word {0} appears {1} times".format("alice", alice_dic["alice"]))


def print_dictionary(dic, file):
    """"creates a text file that logs the keys and values of dic"""
    myfile = open(file, "w")
    myfile.write("{0:<17} {1}\n".format("Word", "Count"))
    myfile.write("=======================\n")
    for (word, frequency) in dic.items():
        myfile.write("{0:<17} {1}\n".format(word, frequency))
    myfile.close()


print_dictionary(alice_dic, "alice_words.txt")


# Ex 20.4

def longest_word_dic(dic):
    """returns the largest item in a dictionary"""
    length = 0
    # First find the largest item (value)
    for word in dic.keys():
        if dic[word] > length:
            length = dic[word]
    # Next find the key the value belongs to
    for word in dic.keys():
        if dic[word] == length:
            return "The longest word is '{0}', and it appears {1} times".format(word, length)


print(longest_word_dic(alice_dic))
