# Formula: A = P*(1+r/n)**(n*t)
P = 10000
n = 12
r = 0.08
t = input("What is the number of years that the money will be accounted for? ")
# t returns a string, so we turn it back into an integer
t = int(t)
A = P*(1+r/n)**(n*t)
print(A)
