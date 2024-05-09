import random
number = random.randint(0,9)
G_input=int(input("Enter the number which can be generated : "))
if number==G_input:
    print("Your Guess is rigth number")
    print(f"You Guess the number is {G_input} and generated number is {number}")
else:
    print("Your Guess is wrong number")
    print(f"You Guess the number is {G_input} and generated number is {number}")