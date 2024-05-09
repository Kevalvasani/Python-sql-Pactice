num=int(input("Enter the number : "))
num1=int(input("Enter the number : "))
for i in range(num,num1+1):
    for m in range(2,i):
        if i%m==0:
           break
    else:
        print(i)




