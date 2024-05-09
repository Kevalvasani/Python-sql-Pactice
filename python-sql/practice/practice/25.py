def fib(n):
    if n<=1:
        return n
    else:  
        return (fib(n-1)+fib(n-2))

m=6
for i in range(m):
    print(fib(i))



