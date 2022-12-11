class Node:
    def __init__(self,data:int,next=None) -> None:
        self.data = data
        self.next = next

def traverseLinkedList(head:Node):
    curr = head
    while curr != None:
        print(curr.data,end=' ')
        curr = curr.next
    
def insertSorted(head,data):
    newNode = Node(data)
    # has no element
    if head == None:
        return newNode
    
    if data < head.data:
        newNode.next = head
        return newNode
    
    curr = head
    while curr.next !=None and curr.next.data < data:
        curr = curr.next

    newNode.next = curr.next
    curr.next = newNode
    return head

def middleOfLinkedList(head:Node):
    if head == None :
        return None
    n = 1
    curr = head
    while curr.next != None:
        curr =curr.next
        n+=1
    n = n//2
    i=0
    curr =head
    while i<n:
        curr = curr.next
        i+=1
    return curr.data

def middleOfLinkedListEff(head:Node):
    if head == None :
        return None
    fast = head
    slow = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# 1 indexing
def nthNodeFromEnd(head:Node,pos):
    if head == None:
        return
    i=1
    fast = head
    while i<pos:
        fast = fast.next
        i+=1
        if fast == None:
            return
    slow = head
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    return slow.data

# iterative
def reverseALinkedList(head:Node):
    if head == None or head.next == None:
        return head
    curr = head
    prev = None
    while curr!= None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
# recursive
def reverseLLRecursive(curr,prev=None):
    if curr == None:
        return prev
    next = curr.next
    curr.next = prev
    return reverseLLRecursive(next,curr)

def removeDuplicates(head:Node):
    curr = head
    while curr != None and curr.next != None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

def reverseLLinGroups(head,k):
    curr = head
    prev = None
    next = None
    i=0
    while curr != None and i<k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i+=1
    if next != None:
        restHead = reverseLLinGroups(next,k)
        head.next = restHead
    return prev

def reverseKIterative(head,k):
    isFirstPass = True
    curr = head
    prevFirst = None
    while curr!= None:
        first = curr
        count = 0
        prev = None
        while curr!= None and count<k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count+=1
        if isFirstPass:
            # if it is the first pass, then set the head because there is not previous pass
            head = prev
            isFirstPass = False
        else:
            # else we will link prevFirst.next as current
            prevFirst.next = prev
        prevFirst = first
    return head


    

        

head = Node(5)
head = insertSorted(head,12)
head = insertSorted(head,12)
head = insertSorted(head,16)
head = insertSorted(head,16)
head = insertSorted(head,2)
# head = insertSorted(head,2)
head = insertSorted(head,3)
head = insertSorted(head,3)
head = insertSorted(head,1)
head = insertSorted(head,24)
head = insertSorted(head,7)
head = insertSorted(head,6)
head = insertSorted(head,9)
# head = insertSorted(head,1)
traverseLinkedList(head)
print('\n after reversal : ')
# removeDuplicates(head)
head = reverseLLinGroups(head,3)
traverseLinkedList(head)
print('\n after reversal : 2')
head = reverseKIterative(head,3)

traverseLinkedList(head)
# print('\nlast nth is: ',nthNodeFromEnd(head,0))
# print('\nlast nth is: ',nthNodeFromEnd(head,10))
# print('middle is: ',middleOfLinkedListEff(head))
