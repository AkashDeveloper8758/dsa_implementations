from queue import LifoQueue
q = LifoQueue()
q.put(10)
q.get()
q.em


class Node:
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next


class LinkedQueue:
    def __init__(self,head=None) -> None:
        self.head = head
        self.tail = self.head
        self.size = 0
    
    def enqueue(self,ele):
        newNode = Node(ele)
        # first node in queue
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size +=1
    
    def dequeue(self):
        if self.head == None:
            print('queue is empty')
        else:
            # print('dequeu : ',self.head.data)
            self.head = self.head.next
            self.size-=1
    
    def sizeOfQueue(self):
        return self.size
    
    def getFront(self):
        if self.head != None:
            return self.head.data
        else:
            print('queue has no element')
    
    def getEnd(self):
        if self.head != None:
            return self.tail.data
        else:
            print('empty queue')

    def printQueue(self):
        if self.head == None:
            print('empty queue')
            return
        curr = self.head
        while curr != None:
            print(curr.data,end=' ')
            curr = curr.next
    
    def isEmpty(self):
        return self.head == None

# queue = LinkedQueue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.dequeue()
# queue.dequeue()
# queue.enqueue(50)
# print('---------------------')
# print('end : ',queue.getEnd())
# print('start : ',queue.getFront())
# print('size : ',queue.sizeOfQueue())
# print('---------------------')

# queue.printQueue()
