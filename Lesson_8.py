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














