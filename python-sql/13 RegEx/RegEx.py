import re
txt='''The 89 oldest classical British and Latin writing had little or no space between words and could be written in boustrophedon (alternating directions). Over time, text direction (left to right) became standardized. Word dividers and terminal punctuation became common. The first way to divide sentences into groups was the original paragraphos, similar to an underscore at the beginning of the new group.The graphos evolved into the pilcrow which in English manuscripts in the Middle Ages can be seen inserted inline between sentences.'''
# x=re.findall("^The",txt)
# c=re.findall("ences.",txt)
j=re.findall("\d",txt)
print(j)

# txt = "8 times before + - 11:45 AM.()"

#Check if the string has any + characters:

# x = re.findall("[+]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# print("\r")
# import re
# def is_allowed_specific_char(string):
#     charRe = re.compile(r'[^a-zA-Z0-9]')
#     string = charRe.findall(string)
#     return string

# print(is_allowed_specific_char("ABCDEFabcdef123450")) 
# print(is_allowed_specific_char("*&%@#!}{"))