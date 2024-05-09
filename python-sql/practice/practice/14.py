num=int(input("enter the number : "))
sum1=0
temp=num
while temp>0:
    digit=temp%10
    sum1+=digit**3
    temp//=10
if num==sum1:
    print("number is armstrong number.")
else:
    print("number is not armstrong number.")