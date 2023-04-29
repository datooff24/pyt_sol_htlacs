def reverse_file(original, reverse):
    old = open(original, "r")
    xs = old.readlines()
    old.close()

    xs.reverse()

    new = open(reverse, "w")
    for word in xs:
        new.write(word)
    new.close()
