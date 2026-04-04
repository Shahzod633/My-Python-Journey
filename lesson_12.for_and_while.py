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
a=int(input())
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

input("Нажми Enter чтобы закрыть...") 