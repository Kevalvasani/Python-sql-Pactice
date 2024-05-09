def string1(n):
    string2=n[::-1]
    if string2==n:
        print("Given string is palindrome.")
    else:
        print("Given string is not palindrome.")
string=input("enter the string : ")
string1(string)
