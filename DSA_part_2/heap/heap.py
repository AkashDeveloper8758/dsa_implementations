class MinHeap:
    def __init__(self):
        self.arr = []
        self.size = 0
        # self.cap = cap

    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-1)//2

    def insert(self,item):
        self.arr.append(item)
        # heapify the insert
        i = len(self.arr)-1
        while i!=0 and self.arr[self.parent(i)] > self.arr[i]:
            # swap the parent and child
            self.arr[self.parent(i)],self.arr[i] = self.arr[i],self.arr[self.parent(i)]
            i = self.parent(i)    

    def minHeapify(self,i):
        size = len(self.arr)
        lt = self.left(i)
        rt = self.right(i)
        smallest=i
        if lt < size and self.arr[lt] < self.arr[i]:
            smallest = lt
        if rt < size and self.arr[rt] < self.arr[smallest]:
            smallest = rt
        if smallest != i:
            # swap, if root is not the smallest
            self.arr[smallest],self.arr[i] = self.arr[i],self.arr[smallest]
            self.minHeapify(smallest)

    
    def minHeapify2(self,i):
        left = self.left(i)
        right= self.right(i)
        smallest = i
        size = len(self.arr)
        if left < size and self.arr[left] < self.arr[i]:
            smallest = left
        if right < size and self.arr[right] < self.arr[smallest]:
            smallest = right
        if i!= right:
            self.arr[i],self.arr[smallest] = self.arr[smallest],self.arr[i]
            self.minHeapify(smallest)
    
    def extraceMinHeap(self) -> int:
        if len(self.arr) == 0:
            return -1
        if len(self.arr) == 1:
            return self.arr.pop()
        minv = self.arr[0]
        # put the largest at the top place and call the minheapify for 0th index and remove that last element
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.minHeapify(0)
        return minv

    # include increase and decrease of the key
    def updateKey(self,i,value):
        if len(self.arr) == 0:
            return
        if i > len(self.arr)-1:
            print('invalid index to update')
            return
        self.arr[i] = value
        # if its childrens are smaller then arr[i], then minheapify will be done
        self.minHeapify(i)
        # check with parent
        while i!= 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)],self.arr[i] = self.arr[i],self.arr[self.parent(i)]
            i = self.parent(i)
    
    def deleteIndex(self,i):
        if len(self.arr) == 0:
            return
        deletedKey = self.arr[i]
        # insert the last index
        self.arr[i] = self.arr[-1]
        self.arr.pop()
        self.minHeapify(i)
        return deletedKey

    def heapSort(self):
        if len(self.arr) == 0:
            return
        

# nlogn
def buildHeap(arr):
    myheap = MinHeap()
    for value in arr:
        myheap.insert(value)
    return myheap

# it looks like time complexity is:  nlogn but mathametically it is O(n) for buildheap2
def buildHeap2(arr):
    myheap = MinHeap()
    myheap.arr = arr
    size = len(myheap.arr)
    for i in range((size-2)//2,-1,-1):
        myheap.minHeapify(i)
    return myheap

