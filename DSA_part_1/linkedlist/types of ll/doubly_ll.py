class Node:
    def __init__(self,data:int,next=None,prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

def traverseLinkedList(head:Node):
    if head == None:
        return
    curr = head
    while curr != None:
        print(curr.data,end=' ')
        curr = curr.next

def insertAtBeginning(head:Node,data):
    newNode = Node(data)
    newNode.next = head
    if head == None:
        return newNode
    # newNode.prev = head.prev
    head.prev = newNode
    return newNode

def insertAtEnd(head:Node,data):
    newNode = Node(data)
    if head== None:
        return newNode
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newNode
    newNode.prev = curr
    return head

def reverseDLL(head:Node):
    if head == None or head.next == None:
        return head
    prev = None
    curr = head
    while curr!=None:
        # we are swapping next and prev of the node
        # making all the links reverse
        prev = curr.prev
        curr.prev = curr.next
        curr.next = prev
        curr = curr.prev
    return prev.prev

def deleteHeadOfDLL(head:Node):
    if head == None:
        return head
    if head.next == None:
        return None
    head = head.next
    head.prev = None
    return head

def deleteLastInDLL(head:Node):
    if head==None or head.next==None:
        return None
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.prev.next = None
    return head


head = Node(1)
node1 = Node(2)
node2 = Node(3)

head.next = node1

node1.prev = head
node1.next = node2

node2.prev = node1
node2.next = None

head = insertAtBeginning(head,10)
head = insertAtEnd(head,100)
print('previous : ')
traverseLinkedList(head)
head = deleteHeadOfDLL(head)
head = deleteLastInDLL(head)
print('after : ')
traverseLinkedList(head)
