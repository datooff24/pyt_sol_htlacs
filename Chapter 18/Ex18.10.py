import os


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix=""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "/"

    dirlist = get_dirlist(path)
    output_list = []
    for f in dirlist:
        fullname = os.path.join(path, f)  # Turn name into full pathname
        if os.path.isdir(fullname):  # If a directory, recurse.
            print_files(fullname, prefix)
        else:
            output = path + prefix + f
            output_list.append(output)
    return output_list


print(print_files("C:/Users/David/Desktop"))
