from queue import LifoQueue

def matching(a,b):
    check = (a=='(' and b==')') or (a == '[' and b == ']') or (a=='{' and b=='}')
    return check
def checkParantheses(string):
    stack = LifoQueue()
    opening = ['(','{','[']
    for i in range(len(string)):
        if string[i] in opening:
            stack.put(string[i])
        else:
            if stack.empty():
                return False
            peekEle = stack.get()
            if not matching(peekEle,string[i]):
                return False
    return stack.empty()

class TwoStack:
    def __init__(self,cap) -> None:
        self.cap = cap
        self.top1 = -1
        self.top2 = cap
        self.arr = [None]*cap

    def push1(self,ele):
        if self.top1 < self.top2-1:
            self.top1+=1
            self.arr[self.top1] = ele
        else:
            print('stack 1 full')

    def push2(self,ele):
        if self.top1 < self.top2-1:
            self.top2-=1
            self.arr[self.top2] = ele
        else:
            print('stack 2 full')

    def pop1(self):
        if self.top1 != -1:
            value = self.arr[self.top1]
            self.top1-=1
            return value
        else:
            print('stack 1 empty')

    def pop2(self):
        if self.top2 != self.cap:
            value = self.arr[self.top1]
            self.top1-=1
            return value
        else:
            print('stack 2 empty')

    def isEmpty(self):
        return self.top1 < self.to2-1


# time : O(n) as every element is pushed and poped  in stack only once,
# so total 2n operation while n iteration
# space : O(n)
def printSpanOfElements(arr):
    stack = LifoQueue()
    n = len(arr)
    stack.put(0)
    print(1,end=' ') 
    for i in range(1,n):
        # while we found the element greater then, in stack
        while stack.empty() == False and arr[stack.queue[-1]] <= arr[i]:
            stack.get()

        span = i+1 if stack.empty() else i-stack.queue[-1]
        print(span,end=' ')
        stack.put(i)

def previousGreater(arr):
    stack = LifoQueue()
    n = len(arr)
    print(-1,end=' ')
    stack.put(arr[0])
    for i in range(1,n):
        while not stack.empty() and stack.queue[-1] <= arr[i]:
            stack.get()
        ele = -1 if stack.empty() else stack.queue[-1]
        print(ele,end=' ')
        stack.put(arr[i])


def nextGreater(arr):
    stack = LifoQueue()
    n = len(arr)
    ansArr = [-1]
    stack.put(arr[-1])
    for i in range(n-2,-1,-1):
        while not stack.empty() and stack.queue[-1] <= arr[i]:
            stack.get()
        ele = -1 if stack.empty() else stack.queue[-1]
        ansArr.append(ele)
        stack.put(arr[i])
    print(list(reversed(ansArr)))




# printSpanOfElements([60,10,20,15,35,50])
# previousGreater([12,10,8,13,16,5,8])
# nextGreater([5,15,10,8,6,12,9,18])

# twoStack = TwoStack(6)
# twoStack.push1(3)
# twoStack.push1(4)
# twoStack.push1(4)
# twoStack.push1(5)
# print('stack data : ',twoStack.arr)
# twoStack.push2(9)
# twoStack.push2(8)
# twoStack.push2(7)
# print('stack data : ',twoStack.arr)
# twoStack.pop1()
# twoStack.pop1()
# twoStack.pop1()
# twoStack.pop1()
# twoStack.pop1()



# print('paranthesis check: ',checkParantheses('{}([(){])'))