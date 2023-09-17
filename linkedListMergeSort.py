from linkedList import LinkedList
#merge-sort, split and merge function

def merge_sort(linkedlist):
    """sorts a linked list
    first recursively divide the list into sublist with one node
    repeatedly merge the sublinked list"""

    #base case for stopping the recursion
    if linkedlist.size()==1:
        return linkedlist
    elif linkedlist.head is None:
        return linkedlist
    
    left_half,right_half=split(linkedlist)
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    return merge(left,right)

def split(linkedlist):
    """divide the unsorted list at midpoint into 2 sublist"""
    if(linkedlist.head is None or linkedlist.head is None):
        left_half=linkedlist
        right_half=None
        return left_half,right_half
    else:
        size=linkedlist.size()
        mid=size//2
        midnode=linkedlist.nodeAtIndex(mid-1)

        left_half=linkedlist
        right_half=LinkedList()
        right_half.head=midnode.next_node
        midnode.next_node=None
        return left_half,right_half


def merge(left,right):
    """
    merges 2 linked list sorting data in the nodes
    returns a new linked list
    """
    #create a new linked list that ought to contain the merged
    merged=LinkedList()

    merged.add(0)
    current=merged.head

    #obtain head of left and right
    left_head=left.head
    right_head=right.head

    #iterating over the left and right until the tail node is reached
    while left_head or right_head: #it is important to set the conditions to an or operation
        #if head node of left is none we are past the tail and add the node in right to the list
        if left_head is None:
            current.next_node=right_head
            #call next on right so that the loop condition can be terminated by setting the right_head to NOne
            right_head=right_head.next_node
        elif right_head is None:
            current.next_node=left_head
            #calling next on left to set the loop conditions to false
            left_head=left_head.next_node
        else:
            #not at either tail node 
            #obtain the node data to perform comparison operations
            left_data=left_head.data
            right_data=right_head.data

            #performing the comparison operations
            if left_data<right_data:
                current.next_node=left_head
                left_head=left_head.next_node
            else:
                current.next_node=right_head
                right_head=right_head.next_node
        #move current to the next node
            current=current.next_node
    #Discarding the fake head and setting the merged head as the head
    head=merged.head.next_node
    merged.head=head
    return merged



import random
random.seed(1)
list=[random.randint(1,100)for _ in range(100)]
 
l=LinkedList()
# for i in range(len(list)):
#     l.add(list[i])
lists=map((lambda x: x*2),list)


sorted=merge_sort(l)
print(list)
