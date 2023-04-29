from TestsChap12 import *
import string

def cleanword(word):
    clean = ""
    for letter in word:
        if letter not in string.punctuation:
            clean += letter
    return clean


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") == "word")

def has_dashdash(word):
    if "--" in word:
        return True

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

def extract_words(phrase):
    new_phrase = ""
    for letter in phrase:
        if letter in string.punctuation:
            new_phrase += " "
        else:
            new_phrase += letter
    low_case = new_phrase.lower()
    return low_case.split()

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

def wordcount(word, phrase):
    count = 0
    for item in phrase:
        if item == word:
            count += 1
    return count

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

def wordset(list):
    new_list = []
    for word in list:
        if word not in new_list:
            new_list.append(word)
    new_list.sort()
    return new_list


test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])


def longestword(list):
    length = 0
    for word in list:
        if len(word) > length:
            length = len(word)
    return length

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)