num=int(input("Enter the number : "))
if num>=0:
    sum=0
    for i in range(0,num):
        sum+=i
        print(sum)
else:
    print("It is not a natural number.")