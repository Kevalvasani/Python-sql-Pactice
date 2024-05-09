l1=[1,2,3,4,5,6,7,8,9]
l2=[10,19,18,17,16,15,4,3,6,8,9]
for i in l2:
    if i not in l1:
        l1.append(i)
print(l1)