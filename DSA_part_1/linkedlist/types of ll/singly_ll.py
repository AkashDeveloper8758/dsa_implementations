class Node:
    def __init__(self,data:int,next=None) -> None:
        self.data = data
        self.next = next

def traverseLinkedList(head:Node):
    curr = head
    while curr != None:
        print(curr.data,end=' ')
        curr = curr.next

def insertAtBeginning(head:Node,data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head

def insertAtEnd(head:Node,data):
    newNode = Node(data)
    if head == None:
        return newNode
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newNode
    newNode.next = None
    return head

def deleteFirstNode(head):
    if head == None:
        return None
    head = head.next
    return head

def deleteLastNode(head:Node):
    if head == None:
        return None
    if head.next == None:
        return None
    curr:Node = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head

def insertAtPosition(head,pos,data):
    newNode = Node(data)
    if head == None:
        return None
    if pos==0:
        newNode.next = head
        return newNode
    curr = head
    i =1
    while curr!=None and i<pos:
        curr = curr.next
        i+=1
    if curr == None:
        print('index exceeds the length of LL')
        return head
    newNode.next = curr.next
    curr.next=newNode
    return head

def searchInLinkedList(head,data):
    if head == None:
        return -1
    if head.data == data:
        return 0
    curr = head
    i=0
    while curr!=None:
        if curr.data == data:
            return i
        i+=1
        curr = curr.next
    return -1

def searchInLLRecursive(head,data):
    if head==None:
        return -1
    if head.data == data:
        return 1
    pos = searchInLLRecursive(head.next,data)
    if pos ==-1:
        return -1
    return pos+1
    

head = Node(5)
node2 = Node(6)
node3 = Node(7)
head.next= node2
node2.next = node3
node3.next = None
# head = insertAtBeginning(head,10)
# head = insertAtBeginning(head,12)

# we are assigning new head in end insertion,
# as curr head can be null then comming head will be new head

head = insertAtEnd(head,50)
head = insertAtEnd(head,60)
# traverseLinkedList(head)
# head = deleteFirstNode(head)
# head = deleteLastNode(head)
head = insertAtPosition(head,3,100)
traverseLinkedList(head)
print('')
print('index : ',searchInLLRecursive(head,44))