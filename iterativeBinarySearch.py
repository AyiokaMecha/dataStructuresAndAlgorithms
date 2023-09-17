def iteSearch(list,target):
    first=0
    last=len(list)-1
    while(first<=last):
        midpoint=(last+first)//2
        if (list[midpoint]==target):
            return midpoint
        elif (list[midpoint]<target):
            first=midpoint+1
        else:
            last=midpoint
    return None
list=[x for x in range(0,199)]
result=iteSearch(list,150)
print("Target found at: ",result)