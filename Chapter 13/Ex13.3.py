def semi_copy(oldfile, newfile):
    infile = open(oldfile, "r")
    xs = infile.readlines()
    infile.close()

    outfile = open(newfile, "w")
    for i in range(5):
        if i >= len(xs):  # Prevents an error if the text file contains less than five lines
            break
        line_num = "{0:04d}".format(i+1) + " " + xs[i]  # Numbers the first five lines
        outfile.write(line_num)
    for i in xs[5:]:
        outfile.write(i)  # Copies all the remaining lines
    outfile.close()

semi_copy("test2.txt", "test3.txt")
