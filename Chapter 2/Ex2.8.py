time_now = int(input("What time is it right now (in hours)? "))
time_wait = int(input("Wait how many hours? "))
time_alarm = (time_now+time_wait) % 24
print("The alarm will say " + str(time_alarm) + ":00")
