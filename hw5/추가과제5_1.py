from datetime import date

born_m = int(input("You : Enter month born (1-12): "))
born_d = int(input("You : Enter day born (1-31): "))
born_y = int(input("You : Enter year born (4-digit): "))
m = int(input("Today : Enter month (1-12): "))
d = int(input("Today : Enter day (1-31): "))
y = int(input("Today : Enter year (4-digit): "))

day = (date(year=y, month=m, day=d) - date(year=born_y, month=born_m, day=born_d)).days
print("Number of days you lived: " + str(day))