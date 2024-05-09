import random
number = '0123456789'
alpha = 'abcdefghijklmnopqrstuvwxyz'
word = ''
length=10
for i in range(0,length,2):
    word += random.choice(number)
    word += random.choice(alpha)
print(word)