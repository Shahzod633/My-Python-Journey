# Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу R
from math import sqrt, ceil, pi 
R=float(input())
S=pi*pow(R, 2)
C=2*pi*R
print(S)
print(C)

#  На вход поступает число сумируйте пол и потолок для этого числа  
'''from math import ceil,  floor
a=float(input())
ca=ceil(a)
fa=floor(a)
print(ca+fa)
'''
# Евклидово расстояние 
'''from math import sqrt, pow
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
p=sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))
print(p)
'''
# Тригонометрическое выражение
'''from math import pow, pi, sin, cos, tan, radians
x=radians(float(input()))
M=sin(x)+cos(x)+pow(tan(x), 2)
print(M)
'''

# Правильный многоугольник
'''from math import pow, pi, tan
n=int(input())
a=float(input())
S=((n*pow(a, 2))/(4*tan(pi/n)))
print(S)
'''

# Средние значения -- среднее арифметическое, среднее геометрическое, среднее гармоническое, среднее квадратичное чисел
'''from math import sqrt, pow
a=float(input())
b=float(input())
print((a+b)/2) #среднее арифметическое
print(sqrt(a*b)) #среднее геометрическое
print((2*a*b)/(a+b)) #среднее гармоническое
print(sqrt((pow(a,2)+pow(b,2))/2)) #среднее квадратичное
'''

# Квадратное уравнение 
'''from math import pow, sqrt
a=float(input())
b=float(input())
c=float(input())
# ax**2+bx+c=0
D=pow(b,2)-(4*a*c)
if D<0:
    print('Нет корней')
elif D==0:
    x=-(b/(2*a))
    print(x)
elif D>0:
    x1=(-b-sqrt(D))/(2*a)
    x2=(-b+sqrt(D))/(2*a)
    print(min(x1, x2))
    print(max(x1, x2))
    '''




















