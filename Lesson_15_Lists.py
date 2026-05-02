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
    
#  Каждый второй предмет  На вход программе подаётся строка из эмодзи-символов. Создайте список, содержащий все символы данной строки, не включая каждый второй, и выведите этот список.
a = input()
# Проходим по индексам от 0 до len(a) с шагом 2
# Это автоматически выкинет каждый второй предмет (индексы 1, 3, 5...)
Alist = [a[j] for j in range(0, len(a), 2)]

print(Alist)

# Дополните приведённый ниже код так, чтобы он вывел среднее арифметическое элементов списка evens
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average =sum(evens)/len(evens)

print(average)

# елемент списка имеющий значение Green заменился на значение Зеленый, а элемент Violet – на Фиолетовый. Далее необходимо вывести полученный список.
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3]='Зеленый'
rainbow[-1]='Фиолетовый'

print(rainbow)

# "перевёрнутый" список languages (то есть элементы будут идти в обратном порядке).
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])

# Используя операторы конкатенации (+) и умножения списка на число (*), дополните приведённый ниже код так, чтобы он вывел следующий список:  [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print((numbers1*2)+(numbers2*9)+(numbers3))

# Напишите программу, выводящую следующий список: ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
numbers = [] # Создаем пустой список

for i in range(1, 27):
    # ord('a') возвращает 97. Прибавляя (i-1), мы идем по алфавиту.
    char = chr(ord('a') + i - 1) 
    numbers.append(char * i)

print(numbers)

#На вход программе подаются натуральное число n а затем n строк. Напишите программу, которая создаёт из указанных строк список, а затем выводит его.
n=int(input())
List=[]
for j in range(1, n+1):
    a=input()
    List.append(a)
print(List)

# На вход программе подаются натуральное число n а затем n целых чисел. Напишите программу, которая создаёт из указанных чисел список их кубов, а затем выводит его.
from math import pow
n=int(input())
List=[]
for j in range(1, n+1):
    a=int(input())
    a=int(pow(a, 3))
    List.append(a)
print(List)

# Дано список нужно Вывел длину списка;  Вывел последний элемент списка; Вывел список в обратном порядке (вспоминаем срезы); Вывел «YES» (без кавычек), если список содержит числа 5 и 17  или «NO» (без кавычек) в противном случае; Вывел список с удалёнными первым и последним элементами.
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
print(numbers[1:-1])

# На вход программе подаётся натуральное число n  Напишите программу, которая создаёт список, состоящий из делителей введённого числа в порядке возрастания, а затем выводит этот список.
n =int(input())
List=[]
for j in range(1, n+1):
    if n%j==0:
        List.append(j)
print(List)

# На вход программе подаётся натуральное число n(n>=2) Затем поступают n целых чисел. Напишите программу, которая создаёт из указанных чисел список, состоящий из сумм соседних чисел.
n=int(input())
sp1=[]
sp2=[]
for j in range(1, n+1):
    a=int(input())
    sp1.append(a)
for i in range(len(sp1)-1):
    sp2.append(sp1[i] + sp1[i+1])
print(sp2) 

# Удалите нечётные индексы
n=int(input())
List=[]
sp1=[]
for j in range(1, n+1):
    a=int(input())
    List.append(a)
for i in range(len(List)):
    if i%2==0:
        sp1.append(List[i])
print(sp1)

# На вход программе подаются натуральное число n и n строк а азтем число k апишите программу, которая выводит K -ую букву из введённых строк на одной строке без пробелов.\
n=int(input())
List=[]
Sp=[]
for j in range(1, n+1):
    a=input()
    List.append(a)
b=int(input())
for i in List:
    if len(i)>=b:
        print(i[b - 1], end="") 

# Символы всех строк
n=int(input())
sp1=[]
for j in range(1, n+1):
    a=input()
    sp1.extend(a)
print(sp1)

# Дополните приведённый ниже код так, чтобы он вывел сумму квадратов элементов списка numbers. numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
num=[]
for j in numbers:
    b=pow(j, 2)
    num.append(b)
print(sum(num))

# Negatives, Zeros and Positives
n=int(input())
ot=[]
z=[]
po=[]
for j in range(n):
    num=int(input())
    if num<0:
        ot.append(num)
    elif num==0:
        z.append(num)
    else:
        po.append(num)
print(*ot, sep='\n')
print(*z, sep='\n')
print(*po, sep='\n')

#  Remove outliers
n = int(input())
nums = [int(input()) for _ in range(n)]
mx = max(nums)
mn = min(nums)
# Печатаем только те числа, которые не равны максимуму и минимуму
for x in nums:
    if x != mx and x != mn:
        print(x)

# Google search - 1
n = int(input())
strings = []

# Шаг 1: Собираем "базу" строк
for _ in range(n):
    strings.append(input())

# Шаг 2: Получаем поисковый запрос
query = input()

# Шаг 3: Ищем запрос в каждой строке
for s in strings:
    # Приводим обе части к нижнему регистру для поиска
    if query.lower() in s.lower():
        print(s)

# На вход программе подаётся строка текста. Напишите программу, которая выводит слова введённой строки в столбик.
a=input()
b=a.split()
print('\n'.join(b))
