import string


def count_words_with_e(text):
    count = 0
    no_punct = ""
    for letter in text:
        if letter not in string.punctuation:
            no_punct += letter
    list_of_words = no_punct.split()
    for word in list_of_words:
        if "e" in word:
            count += 1
    percentage = 100*(count / len(list_of_words))
    output = 'Your text contains {0} words, of which {1} ({2:.2f}%) contain an "e".'
    print(output.format(len(list_of_words), count, percentage))


Text = """Wikipedia is an encyclopedia that anyone can edit, and tens of millions already have Wikipedia's purpose is 
to satisfy the curious minds by acting as a widely accessible and free encyclopedia that contains information on all 
branches of knowledge."""

count_words_with_e(Text)



# ------------ Alt solution -------------



import string


def count_words_with_e(text):
    # Remove punctuation
    filtered_text = ""
    for letter in text:
        if letter not in string.punctuation:
            filtered_text += letter

    # Break string into list of words
    word_list = filtered_text.split()

    # Count number of words with 'e'
    count = 0
    for word in word_list:
        if 'e' in word:
            count += 1

    # Calculate percentage
    tot_word_count = len(word_list)
    count_ratio = count / tot_word_count
    count_percentage = count_ratio*100

    # Print output
    output = 'Your text contains {0} words, of which {1} ({2:.2f}%) contain an "e".'
    print(output.format(tot_word_count, count, count_percentage))
