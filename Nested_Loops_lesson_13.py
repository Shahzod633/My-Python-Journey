# This program uses nested loops to print all the possible combinations of hours, minutes, and seconds in a day.
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

 # Таблица-1
a=int(input())
for i in range(a):
    for j in range(3):
        print(a, end=' ')
    print()

# Таблица-2 
a=int(input())
total=0
for i in range(1,a+1):
  for j in range(1, 6):
    print(i, end=" ") 
  print()

# Таблица-3
a=int(input())
for i in range(1, a+1):
  for j in range(1, 10):
    print(i, '+', j, '=', i+j)
  print()

# Численный треугольник 
a=int(input())
for i in range(1):
  for j in range(1, a+1):
    print(str(j)*j)
  print()
