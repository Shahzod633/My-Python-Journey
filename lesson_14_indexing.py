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

# На вход программе подаётся строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс. Если она встречается два и более раза, выведите индексы её первого и последнего вхождения на одной строке, разделённые символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO» (без кавычек).
s=input()
if s.count('f')==1:
    print(s.find('f'))
if s.count('f')>=2:
    print(s.find('f'), s.rfind('f'))
if s.count('f')==0:
    print('NO')

# На вход программе подаётся строка текста, в которой буква «h» встречается минимум два раза. Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними
s = input()
first=s.find('h')
last=s.rfind('h')
b=s[:first] + s[last + 1:]
print(b)

# Плохие комментарии коменты состояшие из пробелов или пустые пробелы 
n=int(input())
total=0
for j in range(n):
    a=input()
    total+=1
    b=a.isspace()
    if b==True or a=='':
        print(str(total)+':', 'COMMENT SHOULD BE DELETED')
    else:
        print(str(total)+':', a)

# Проверь никнейм условие начинается с @ и 5<=len(a)<=15 и все букви нижнего регистра 
a=input()
body=a[1:]
if (a.startswith('@')==True) and 5<=len(a)<=15 and (body.isalnum()==True) and (body == body.lower()) :
    print('Correct')
else:
    print('Incorrect')

# Автомобильный номер Напишите программу, которая принимает на вход строку и проверяет, является ли эта строка корректным автомобильным номером.
s = input().strip()

allowed = "АВЕКМНОРСТУХ"  

if len(s) in [9, 10]:
    p1 = s[0]
    p2 = s[1:4]
    p3 = s[4:6]
    p4 = s[6]
    p5 = s[7:]

    if (p1 in allowed and
        p2.isdigit() and
        p3[0] in allowed and p3[1] in allowed and
        p4 == '_' and
        p5.isdigit()):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

# Используя метод format(), дополните приведённый ниже код так, чтобы он вывел текст: In 2010, someone paid 10k Bitcoin for two pizzas.
s = 'In {0}, someone paid {1} {2} for two pizzas.'
year=2010
cash='10k'
money='Bitcoin'
print(f'In {year}, someone paid {cash} {money} for two pizzas.')

# другой способ предидушей задачи 
s = 'In {}, someone paid {} {} for two pizzas.'
year=2010
cash='10K'
money='Bitcoin'
print(s.format(year, cash, money))

# На вход программе подаются два целых числа a и b. Ваша программа должна посчитать для этих чисел сумму их кубов и куб их суммы и вывести результат вычислений
a=int(input())
b=int(input())
print(f'Для чисел {a} и {b}:',
         f'Сумма кубов: {a}**3 + {b}**3 = {(a**3)+(b**3)}',
         f'Куб суммы: ({a} + {b})**3 = {(a+b)**3}', sep='\n  ') 

# (Не) Активное похудение
a, b=int(input()), float(input())
c = 100 - a * 0.2
if b <= c:
    print("Все идет по плану")
    print(f"#{a} ДЕНЬ: ТЕКУЩИЙ ВЕС = {b} кг, ЦЕЛЬ по ВЕСУ = {c} кг")
else:
    print('Что-то пошло не так')
    print(f"#{a} ДЕНЬ: ТЕКУЩИЙ ВЕС = {b} кг, ЦЕЛЬ по ВЕСУ = {c} кг")


# Какая следующая буква?
a=input()
b=ord(a)
total=0
total+=b
c=chr(total+1)
if c=='а':
    print('Дальше букв нет')
else:
    print(chr(total+1))
    
# Символы в диапазоне 
a=int(input())
b=int(input())
M=max(a,b)
m=min(a,b)
for j in range(m, M+1):
    print(chr(j), end=" ")

# Простой шифр
a=input()
for j in a:
    print(ord(j), end=" ")

# Самое тяжёлое слово  
a=input()
b=input()
c=input()
d=input()
s1=0
s2=0
s3=0
s4=0
for j in a:
    s1+=ord(j)
for i in b:
    s2+=ord(i)
for f in c:
    s3+=ord(f)
for n in d:
    s4+=ord(n)
maxi=max(s1, s2, s3, s4)
if maxi==s1:
    print(a)
elif maxi == s2:
    print(b)
elif maxi == s3:
    print(c)
else:
    print(d)

# Стоимость ответа
a=input()
summ=0
for j in a:
    summ+=ord(j)
print(f"Текст сообщения: '{a}'", f'Стоимость сообщения: {summ*3}🐝', sep='\n')
























    
    
    





