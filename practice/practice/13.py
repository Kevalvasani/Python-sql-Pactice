
num=int(input("Enter the number : "))
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(2,num):
    result=num1+num2
    num1=num2
    num2=result
    print(result,end=" ")