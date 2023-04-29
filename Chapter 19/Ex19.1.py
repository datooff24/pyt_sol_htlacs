def get_age():
    try:
        integer = input("Please enter a positive integer: ")
        # if the input is not a decimal number or negative
        if integer != str(int(integer)) or int(integer) <= 0:
            raise ValueError
    except ValueError:
        print("Enter a positive integer, nothing else")
        # recurse until a valid input has been given
        get_age()
    else:
        print("Good job")

get_age()
