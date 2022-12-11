import math
from heap import MinHeap,buildHeap
from typing import List
import heapq


# myheap = MinHeap()
# myheap.insert(1)
# myheap.insert(12)
# myheap.insert(17)
# myheap.insert(27)
# myheap.insert(34)
# myheap.insert(15)
# myheap.insert(13)
# print(myheap.arr)

# heap2 = buildHeap([10,12,17,27,34,15,13])
# print(f'heap 2: {heap2.arr}')


# on averate it will performe much better then sorting solution
def purchasingMaxItems(arr,totalSum):
    newHeap = buildHeap(arr)
    count = 0

    while totalSum > 0:
        # logn
        minv = newHeap.extraceMinHeap()
        if minv < totalSum:
            totalSum -= minv
            count+=1
        else:
            return count
    return count

#* k largest elements
# method 1: use max heap, remove top for k time to get k largest elements : n + klogn
# method 2: use min heap, store first k items in min heap
#           from k+1 in list, compare with the root and if smaller,
#           remove from the top, and add the k+nth element in the min heap
#           => and finally we will have min heap containing k largest elements : [k + (n-k)logk] < [n + klogn]


# k closest near the x
# time : kn
def printKclosest(arr,k,x):
    n = len(arr)
    visited = [False]*n
    for i in range(k):
        minInd= -1
        minDiff = math.inf
        for j in range(n):
            if visited[j] == False and abs(arr[j]-x) <= minDiff:
                minDiff = abs(arr[j]-x)
                minInd = j
        print(arr[minInd],end=' ')
        visited[minInd] = True
    

# time : nk.log(k)
# idea: store first min k values in k-min-heap , pop the min-heap and add the same element from kth-array which is popped 
class KElement:
    def __init__(self,item,array_pos,item_pos):
        self.item = item
        self.array_pos = array_pos
        self.item_pos = item_pos
    def __lt__(self,other:object):
        return self.item <= other.item

# time : nk.log(k), most efficient time solution
def mergeKSortedEff(arr:List[List],k):
    # maintaining the array position improve the 
    mheap:List[KElement] = []
    res = []
    # push first elements from k-arrays
    for i in range(k):
        item = KElement(arr[i][0],i,0)
        mheap.append(item)
    # heapify them
    heapq.heapify(mheap)
    while mheap:
        minv = heapq.heappop(mheap)
        res.append(minv.item)
        arrayPos = minv.array_pos
        itemPos = minv.item_pos

        # check if items left in the arrayPos-th-> array
        if itemPos+1 < len(arr[arrayPos]):
            pushItem= KElement(arr[arrayPos][itemPos+1], minv.array_pos, itemPos+1)
            heapq.heappush(mheap,pushItem)
    return res


# print('max count : ',purchasingMaxItems([1,12,5,111,200],10))
print('merge k sorted value : ',mergeKSortedEff([[7,8,10],[2,6,9],[1,3,5]],3))

