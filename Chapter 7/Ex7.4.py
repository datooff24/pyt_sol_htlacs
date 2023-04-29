def number_words_length(lists, length):
    """calculates the number of words of length in lists"""
    counter = 0
    for word in lists:
        if len(word) == length:
            counter += 1
    return counter

