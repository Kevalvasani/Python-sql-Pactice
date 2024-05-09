# selection_sort

# def selection_sort(array,size):
#     for i in range(size):
#         min_ind=i
#         for j in range(i+1,size):
#             if array[j] < array[min_ind]:
#                 min_ind=j
#         (array[i],array[min_ind])=(array[min_ind],array[i])

# data=[1,4,2,7,8,6,3]
# size=len(data)
# print(data)
# print()
# print("With selection sort.")
# print()
# data1=[]
# selection_sort(data,size)
# for i in data:
#     data1.append(i)
# print(data1)


#  Bubble sort

def bubble_sort(array,size):
    for i in range(size):
        for j in range(0,size-i-1):
            if array[j] > array[j+1]:
                (array[j],array[j+1]) = (array[j+1],array[j])


data=[1,4,2,7,8,6,3]
size=len(data)
print(data)
print()
print("With Bubble sort")
print()
data1=[]
bubble_sort(data,size)
for i in data:
    data1.append(i)
print(data1)