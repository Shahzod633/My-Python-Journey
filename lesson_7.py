# Тема string  и  методы строк
'''s='"Python is a great language!"'
b=', said Fred.'
d='"I '
h="don't"
c=' ever remember having this much fun before."'
print(str (s)+str (b)+str (d)+str (h)+str (c))'''

# What's Your Name? тема string  и  методы строк
'''a=str(input())
b=str(input())
print('Hello', a, b + "! You have just delved into Python")'''

#Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит информацию о ней
'''team=str(input())
team_length=len(team)
print("Футбольная Команда", team, "имеет длину", team_length, "символов.")'''

#Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
city1=str(input())
city2=str(input())
city3=str(input())
city1_length=int(len(city1))
city2_length=int(len(city2))
city3_length=int(len(city3))
city_w_mini_l=min(city1_length, city2_length, city3_length)
city_w_maxi_l=max(city1_length, city2_length, city3_length)
if city1_length==min(city1_length, city2_length, city3_length) and city2_length==max(city1_length, city2_length, city3_length):
    print(city1)
    print(city2)
elif city1_length==min(city1_length, city2_length, city3_length) and city3_length==max(city1_length, city2_length, city3_length):
    print(city1)
    print(city3)
elif city2_length==min(city1_length, city2_length, city3_length) and city1_length==max(city1_length, city2_length, city3_length):
    print(city2)
    print(city1)
elif city2_length==min(city1_length, city2_length, city3_length) and city3_length==max(city1_length, city2_length, city3_length):
    print(city2)
    print(city3)
elif city3_length==min(city1_length, city2_length, city3_length) and city1_length==max(city1_length, city2_length, city3_length):
    print(city3)
    print(city1)
elif city3_length==min(city1_length, city2_length, city3_length) and city2_length==max(city1_length, city2_length, city3_length):
    print(city3)
    print(city2)
