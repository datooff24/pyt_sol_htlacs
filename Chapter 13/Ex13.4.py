def semi_copy_reverse(oldfile, newfile):
    infile = open(oldfile, "r")
    xs = infile.readlines()
    infile.close()

    outfile = open(newfile, "w")

    # Take each line, split each word into a list, join back together without first number
    for line in xs:  
        line_list = line.split(" ")  # Specify separator so \n is not removed in the splitting process

        # Remove number in listing
        if line_list[0].isdigit():
            del line_list[0]

        # Add numberless lines back together
        complete_line = " ".join(line_list)
        outfile.write(complete_line)
    outfile.close()

semi_copy_reverse("test2.txt", "test3.txt")
