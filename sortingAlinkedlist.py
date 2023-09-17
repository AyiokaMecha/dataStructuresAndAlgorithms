def split(list):
    mid=list.size()//2
    current=list.head
    position=0
    right=LinkedList()
    left=LinkedList()
    while(position<=mid):
        current=current.next_node
        position+=1
    left=list
    right.head=current.next_node
    current.next_node=None
    return left,right


def merge(left,right):
    sortedlink=LinkedList()
    sortedLink.head=0
    currentLeft=left.head
    currentRight=right.head
    currentSorted=sortedLink.head
    while (currentLeft and currentRight):
        if currentLeft.data<currentRight.data:
            currentSorted.next_node=currentLeft
            currentLeft=currentLeft.next_node
            currentSorted=currentSorted.next_node
        else:
            currentSorted.next_node=currentRight
            currentRight=currentRight.next_node
            currentSorted=currentSorted.next_node
    while currentLeft:
        currentSorted.next_node=currentLeft
        currentLeft=currentLeft.next_node
        currentSorted=currentSorted.next_node
    while currentRight:
        currentSorted.next_node=currentRight
        currentRight=currentRight.next_node
        currentSorted=currentSorted.next_node
    sortedlink.head=sortedlink.head.next_node
    return sortedlink



def sortingLinkedLists(list):
    left=LinkedList()
    right=LinkedList()
    left,right=split(list)
    sortingLinkedLists(left)
    sortingLinkedLists(right)
    return merge(left,right)
