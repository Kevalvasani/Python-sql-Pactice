string="the incessant ticking and chiming echoed off the weathered walls of the clock repair shop."
word=string.split()
vowel=["a","e","i","o","u","A","E","I","O","U"]
sum1=0
for i in word:
    count=0
    for j in range(0,len(i)):
        if i[j] in vowel:
            count+=1
    sum1+=count
print(f"there are {sum1} number of vowels in string")
