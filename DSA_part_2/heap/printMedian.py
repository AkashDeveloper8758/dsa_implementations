from typing import List
import heapq

class MaxHeapObj:
    def __init__(self,val):
        self.val = val
    def __lt__(self,other):
        # reverse the less then operation, so it act as a maxheap
        return self.val > other.val
    def __repr__(self) -> str:
        return str(self.val)


def printMedian(arr):
    #* smaller will be maxheap
    s = []
    #* greater will be minheap
    g = []
    # add first element in smaller maxheap
    heapq.heappush(s,MaxHeapObj(arr[0]))
    print(arr[0],end=' ')
    for i in range(1,len(arr)):
        x = arr[i]
        # if smaller has more elements then greater
        # we will always maintain diff of 1 bw smaller and greater
        if len(s) > len(g):
            if s[0].val > x:
                # to maintain 1-diff, remove from small-> add to greater, then add current to smaller
                v = heapq.heappop(s)
                heapq.heappush(g,v.val)
                heapq.heappush(s,MaxHeapObj(x))
            else:
                heapq.heappush(g,x)
            #even elements are present here 
            print((s[0].val + g[0])/2,end=', ')
        else:
            if s[0].val > x:
                heapq.heappush(s,MaxHeapObj(x))
            else:
                heapq.heappush(g,x)
                polledItem = heapq.heappop(g)
                heapq.heappush(s,MaxHeapObj(polledItem))
            print(s[0],end=', ')    

printMedian([12,15,10,5,8,7,16])