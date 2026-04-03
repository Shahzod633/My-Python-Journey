# Квадрат числа
'''from math import sqrt, pow
a=int(input())
print('Квадрат числа', 0, "равен", 0 )
for j in range(a):
    print('Квадрат числа', j+1, "равен", int(pow(j+1,2)))'''
 
 #Звёздный треугольник 
'''a=int(input())
for j in range(a+1):
    if a>j:
        b=a-j
        print('*' * b)
'''
# Популяция 
a=int(input())
b=int(input())
c=int(input())
for j in range(c):
    print(j+1, (a * (b / 100 + 1) ** j) )
    print(j+1, (a * (b / 100 + 1) ** j) - (a * (b / 100 + 1) ** (j-1)) )




