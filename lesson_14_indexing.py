# На вход программе подаётся одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).
a=input()
total=0
for j in range(1, 20):
    if str(j) in a:
        total+=1
if total>0:
    print('Цифра')
else:
    print('Цифр нет')

# Сколько раз встречается '+' and "*"?
a=input()
total=0
count=0
for j in range(len(a)):
    if '+' in a[j]:
        total+=1
    if '*' in a[j]:
        count+=1
print(f'Символ + встречается {total} раз')
print(f'Символ * встречается {count} раз')

# Одинаковые соседи    
a=input()
total=0
for j in range(len(a)-1):
    if a[j] == a[j + 1]:
        total+=1
print(total)
    
# Гласные и согласные На вход программе подаётся одна строка с буквами русского языка. Напишите программу, которая определяет количество гласных и согласных букв и выводит текст в следующем формате:
s = input().lower() 
gl = "уеыаоэяиюёУЕЫАОЭЯИЮЁ"
total=0
sogl = "йцкнгшщзхфвпрлджчсмтбЙЦКНГШЩЗХФВПРЛДЖЧСМТБ"
count=0
for j in range(len(s)):
    if s[j] in gl:
        total+=1
    if s[j] in sogl:
        count+=1
print(f'Количество гласных букв равно {total}')
print(f'Количество согласных букв равно {count}')

# На вход программе подаётся натуральное число, записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.
a =int(input())
s=""
while a!=0:
    g = a%2
    s=s+str(g)
    a=a//2
for i in range(-1,-len(s)-1,-1):
    print(s[i], end="")

# Палиндром
a=input()
if a[:]==a[::-1]:
    print('YES')
else:
    print('NO')

# Делаем срезы 1
a=input()
print(len(a))
print(a[:]*3)
print(a[0])
print(a[:3])
print(a[-3:])
print(a[::-1])
print(a[1:-1])

# Срезы 2
a=input()
print(a[2])
print(a[-2])
print(a[:5])
print(a[0:-2])
print(a[0::2])
print(a[:])
print(a[:0:-2])  # все символы строки через один в обратном порядке, начиная с последнего.

# На вход программе подаётся строка текста. Напишите программу, которая разрежет её на две равные части, переставит их местами и выведет на экран.
s = input()
m = (len(s) + 1) // 2
print(s[m:] + s[:m])

# На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
a=input()
total=0
for j in range(len(a)):
    if a[j]==a[j].upper():
        total+=1
if total>2:
    print('YES')
else:
    print('NO')

# На вход программе подаётся строка текста. Напишите программу, которая определяет, является ли оттенок текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» (без кавычек) во всевозможных регистрах.
a=input()
a=a.upper()
if 'ХОРОШ' in a:
    print('YES')
else:
    print('NO')

# На вход программе подаётся строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
a = input()
total = len(a)
for j in range(len(a)):
    if a[j] == a[j].upper():
        total -= 1

print(total)

# Количество слов
a = input()
print(a.count(' ') + 1)

# Минутка генетики
a=input()
a=a.lower()
print('Аденин: ' + str(a.count('а')))
print('Гуанин: ' + str(a.count('г')))
print('Цитозин: ' + str(a.count('ц')))
print('Тимин: ' + str(a.count('т')))

# Очень странные дела
n = int(input())  # Считываем количество строк
count_odi = 0     # Счетчик сообщений от Оди

for _ in range(n):
    message = input()
    if message.count('11') >= 3:
        count_odi += 1
print(count_odi)

# Количество цифр  в слове 
a = input()
a=a.lower()
total = 0
for j in range(len(a)):
    if a[j] in '0123456789':
        total += 1

print(total)

# На вход программе подаётся строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
a=input()
if a.endswith('.com') == True:
    print('YES')
elif a.endswith('.ru') == True:
    print('YES')
else:
    print('NO')

# Самый частотный символ
s=input()
maxi=0
ma=0
count=0
for i in s:
    if s.count(i) >=maxi:
        maxi=s.count(i)
        ma=i
print(ma)

















    
    
    





