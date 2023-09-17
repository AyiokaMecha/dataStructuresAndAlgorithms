def recursiveSearch(list,target):
    if len(list)==0:
        return False
    else:
        midpoint=len(list)//2
        if list[midpoint]==target:
            return True
        else:
            if list[midpoint]<target:
                return recursiveSearch(list[midpoint+1:],target)
            else:
                return recursiveSearch(list[:midpoint],target)

def verify(result):
    print("target found: ",result)

numbers=[x for x in range(0,100)]
result=recursiveSearch(numbers,50)
verify(result)
# this type of algorihm has an issue in that in certain languages it has a space compolexity of
# O(log n) this results in the use of extra additional space within the system
"""
this is docstring and this is how you style python code in the ide
"""