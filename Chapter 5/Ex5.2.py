def number_to_day_stay(num, length):
    total = num+length
    if total % 7 == 0:
        print("Sunday")
    elif total % 7 == 1:
        print("Monday")
    elif total % 7 == 2:
        print("Tuesday")
    elif total % 7 == 3:
        print("Wednesday")
    elif total % 7 == 4:
        print("Thursday")
    elif total % 7 == 5:
        print("Friday")
    else:
        print("Saturday")


start = int(input("What is the number of your starting day? "))
stay = int(input("What is the length of your stay? "))

number_to_day_stay(start, stay)
