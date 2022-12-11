# stack with current min, in time: O(1) and space: O(1)

class Stack:
    def __init__(self) -> None:
        self.arr = []
        self.currMin = None

    def push(self,ele):
        if len(self.arr) ==0:
            self.arr.append(ele)
            self.currMin = ele
        elif ele <= self.currMin:
            # value will always be smaller then currmin
            value = 2*ele - self.currMin
            self.arr.append(value)
            self.currMin = ele
        else:
            self.arr.append(ele)

    def pop(self):
        if len(self.arr) >0:
            t = self.arr[-1]
            #  if less then currmin then it is a special element
            if t<=self.currMin:
                res = self.currMin
                self.currMin = 2*self.currMin - t
                return res
            else:
                return t

    def peek(self):
        if len(self.arr) >0:
            if self.arr[-1] <= self.currMin:
                return self.currMin
            else:
                return self.arr[-1]
        else:
            print('empty stack')
            return -1
    def getMin(self):
        return self.currMin
        # return self.minArr[-1] if len(self.minArr) > 0 else math.inf

    def isEmpty(self):
        return self.top ==-1
    
    def size(self):
        return self.top+1

myStack = Stack()
myStack.push(5)
myStack.push(10)
myStack.push(20)
myStack.push(2)
print('curr min : ',myStack.getMin())
myStack.push(6)
myStack.push(4)
myStack.pop()
myStack.pop()
myStack.push(2)
print('curr min : ',myStack.getMin())
myStack.pop()
myStack.push(1)
print('curr min : ',myStack.getMin())
myStack.pop()
myStack.pop()


