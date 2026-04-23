# На вход программе подаётся одно число n Напишите программу, которая выводит список 
a=int(input())
print(list(range(1, a+1)))

# Список букв
n = int(input())
Alist = [chr(i) for i in range(97, 97 + n)]
print(Alist)

#Список нечётных чисел
a=int(input())
Alist=[j for j in range(1, a+1) if j%2!=0]
print(Alist)
    


