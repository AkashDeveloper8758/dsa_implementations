class Node:
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next

def traverseLinkedList(head:Node):
    curr = head
    while curr != None:
        print(curr.data,end=' ')
        curr = curr.next
    

def detectLoop(head:Node):
    if head == None:
        return False
    fast = head
    slow = head
    while fast!=None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

def detectionAndRemovalOfLoop(head:Node):
    # make end of loop next to null, and loop will break
    # first detect the loop with floyd cycle detection, 
    slow,fast = head,head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if fast != slow:
        return 
    # move the slow to the beginning
    slow = head
    # move fast and slow at the same step if  their next become same, then fast is at end of the loop
    print('fast : ',fast.data)
    print('slow : ',slow.data)
    while slow.next != fast.next and fast.next != slow:
        slow = slow.next
        fast = fast.next
    fast.next = None

def deleteNodeWithOnlyPointer(ptr:Node):
    if ptr.next == None:
        print('last element')
        return 
    ptr.data = ptr.next.data
    ptr.next = ptr.next.next

def segregateEvenAndOdd(head:Node):
    if head == None:
        return head
    # create even and odd stat/end pointers, when encounter even append even end and vice versa
    evenS,evenE,oddS,oddE = None,None,None,None
    curr = head
    while curr!=None:
        if curr.data %2==0:
            if evenS == None:
                evenS = curr
                evenE = evenS
            else:
                evenE.next = curr
                evenE = curr
        else:
            if oddS == None:
                oddS = curr
                oddE = oddS
            else:
                oddE.next = curr
                oddE = curr
        curr = curr.next
    # if any of the odd or even list is null, means list is already segregated
    if oddS == None or evenS == None:
        return head
    evenE.next = oddS
    oddE.next = None
    return evenS

# time : O(m+n) space : O(m)
def findIntersectionOfTwoNode(head1:Node,head2:Node):
    if head1 == None or head2==None:
        return -1
    nodeSet = set()
    curr=head1
    while curr != None:
        nodeSet.add(curr)
        curr = curr.next
    curr = head2
    while curr != None:
        if curr in nodeSet:
            return curr.data
        curr = curr.next
    return -1

# time : O(m+n) space : O(1)
def findIntersectionEff(head1:Node,head2:Node):
    if head1 == None or head2==None:
        return -1
    len1,len2 = 0,0
    curr = head1
    while curr != None:
        len1+=1
        curr = curr.next
    curr = head2
    while curr!=None:
        len2 +=1
        curr =curr.next
    big,small = None,None
    if len1 > len2:
        big = head1
        small = head2
    else:
        big = head2
        small = head1
    curr = big
    diff = abs(len1-len2)
    count =0
    while count < diff:
        curr = curr.next
        big = curr
        count+=1
    while big != None:
        if big == small:
            return big.data
        big = big.next
        small = small.next
    return -1

def pairswap(head:Node):
    if head==None:
        return None
    curr = head
    while curr != None and curr.next != None:
        curr.data,curr.next.data = curr.next.data,curr.data
        curr = curr.next.next

# -------------------------------------------------
# LRU Cache Implementation required : 
# 1. hashTable with {10 : Node(data:10)}
# 2. doubly linked list with tail pointer
# -------------------------------------------------

def mergeSortedLLinPlace(a:Node,b:Node):
    if a == None:
        return b
    elif b == None:
        return b

    newHead,tail = None,None

    if a.data >= b.data:
        newHead = b
        tail = b
        b = b.next
    else:
        newHead = a
        tail = a
        a = a.next
    
    while a != None and b != None:
        if b.data >= a.data:
            tail.next = a
            tail = a
            a = a.next
        else:
            tail.next = b
            tail = b
            b = b.next
    if a == None:
        tail.next = b
    else:
        tail.next = a
    return newHead

def palindromeLinkedList(head):
    if head == None:
        return False
    curr = head
    # reverse ll
    tempHead = head
    curr = curr.next
    while curr != None:
        newNode = Node(curr.data)
        newNode.next = tempHead
        tempHead = newNode
        curr = curr.next

    curr = head
    curr2 = tempHead
    while curr!= None:
        if curr.data != curr2.data:
            return False
        curr = curr.next
        curr2 = curr2.next
    return True

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

def palindromeCheckEff(head):
    if head == None:
        return None
    curr = head
    fast = head
    slow = head
    # find middle
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    rev = reverseALinkedList(slow.next)
    curr = head
    while rev != None:
        if rev.data != curr.data:
            return False
        rev = rev.next
        curr = curr.next

    return True

    
    


head= Node('M')
node1 = Node('A')
node2 = Node('A')
node3 = Node('R')
# node4 = Node('R')

# head= Node(4)
# node1 = Node(6)
# node2 = Node(9)
# node3 = Node(12)

# head2= Node(3)
# node12 = Node(5)
# node22 = Node(10)
# node32 = Node(24)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = head
# node4.next = None

# head2.next = node12
# node12.next = node22
# node22.next = node32
# node32.next = None


# print('head : ')
# traverseLinkedList(head)
# print()
# print('head2 : ')
# traverseLinkedList(head2)
# print()
# print('merged : ')
# mergedHead = mergeSortedLLinPlace(head,head2)
# traverseLinkedList(mergedHead)

detectionAndRemovalOfLoop(head)
traverseLinkedList(head)
# print('after pair swap')
# print('')
# pairswap(head2)
# traverseLinkedList(head2)
# print('intersection point : ',findIntersectionEff(head,head2))
# head = segregateEvenAndOdd(head)
# deleteNodeWithOnlyPointer(head)


# print('is palindrome: ',palindromeCheckEff(head))