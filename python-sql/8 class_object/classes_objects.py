#     # class Myclass:
#     #     name="Keval"
#     #     surname="vasani"
#     # c1=Myclass()
#     # print(c1.name,c1.surname)

# class Myclass:
#     school="sibmt"
#     def __init__(self):
#         self.name=input("Enter your name : ")
#         self.age=int(input("Enter your age : "))
    
#     def name_age(self):
#         print(self.name,self.age)    

#     def update(self):
#         self.name=input("Enter your name : ")
#         self.age=int(input("Enter your age : "))

#     def gschool():
#         school=school
        
# c1=Myclass()
# # print(Myclass.gschool())
# c1.age=int(input("Enter your age : "))
# c1.name_age()


# Inheritance

# class Father:
#     def __init__(self):
#         self.name="Deepak"
#     def father():
#         print("i'm your father")
# class Son(Father):
#     def __init__(self):
#         super().__init__()
#         self.sname="vasani"
#     def son():
#         print("I'm your son")
# f=Son()
# print(f.name,f.sname)



# multiple inheritance 

# class Fun:
#     def name(self,fname):
#         self.fname=fname
# class Sun:
#     def name(self,mname):
#         self.mname=mname
#         print(self.mname)
# class Jun(Fun,Sun):
#     def name(self,sname):
#         # super().name()
#         self.sname=sname
#         print(self.sname)
# v=Jun()
# v.name("vasani")

# multilevel inheritance 

# class Fun:
#     def vname(self,fname):
#         self.fname=fname
#         print(self.fname)
# class Sun(Fun):
#     def dname(self,mname):
#         self.mname=mname
#         print(self.mname)
# class Jun(Sun):
#     def name(self,sname):
#         # super().name()
#         self.sname=sname
#         print(self.sname)
# v=Sun()
# v.vname("vasani")

# Hierarchical inheritance

# class Fun:
#     def vname(self,fname):
#         self.fname=fname
#         print(self.fname)
# class Sun(Fun):
#     def dname(self,mname):
#         self.mname=mname
#         print(self.mname)
# class Jun(Sun):
#     def name(self,sname):
#         # super().vname()
#         self.sname=sname
#         print(self.sname)

# v=Fun()
# v.vname("vasani")

# polymorphism

# class Name:
#     def Show(self,firstname=""):
#         print("welcome ",firstname)
#     def Show(self,firstname="",lastname=""):
#         print("welcome ",firstname,lastname)

# obj=Name()
# obj.Show('keval')
# obj.Show("Keval",15)




# Enqcapsulation

# class Enq:
#     def name(self):
#         print("keval")
#     def _mname(self):
#         print("Deepak")
#     def __sname(self):
#         print("vasani")
# class Access(Enq):
#     def fname(self):
#         print("keval")
# obj=Access()
# obj._mname()


# Method overriding
# class Brand_model:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print(self.brand,self.model)

# class Car(Brand_model):
#     pass

# class Bike(Brand_model):
#     def move(self):
#         print(f"this bike is of {self.brand} company and model name is {self.model}")


# class Scooty(Brand_model):
#     def move(self):
#         print(f"this scooty is of {self.brand} company and model name is {self.model}")

# car1=Car("Lamborghini","Lamborghini Urus")
# bike1=Bike("Kawasaki","Kawasaki Ninja H2")
# scooty1=Scooty("Honda","Honda Deo")
# for i in (car1,bike1,scooty1):
#     i.move()


# import random

# def generate_otp():
#     otp = str(random.randint(1000, 9999))  # Generate a 4-digit OTP
#     return otp
# def match_otp(user_input, generated_otp):
#     return user_input == generated_otp
# # Generate an OTP
# otp = generate_otp()
# print(f"Generated OTP: {otp}")

# # Simulate user input
# user_input = input("Enter the OTP: ")

# # Match the user input with the generated OTP
# if match_otp(user_input, otp):
#     print("OTP is valid.")
# else:
#     print("OTP is not valid.")


# import random
# otp=random.randint(1000,9999)
# print(f"otp is here : {otp}")
# eotp=int(input("Enter your otp : "))
# if otp == eotp:
#     print("otp is valid")
# else:
#     print("otp is not valid")


# class Calculator:
#     def __init__(self):
#         self.num1=int(input("Enter the number : "))
#         self.num2=int(input("Enter the number : "))
#     def add(self):
#         return self.num1+self.num2
#     def sub(self):
#         return self.num1-self.num2
#     def mul(self):
#         return self.num1*self.num2
#     def div(self):
#         return self.num1/self.num2

# cal=Calculator()
# num1=int(input("Enter the number : "))
# num2=int(input("Enter the number : "))
# print("\n 1. Addition \n 2. SUBTRACTION \n 3. MULTIPLICATION \n 4. DIVISION")
# choice=int(input("Enter the choice : "))
# if choice==1:
#     print(cal.add())
# elif choice==2:
#     print(cal.sub())
# elif choice==3:
#     print(cal.mul())
# elif choice==4:
#     print(cal.div())
# else:
#     print("Enter from given choice")
    


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
