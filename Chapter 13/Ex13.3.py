def semi_copy(oldfile, newfile):
    infile = open(oldfile, "r")
    xs = infile.readlines()
    infile.close()
    
    # we cannot have more than 9999 lines
    if len(xs) > 9999:
        return print("File is too large")

    # numbers each line and place them in a newfile
    outfile = open(newfile, "w")
    for i in range(len(xs)):
        numbered_line = "{0:04d}".format(i+1) + " " + xs[i] 
        outfile.write(numbered_line)
    outfile.close()
