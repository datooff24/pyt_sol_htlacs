import random


my_tickets = [ [ 7, 17, 37, 19, 23, 43],
[ 7, 2, 13, 41, 31, 43],
[ 2, 5, 7, 11, 13, 17],
[13, 17, 37, 19, 23, 43] ]

# 14.5.a

def lotto_draw():
    """draw 6 random balls labeled 1 to 49"""
    rng = random.Random()
    ball = 0
    ball_list = []
    while ball < 6:  # draw 6
        new_ball = rng.randrange(1, 50)
        if new_ball not in ball_list:  # lotto balls don't contain duplicates
            ball_list.append(new_ball)
            ball += 1  # only consider a ball drawn if it is not a duplicate
    return ball_list

# 14.5.b
def lotto_match(draw, ticket):
    correct = 0  # number of correct guesses
    for number in ticket:
        if number in draw:
            correct +=1
    return correct

# 14.5.c
def lotto_matches(draw, tickets):
    correct_list = []
    for ticket in tickets:
        correct_list.append(lotto_match(ticket, draw))
    return correct_list

# 14.5.d
# is_prime from Ex7.10
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def primes_in(ticket):
    count = 0
    for num in ticket:
        if is_prime(num):
            count+= 1
    return count

# 14.5.e

# idea: create a separate function that makes a list of prime numbers with lower bound 2, upper bound the largest
# number in each ticket. Then check whether the prime number list contains values not in ticket.

def prime_num_list(upper_bound):
    num_list = list(range(2,upper_bound+1))  # go through all numbers from 2 up to and including upper bound
    prime_list = []
    for num in num_list:  # filter out the non-prime numbers in num_list
        if is_prime(num):
            prime_list.append(num)
    return prime_list

def prime_misses(tickets):
    # merge all the numbers in tickets into one single list
    merge_list = []
    for item in tickets:
        merge_list += item
    # filter out all the duplicates
    merge_list_filter = []
    for item in merge_list:
        if item not in merge_list_filter:
            merge_list_filter.append(item)
    # generate a prime_num_list with upper_bound 49 since the balls are numbered 1 to 49
    prime_list = prime_num_list(49)
    # compare prime_list to merge_list_filter
    missed_primes = []
    for item in prime_list:
        if item not in merge_list_filter:
            missed_primes.append(item)
    return missed_primes

#14.5.f
def compare_ticket_draw(tickets, amount):
    """counts how long it takes to get amount of correct numbers in any ticket of tickets"""
    counter = 1  # start at 1 because if you draw successfully the first time, it only took one draw
    while True:
        # draw a random draw through lotto_draw(), keep on doing this until AMOUNT correct
        draw = lotto_draw()
        # compare the draw to the tickets using lotto_matches()
        correct_list = lotto_matches(draw, tickets)
        if amount in correct_list:
            return counter
        else:
            counter += 1


# now we run the experiment amount times:
def experiment_correct_num(amount, correct_numbers):
    """runs compare_ticket_draw amount times to check for correct_numbers and averages all the outputs"""
    counter = 0
    for i in range(amount):
        num = compare_ticket_draw(my_tickets, correct_numbers)
        print("it took {0} tries to get {1} correct numbers in a ticket".format(num, correct_numbers))
        counter += num
    average = counter / amount
    return average

print("On average you need {0} tries to get {1} correct numbers in a ticket.".format(experiment_correct_num(20, 5), 5))