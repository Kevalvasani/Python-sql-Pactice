# import platform

# help("platform")
# h=platform.python_version()
# print(h)
# x=platform.architecture()
# print(x)
# x=platform.system()



# import module

# a=module.person()
# print(a)
# print(x)
# name=module.MyNumber()
# print(name.name())



# import math

# print(math.log2(23))
# v=math.hypot(5,10)
# print(math.floor(v))
# c=math.pow(5,3)
# print(pow(3,2))



# import time
# print("hello")
# time.sleep(3)
# print("keval")
# time.sleep(3)
# print(c)


# from datetime import datetime

# strdate="16-Oct-20" 
# v=datetime.datetime.strftime(strdate,"%d-%b-%y")
# print(v)
# v=datetime.datetime(2022,11,10,8,52,52)
# print(v)
# datetimeobj=datetime.datetime(*dt_tuple)
# datetimeobj 
# datetime_obj= datetime.now()
# date=datetime_obj.date()
# time=datetime_obj.time()
# print(datetime_obj)
# print(date)
# print(time)



# import sys

# print(sys.path)



# import numpy as np
 
# Initial Array
# arr = np.array([[-1, 2, 0, 4, 5],
#                 [4, -0.5, 6, 0, 5],
#                 [2.6, 0, 7, 8, 5],
#                 [3, -7, 4, 2.0, 5],
#                 [3, 4, 5, 6, 7]])
# arr1=arr.sum(axis=0)
# print(arr1)
# arr2=arr.sum(axis=1)
# print(arr2)

# ar = np.array([[3,5,7],
#                [4,6,8],
#                [7,6,3]])

# ar2 = np.array([[4,6,8],
#          [7,6,3],
#          [3,5,7]])
# ar3 = ar2[0:2]

# print(ar3)
# print("First array\n",ar)
# print("Second array\n",ar2)   
# print("Multiplication of ar,ar2 : \n",ar*ar2)
# print("Addition of ar,ar2 : \n",ar+ar2)
# print("Substraction of ar,ar2 : \n",ar-ar2)
# print("Division of ar,ar2 : \n",ar/ar2)

# print("\nFirst array\n",ar)
# print("\nSecond array\n",ar2)
# print("\nMultiplication of ar with 2 : \n",ar*2)
# print("\nAddition of ar,ar2 with 1 : \n",ar+1)
# print("\nSubstraction of ar with 1 : \n",ar-1)
# print("\nDivision of ar with 2 : \n",ar/2)

# print("\nlargest element in ar : \n", ar.max())
# print("\nlargest element in rowwise ar : \n", ar.max(axis=1))


# ar1=np.array([[12,23],[93,64]])
# ar2=np.array([[88,55],[77,44]])
# ar3=np.concatenate((ar1,ar2))
# ar3=np.concatenate((ar1,ar2),axis=1)
# print(ar1)
# print(ar2)
# print(ar3)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#     print("\n",x,"\n")
#     for y in x:
#        print(y)
#        for z in y:
#           print(z)

# import pandas as pd
# pd.options.display.max_rows = 9999      
# df=pd.read_csv("data.csv")
# pf=df.head(29)
# print(pf)



# import arrow,datetime

# arrow_obj=arrow.Arrow(2021,2,21)
# arrow_obj=arrow.now()
# arrow_obj=arrow.get('October 30 2021 11:23','MMMM DD YYYY HH:mm')
# datetime = arrow.get('March 30 2021 12:05', 'MMMM DD YYYY HH:mm')
# datetime = datetime.datetime(2021, 1, 1, 0, 0)
# arrow_object = arrow.Arrow.fromdatetime(datetime)
# print(arrow_object)
# print(arrow_obj)

# arrow_1 = arrow.Arrow(2021, 1, 1, 0, 0, tzinfo='US/Pacific')
# print(arrow_1)




