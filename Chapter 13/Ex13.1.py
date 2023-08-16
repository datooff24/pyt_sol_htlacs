def reverse_files(original, reversed="reversed"):
    """copies the content of the file original and pastes them in a new file reversed"""
    # separate each line of original one list and reverse them
    old_file = open(original, "r")
    line_list = old_file.readlines()
    line_list.reverse()
    old_file.close()

    # open a new file, and put each line of the reverse list in there
    new_file = open(reversed, "w")
    for line in line_list:
        new_file.write(line)
    new_file.close()
