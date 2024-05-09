def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
m=int(input("Enter the number : "))
if m<0:
    print("Enter the natural number")
else:
    print("sum of given natural number is ",sum(m))