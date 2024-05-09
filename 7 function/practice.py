# 1
# def kilometertomiles(kilometer):
#     return kilometer*0.6214
# def main():
#     kilometers=float(input("Enter your number : "))
#     print()
#     return kilometers, "kilometers = ", format(kilometertomiles(kilometers),".2f"), "miles"
# main()

# 2 
# def num(n):
#     if n in range(44,50):
#         print("%s is in the range"%str(n))
#     else:
#         print("%s is not in the range"%str(n))
# num(48)

# 3
# def sum(number):
#     total = 0
#     for m in number:
#         total+=m
#     return total
# sum([8, 2, 3, 0, 7])

# 4 
# def mul(number):
#     total= 1
#     for m in number:
#         total*=m
#     return total
# mul([8, 2, 3, -1, 7])

def bold(fn):
    def wrapped():
        return "<b>"+ fn()+ "</b>"
    return wrapped
def italic(fn):
    def wrapped():
        return "<i>"+ fn()+ "</i>"
    return wrapped
def underline(fn):
    def wrapped():
        return "<u>"+ fn()+ "</u>"
    return wrapped

@bold
@italic
@underline
def main():
      return "My name is keval"
main()

# def prime(num):
#     if num==1:
#         return "number is prime"
#     elif num == 2:
#         return "number is prime"
#     else:
#         for i in range(2,num):
#             if num%i!=0:
#                 return "number is prime" 
#             return "number is not a prime"
# prime(1)

# def main(string):
#     upper = 0
#     lower = 0
#     for i in string:
#         if i.isupper():
#             upper+=1
#         elif i.islower():
#             lower+=1
#         else:
#             pass
#     print(string)
#     print("uppercase in are",upper)
#     print("lowercase in are",lower)

# main("The quick Brow Fox")

    
# def main(num):
#     l=[]
#     for i in num:
#         if i not in l:
#             l.append(i)
#     return l 
# main([1,2,3,3,3,3,4,5])

# def main(num):
#     l=[]
#     for i in num:
#         if i%2==0:
#             l.append(i)
#     return l 
# main([1, 2, 3, 4, 5, 6, 7, 8, 9])

# def perfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum+=i
#     return sum == num
# perfect(6)

# def palim(s):
#     p = s[::-1]
#     if p==s:
#         return "palimdrome"
#     else:
#         return "not palimdrome"
# palim("mihim")


# def local():
#     var="keval"
#     num=3
#     return num
# local()



# LAMBDA-------------------------------------------------------------------------------------------------
# string="keval vasani"
# str1=lambda upper : upper.upper()
# print(str1(string))



# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
# Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)
 
# Get the second largest element
# secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
# res = secondLargest(List, sortList)
 
# print(res)