from queue import LifoQueue

class Stack:
    def __init__(self,cap) -> None:
        self.cap = cap
        self.top = -1
        self.arr = []

    def push(self,ele):
        if self.top < self.cap-1:
            self.arr.append(ele)
            self.top+=1
            print('cap,top: ',[self.cap,self.top])
        else:
            print('stackoverflow')
            return

    def pop(self):
        if self.top > -1:
            element = self.arr.pop()
            self.top-=1
            return  element
        else:
            print('stack underflow')

    def peek(self):
        if len(self.arr) >0:
            return self.arr[self.top]
        else:
            print('empty stack')
            return -1

    def isEmpty(self):
        return self.top ==-1
    
    def size(self):
        return self.top+1

myStack = Stack(5)
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.pop()
myStack.pop()
print('is empty: ',myStack.isEmpty())
myStack.pop()
myStack.pop()
print('is empty: ',myStack.isEmpty())
myStack.pop()
print('stack data : ',myStack.arr)