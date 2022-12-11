# implementation of a queue with circular array
class Queue:
    def __init__(self,cap) -> None:
        self.cap = cap
        self.front = -1
        self.rear = -1
        self.queue = [None]*cap

    def enqueue(self,ele):
        if self.front == -1:
            self.rear+=1
            self.front+=1
            self.queue[self.rear] = ele
        elif (self.rear + 1 ) % self.cap != self.front:
            self.rear = (self.rear + 1 ) % self.cap
            self.queue[self.rear] = ele
        else:
            print('queue is full')

    def dequeue(self):
        if self.front == -1 or (self.front +1)%self.cap == self.rear:
            print('queue is empty')
        else:
            print('deque : ',self.queue[self.front])
            self.queue[self.front] = None
            self.front = (self.front +1)%self.cap
            
    def getSize(self):
        return abs(self.front - self.rear)+1

    def getFront(self):
        if self.front == -1:
            print('queue is empty')
        else:
            return self.queue[self.front]
    def getLast(self):
        if self.front ==-1:
            print('queue is empty')
        else:
            return self.queue[self.rear]




# myqueue = Queue(5)
# myqueue.enqueue(10)
# myqueue.enqueue(20)
# myqueue.enqueue(30)
# myqueue.enqueue(40)
# myqueue.enqueue(50)
# myqueue.dequeue()
# myqueue.dequeue()
# myqueue.enqueue(60)
# myqueue.enqueue(70)
# myqueue.dequeue()
# myqueue.enqueue(80)
# print('my queue : ',myqueue.queue)
        

    

    

        