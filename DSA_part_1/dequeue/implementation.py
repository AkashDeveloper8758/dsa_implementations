class Deque:
    def __init__(self,cap) -> None:
        self.cap = cap
        self.size = 0
        self.front = -1
        self.rear = -1
        self.arr = [None]*cap
    
    def insertFront(self,ele):
        if self.isEmpty():
            self.front=0
            self.rear=0
            self.arr[self.front] = ele
            self.size+=1
            return

        tempFront = (self.front -1) %self.cap
        if tempFront == self.rear:
            print('size full')
        else:
            self.front = tempFront
            self.arr[tempFront] = ele
            self.size+=1

    def insertRear(self,ele):
        if self.isEmpty():
            self.front=0
            self.rear=0
            self.arr[self.front] = ele
            self.size+=1
            return
        tempRear = (self.rear+1)%self.cap
        if tempRear == self.front:
            print('size full')
        else:
            self.rear = tempRear
            self.arr[tempRear] = ele
            self.size+=1
    
    def removeFront(self):
        if self.isEmpty():
            print('empty deque')
            return
        if self.front == self.rear:
            # print('remove front : ',self.arr[self.front])
            self.arr[self.front]=None
            self.front = -1
            self.rear  = -1
        else:
            # print('remove front : ',self.arr[self.front])
            tempFront = (self.front+1)%self.cap
            self.arr[self.front] = None
            self.front = tempFront
            self.size-=1

    def removeRear(self):
        if self.isEmpty():
            print('empty deque')
            return
        if self.front == self.rear:
            # print('remove front : ',self.arr[self.front])
            self.arr[self.rear]=None
            self.front = -1
            self.rear  = -1
        else:
            # print('remove front : ',self.arr[self.front])
            self.arr[self.rear] = None
            self.rear = (self.rear-1)%self.cap 
            self.size-=1


    def getFront(self):
        if not self.isEmpty():
            return self.arr[self.front]
        else:
            return None
    def getRear(self):
        if not self.isEmpty():
            return self.arr[self.rear]
        else:
            return None
    def isEmpty(self):
        return self.rear == -1
    def isFull(self):
        return self.size == self.cap

deque = Deque(5)
deque.insertFront(5)
deque.insertFront(6)
deque.insertFront(7)
deque.insertFront(8)
deque.insertRear(1)
deque.removeFront()
deque.insertRear(12)
deque.removeFront()
deque.removeFront()
deque.removeFront()
deque.removeFront()
deque.removeFront()
print('dequeue : ',deque.arr)