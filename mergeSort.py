def split_iteratively(list):
    mid=len(list)//2
    left=[]
    right=[]
    for i,x in enumerate(list):
        if i<mid:
            left.append(x)
        else:
            right.append(x)
    return left,right
def merge_sort(list):
    """
    Divide and conquer algorithmic approach in solving problems
    Steps:
    Divide step: breakdown the list into halfes until the sublists have 1 element
    Conqure: recursively sort the sublist created in the previous steps
    Combine: Merge the sorted sublists create in previous steps
    its time complexity is O(n log n)
    """
    #base case or stopping case
    if len(list)<=1:
        return list
    
    left_list,right_list=split_iteratively(list)
    left=merge_sort(left_list)
    right=merge_sort(right_list)

    return merge(left,right)


def split(list):
    """Divide the unsorted list into two lists left and right 
    utilizes the floor division operation to find the midpoint
    and then uses the slicing operation in python to return the 
    appropriate values in the system
    operates in logatithmic time O(log n)
    but slicing operation in python runs in K logn
    """
    midpoint=len(list)//2
    left=list[:midpoint]
    right=list[midpoint:]
    return left,right

def merge(left,right):
    """
    merges two lists and sorts them in the process and 
    returns a new list
    operates in linear time O(n)
    """
    list=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            list.append(left[i])
            i+=1
        else:
            list.append(right[j])
            j+=1
    while j<len(right):
        list.append(right[j])
        j+=1
    while i<len(left):
        list.append(left[i])
        i+=1
    return list

def verify(list):
    n=len(list)
    if n==0 or n==1:
        return True
    return list[0]<= list[1] and  verify(list[1:])
import random
n=100
min=1
max=100
list=[random.randint(min,max)for _ in range(n)]
slist=merge_sort(list)
print(verify(list))
print(verify(slist))


