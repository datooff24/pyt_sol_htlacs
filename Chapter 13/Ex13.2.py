def read_snake(file):
    newhandle = open(file, "r")
    while True:
        theline = newhandle.readline()
        if len(theline) == 0:
            break
        if "snake" in theline:
            print(theline, end = "")
    newhandle.close()

# ---- Alt solution ----

def read_snake(file):
    handle = open(file, "r")
    line = "line"
    while len(line) != 0:
        line = handle.readline()
        if "snake" in line:
            print(line, end="")
    handle.close()
