# 12.1.a
import calendar
cal = calendar.TextCalendar()
cal.pryear(2012)

# 12.1.b
# firstweekday is set to zero i.e. monday by default.
cal = calendar.TextCalendar(firstweekday=3)
cal.pryear(2012)

# 12.1.c
# 0 corresponds to january, 1 to february etc.
cal.prmonth(2023, 4)

# 12.1.d
d = calendar.LocaleTextCalendar(6, "norwegian")  # Norwegian works, Korean does not work
d.pryear(2012)

# 12.1.e
# Takes a year as argument, returns TRUE if the year is a leap year, FALSE otherwise
print(calendar.isleap(2000))
