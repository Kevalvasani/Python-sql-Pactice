l = ["Spade","Heart","Diamond","Club"]
print(l)
r=input("Enter which element you have to delete : ")
c=r.capitalize()
if c in l:  
    l.remove(c)
    print(l)
else: 
    print(f"{r} is not there in list please write correct element.")
