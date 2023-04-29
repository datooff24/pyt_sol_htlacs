# Writing type() will tell us what class a value falls into
type(3)
type("Hello")
type(3.2)

# = is the assignment operator, == is the equality operator
# Some words, like lambda, if, else, for, etc. cannot be used as variable names. These are Python's keywords
# and have their own meaning

# len() returns the number of characters in a string
len("Hello world")

# The operator / will divide and return a float number. The operator // will divide and return the number rounded down
x = 10/3
y = 10//3

print(x)
print(y)

# int float and str are type converter functions:
# int changes any number to an integer, rounding it down no matter the value.
int(3.999)
# float changes any string back to a number (if the string itself is a number), turning it into a floating number
float("3")
# str turns its argument into a string
str(19)

# Most operators do not work on strings. Some exceptions are + and *.
# + will concatenate two strings
message = "message"
name = " name"
print(message + name)
# * will repeat the string
print(message*3)

