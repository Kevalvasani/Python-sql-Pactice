x=12
y=20
if x>y:
    smaller=x
else:
    smaller=y
for i in range(1,smaller+1):
    if (x%i==0) and (y%i==0):
        hcf=i
print(hcf)