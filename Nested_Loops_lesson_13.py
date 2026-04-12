# This program uses nested loops to print all the possible combinations of hours, minutes, and seconds in a day.
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)