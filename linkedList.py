from merginglinkedlists import mergeLinkedLists
class Node:
    """
    an object for storing a single node of a linked list
    Models two attributes- data and a link to the next nod elin the list
    """
    data=None
    next_node=None
    def __init__(self,data):
        self.data=data
    def __repr__(self) -> str:
        return "<Node data: %s>"%self.data
    
class LinkedList:
    head=None
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head==None
    def size(self):
        """
        returns the number of nodes within the list and it runs in linear time 
        O(n) linear time complexity in the system
        """
        current=self.head
        count=0
        while current:
            count +=1
            current=current.next_node
        return count
    def add(self,data):
        """
        Adding a new node to the head of the list
        this is done in constant time O(1)
        First off we take the value of the data hold it in a node, set the next_node property of the data to point
        to the head of the given list, the set the head of the list to be equal to the new node
        """
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return current
            else:
                current=current.next_node
        return None
    def insert(self,data,index):
        """
        the insertion algorithm, it occurs in constant time O(1)
        but reaching the node occurs in linear time
        """
        if index==0:
            self.add(data)
        if index>0:
            new=Node(data)
            position=index
            current=self.head
            while position>1:
                current=current.next_node
                position-=1
            # prev_node=current
            # next_node=current.next_node
            # prev_node.next_node=new
            # new.next_node=next_node
            current.next_node,new.next_node=new,current.next_node
    def myRemove(self,index):
        
        if index==0:
            self.head=self.head.next_node
        else:
            position=index
            current=self.head
            while position>1:
                current=current.next_node
                position-=1
            remove=current.next_node
            current.next_node=remove.next_node
        return None
    def remove(self,key):
        """
        remove the node containing data that matches the key
        returns the node or none if the key doesn't exist
        linear time complexity O(n)
        """
        current=self.head
        previous=None
        found=False

        while current and not found:
            if current.data==key and current is self.head:
                found=True
                self.head=current.next_node
            elif current.data==key:
                found=True
                previous.next_node=current.next_node
            else:
                previous=current
                current=current.next_node
        return current#best practice to return the removed data
            
    def remove_at_index(self,index):
        position=index
        current=self.head
        prev=None
        if index==0:
            self.head=current.next_node
        else:
            while position>1 and current:
                prev=current
                current=current.next_node
                position-=1
            prev.next_node=current.next_node
        return current
    def remove_at_index_chatGPT(self,index):
        if index < 0:
            # Handle negative index (optional)
            raise ValueError("Index must be non-negative")

        if index == 0:
            # Special case: Removing the head node
            if self.head:
                removed_node = self.head
                self.head = self.head.next_node
                return removed_node
            else:
                raise IndexError("Index out of bounds")

        current = self.head
        prev = None
        position = 0

        while current and position < index:
            prev = current
            current = current.next_node
            position += 1

        if current:
            # Node at the specified index found
            prev.next_node = current.next_node
            return current
        else:
            raise IndexError("Index out of bounds")
    
    def nodeAtIndex(self,index):
        if index==0:
            return self.head
        else:
            current=self.head
            position=0
            while position<index:
                current=current.next_node
                position+=1
            return current

    def __repr__(self) -> str:
        nodes=[]
        current=self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]"%current.data)
            else:
                nodes.append("[%s]" %current.data)
            current=current.next_node
        return '->'.join(nodes)
l=LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l.add(7)


def linkedListReversal(listHead):
    if (listHead.next_node is None or listHead is None):
        return listHead
    returnedValue=linkedListReversal(listHead.next_node)
    listHead.next_node.next_node=listHead
    listHead.next_node=None
    return returnedValue

# def llreversalList(list):
#     if list.head is None or list.size()==1:
#         return list
#     current=list.head
#     returnedVal=linkedListReversal(list.head)
#     list.head=returnedVal
#     return list


# print(llreversalList(l))
# def mergeSortedLinked(list1,list2):
#     returnlist=LinkedList()
#     if list1.head.data<list2.head.data:
#         returnlist.head=list1.head
#         mergeLinkedLists(list1.head.next_node,list2.head)
#     else:
#         returnlist.head=list2.head
#         mergeLinkedLists(list1.head,list2.head.next_node)
#     return returnlist

list1=LinkedList()
list2=LinkedList()
list1.add(12)
list1.add(23)
list1.add(34)
list1.add(45)
list1.add(33)
list1.add(21)
list2.add(1)
list2.add(78)
list2.add(89)
list2.add(99)
list2.add(101)

# result=mergeSortedLinked(list1,list2)
# print(result)

def split(list):
    mid=list.size()//2
    current=list.head
    position=0
    right=LinkedList()
    left=LinkedList()
    while(position<=mid):
        current=current.next_node
        position+=1
    left=current
    right.head=current.next_node
    current.next_node=None
    return left,right


def merge(left,right):
    sortedLink=LinkedList()
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
    sortedLink.head=sortedLink.head.next_node
    return sortedLink



def sortingLinkedLists(list):
    if list.size()<=1:
        return list
    left=LinkedList()
    right=LinkedList()
    left.head,right.head=split(list)
    left_half=sortingLinkedLists(left)
    right_half=sortingLinkedLists(right)
    return merge(left_half,right_half)


result=sortingLinkedLists(list1)