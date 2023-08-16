def semi_copy(oldfile, newfile):
    # Idea: put each file line into a list, create a new string that is line number + file line
    infile = open(oldfile, "r")
    xs = infile.readlines()
    infile.close()

    outfile = open(newfile, "w")
    for i in range(len(xs)):
        numbered_line = "{0:04d}".format(i+1) + " " + xs[i]  # Numbers the first five lines before the text
        outfile.write(numbered_line)
    outfile.close()
