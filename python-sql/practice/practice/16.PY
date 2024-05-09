# print("1. Addition \n2. Substraction \n3. Multiplication \n4. Division")
# num=int(input("enter the number : "))
# if num==1:
#     num1=int(input("enter the number : "))
#     num2=int(input("enter the number : "))
#     print(num1+num2)
# elif num==2:
#     num1=int(input("enter the number : "))
#     num2=int(input("enter the number : "))
#     print(num1-num2)
# elif num==3:
#     num1=int(input("enter the number : "))
#     num2=int(input("enter the number : "))
#     print(num1*num2)
# elif num==4:
#     num1=int(input("enter the number : "))
#     num2=int(input("enter the number : "))
#     print(num1/num2)
# else:
#     print("enter the valid option")



def cal(num):
    if num==1:
        a=int(input("enter the first number : "))
        b=int(input("enter the second number : "))
        print(a+b)
    elif num==2:
        a=int(input("enter the first number : "))
        b=int(input("enter the second number : "))
        print(a-b)
    elif num==3:
        a=int(input("enter the first number : "))
        b=int(input("enter the second number : "))
        print(a*b)
    elif num==4:
        a=int(input("enter the first number : "))
        b=int(input("enter the second number : "))
        print(a/b)
    else:
        print("enter the valid option")

print("1. Addition \n2. Substraction \n3. Multiplication \n4. Division")
num=int(input("enter the number : "))
cal(num)