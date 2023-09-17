#my attempt at recursion
# def factorial(number):
#     if number==0 or number==1:
#         return 1
#     else:
#         return number *(factorial(number-1))

# number=10
# print(factorial(number))

"""
onto the quicksort algorithm and how I am going to implement it in python
notes
-it uses the divide and conquer methodology in python to do its work
-recursively calls the itself as will be shown
-remember the base case that is meant to stop us from triggering the maximum recursion depth
"""


def quickSort(values):
    if len(values)<=1:
        return values
    less_than_pivot=[]
    greater_than_pivot=[]
    pivot=values[0]
    for value in values[1:]:
        if value<=pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quickSort(less_than_pivot) +[pivot]+quickSort(greater_than_pivot)

import random
random.seed(1)
list=[random.randint(0,1000) for _ in range(1000)]

sorted=quickSort(list)
print(sorted)