def mergeSort(numbers):
    if len(numbers)<=1:
        return numbers
    mid=len(numbers)//2
    left_half=numbers[:mid]
    right_half=numbers[mid+1:]
    left=mergeSort(left_half)
    right=mergeSort(right_half)
    return merge(left,right)

def merge(left,right):
    i=0
    temp=[]
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    while i<len(left):
        temp.append(left[i])
        i+=1
    while j<len(right):
        temp.append(right[j])
        j+=1
    return temp


import random
random.seed(1)
numbers=[random.randint(0,1000) for _ in range(150)]

sortedNumbers=mergeSort(numbers)
print(sortedNumbers)