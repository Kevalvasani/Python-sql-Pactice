def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)
   
num=int(input("enter the number : "))

if num<=0:
    print("please enter number greater than zero")
else:
    print("factorial of given number is ",fact(num))