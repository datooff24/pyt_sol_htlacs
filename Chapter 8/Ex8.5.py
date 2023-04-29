import string


def remove_punct(text):
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
branches of knowledge. Hosted by the Wikimedia Foundation, Wikipedia consists of freely editable content, 
whose articles also have numerous links to guide readers for more information. Written collaboratively by largely 
anonymous volunteers, anyone with Internet access and in good standing can write and make changes to Wikipedia 
articles (except in limited cases where editing is restricted to prevent disruption or vandalism). Since its creation 
on January 15, 2001, Wikipedia has grown into the world's largest reference website, attracting over a billion 
visitors monthly. It currently has more than sixty million articles in more than 300 languages, including 6,609,
556 articles in English with 127,941 active contributors in the past month. """

remove_punct(Text)
