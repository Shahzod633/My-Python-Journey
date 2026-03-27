#Самописный калькулятор!!!
# the first project in python!!!
a=int(input())
b=int(input())
c=input()
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif b==0 and c=="/":
    print(" На ноль делить нельзя!")
elif c!="+" and c!="-" and c!="*" and c!="/":
    print("Неверная операция")
elif c=="/":
    print(a/b) 