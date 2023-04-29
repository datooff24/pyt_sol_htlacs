def read_snake(file):
    newhandle = open(file, "r")
    while True:
        theline = newhandle.readline()
        if len(theline) == 0:
            break
        if "snake" in theline:
            print(theline, end = "")
