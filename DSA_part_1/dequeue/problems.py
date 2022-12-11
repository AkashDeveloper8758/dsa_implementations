from collections import deque

def maxOfSizeK(arr,k):
    n = len(arr)
    mydeq = deque()
    for i in range(k):
        # can ever be greater then 2n, in whole function execution
        while len(mydeq)>0 and arr[i] >= arr[mydeq[-1]]:
            mydeq.pop()
        mydeq.append(i)

    for i in range(k,n):
        print(arr[mydeq[0]],end=' ')
        # remove elements from front when they are less then i-k
        while len(mydeq)>0 and mydeq[0] <= i-k:
            mydeq.popleft()
        # remove elements from end until arr[i] is greater then elements in dequeue
        while len(mydeq) >0 and arr[i] >= arr[mydeq[-1]]:
            mydeq.pop()
        mydeq.append(i)
    print(arr[mydeq[0]])
s
def circularPetrolTourEff(petrol,dist):
    curr=0
    prev = 0
    start = 0
    for i in range(len(petrol)):
        curr += petrol[i] - dist[i]
            # when distance become less then zero
        if curr <0:
            # stat is i+1 because point before p(i) can't be possible if p(i-1) is neg
            start = i+1
            # increse prev += curr as to total neg values
            # to finally compare with the remaining petrol at the end
            prev+=curr
            curr = 0
    return start+1 if curr+prev >=0 else -1
    

# maxOfSizeK([10,8,5,12,15,7,6],3)
# maxOfSizeK([20,40,30,30,30,30,10,60],3)
print('petrol point : ',circularPetrolTourEff([50,10,60,100],[30,20,100,10]))