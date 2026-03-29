# Квадратное уравнение 
from math import pow, sqrt
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