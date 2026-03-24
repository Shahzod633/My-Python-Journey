# Первая цифра после точки 
a=float(input())
b=int((a*10)%10)
print(b) 

# Дробная часть цыфры
'''a=float(input())
b=((a*10)%10)/10 
print(b)'''

# Наибольшее и наименьшее
''' a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
mi=min(a,b,c,d,e)
ma=max(a,b,c,d,e)
print('Наименьшее число', '=', mi)
print('Наибольшее число =', ma) '''

# Абсолютная сумма 5 чисел Напишите программу, которая вычисляет сумму их модулей
''' a=abs((float(input())))
b=abs((float(input())))
c=abs((float(input())))
d=abs((float(input())))
e=abs((float(input())))
print(abs(a+b+c+d+e))  '''

# Интересное число
''' a=int(float(input()))
a3 =a%10
a2 = a%100//10
a1 = a//100
mi=min(a3,a2,a1)
ma=max(a3,a2,a1)
if (ma-mi)==(a3+a2+a1-mi-ma):
    print('Число интересное')
else:
    print('Число неинтересное')'''




