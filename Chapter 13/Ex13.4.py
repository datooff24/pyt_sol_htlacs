def semi_copy_reverse(oldfile, newfile):
    infile = open(oldfile, "r")
    xs = infile.readlines()
    infile.close()

    outfile = open(newfile, "w")
    for line in xs:  # Take each line, split each word into a list, join back together without first number
        line_list = line.split(" ")  # Specify separator so \n is not removed in the splitting process
        if line_list[0].isdigit():
            line_list[0] = ""  # Remove number in listing
        complete_line = " ".join(line_list)
        outfile.write(complete_line)
    outfile.close()

semi_copy_reverse("test2.txt", "test3.txt")