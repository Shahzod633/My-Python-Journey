# Популяция 
'''a=int(input())
b=int(input())
c=int(input())
for j in range(c):
    print(j+1, (a * (b / 100 + 1) ** j) )'''

# продолжение изучение команд for 
'''for j in range(1, 10):
    print(j)'''

# таблица умножение 
'''a=int(input())
for j in range(1, 11):
    print(a, 'x', j, '=', a*j )
'''

# Последовательность чисел 2 
'''a=int(input())
b=int(input())
for j in range(a, b+1):
    if j%10==9:
        print(j)
    elif  j%15==0:
        print(j)
    elif j%17==0:
        print(j)'''

# последовательность чисел 3
'''a=int(input())
b=int(input())
for j in range(a, b+1):
    if a<b:
        print(j)
    else:
        break
if a>b:
    for j in range(a, b-1, -1):
            print(j)
elif a==b:
    print(a)

input("Нажми Enter чтобы закрыть...") '''

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''a=int(input())
a3=a%10 # последняя цифра
a2=(a%100)//10 # вторая цифра
a1=(a//100) # первая цифра
print('Сумма цифр:', a1 + a2 + a3)
print('Произведение цифр:', a1 * a2 * a3)'''

# Сумма чисел
'''n=int(input())
total=0
for _ in range(n):
    num=int(input())
    total=total+num
print(total)'''
    
# Асимптотическое приближение
from math import log 
counter = 0
n = int(input())
for i in range(1, n+1):
    counter = counter + 1/i
print(counter - log(n))

# На вход программе подаётся натуральное число n Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), , квадрат которых оканчивается на 2 на  5  или на 8.
from math import pow
n=int(input())
counter=0
for j in range(1, n+1):
    if pow(j,2)%10==2 or pow(j,2)%10==5 or pow(j,2)%10==8:
        counter+=j
print(counter)

# Факториал
n=int(input())
counter=1
for j in range(1, n+1):
    counter = counter*j
print(counter)

#Без нулей 0️
total=1
for _ in range(1, 11):
    num=int(input())
    if num>0 or num<0:
        total*=num
print(total)

# Сумма делителей
n=int(input())
total=0
for j in range(1,n+1):
    if n%j==0:
        total+=j
    
print(total)

#  Напишите программу, которая считывает последовательность из 10 целых чисел и определяет, является ли каждое из них чётным или нет.
total=0
for _ in range(10):
    num=int(input())
    if num%2==0:
        total+=1
        if total==10:
            print("YES")
    elif num%2!=0:
        print("NO")
        break 

# Знакочередующаяся сумма
n=int(input())
total=0
Total=0
for j in range(1, n+1):
    if j%2==0:
        total+=j
    else:
        Total+=j
print(Total-total)

# Наибольшое число 2 
n=int(input())
max1=0
max2=0
for j in range(n):
    num=int(input())
    if num>max1:
        max2=max1
        max1=num
    elif num>max2:
        max2=num
print(max1)
print(max2)

# Число Фибоначчи
n=int(input())
x=1
y=0
for j in range(1, n+1):
    print(x,end=' ')
    x,y=x+y,x 

# До КОНЦА 1
text=input()
while text!="КОНЕЦ":
    print(text)
    text=input()

# На вход программе подаётся последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трёх слов: «стоп», «хватит», «достаточно» (без кавычек). Сами эти слова в последовательность не входят, лишь символизируя её окончание. Напишите программу, которая выводит общее количество членов данной последовательности.
text=input()
total=0
while text!='стоп' and text!='хватит' and text!='достаточно':
    total+=1
    text=input()
print(total)

#На вход программе подаётся последовательность целых чисел, каждое число на отдельной строке. Признаком окончания последовательности является любое отрицательное число, при этом в саму последовательность оно не входит. Напишите программу, которая выводит сумму всех членов данной последовательности.
a=int(input())
total=0
while a>=0: 
    total+=a
    a=int(input())
print(total)