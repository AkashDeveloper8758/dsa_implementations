class Node:
    def __init__(self,data:int,next=None) -> None:
        self.data = data
        self.next = next

def traverseCLL(head:Node):
    if head ==None:
        return
    curr = head
    while curr.next != head:
        print(curr.data,end=' ')
        curr = curr.next
    print(curr.data,end=' ')

def insertAtBeginningCLL(head:Node,data):
    newNode = Node(data)
    if head ==None:
        newNode.next = newNode
        return newNode
    newNode.next = head.next
    head.next = newNode
    head.data,newNode.data = newNode.data,head.data
    return head

def insertAtEndCLL(head:Node,data):
    newNode = Node(data)
    if head == None:
        newNode.next = newNode
        return newNode
    newNode.next = head.next
    head.next = newNode
    head.data,newNode.data = newNode.data,head.data
    # change the head to next new node, which make the first node last automatically
    head = newNode
    return head

def deleteHeadOfCLL(head:Node):
    if head == None or head.next == None:
        return None
    # copy the second node data in head
    # delete the second node
    head.data = head.next.data
    head.next = head.next.next
    return head

#assumption :  N >= k
def deleteKthElementInCLL(head:Node,k):
    if head == None:
        return None
    if k==1:
        return deleteHeadOfCLL(head)
    i=1
    curr = head
    while i<k-1:
        curr = curr.next
        i+=1
    curr.next = curr.next.next
    return head
        

head = Node(1)
node2 = Node(2)
node3 = Node(3)
head.next = node2
node2.next = node3
node3.next = head
traverseCLL(head)
head = insertAtBeginningCLL(head,10)
head = insertAtEndCLL(head,50)
head = insertAtBeginningCLL(head,20)
head = insertAtEndCLL(head,60)
head = deleteHeadOfCLL(head)
print('\nbefore delete : ')
traverseCLL(head)
print('\nafter delete : ')

head = deleteKthElementInCLL(head,1)
head = deleteKthElementInCLL(head,5)
traverseCLL(head)