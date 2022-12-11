def maxHeapify(arr,n,i):
    left,right = i*2+1, i*2+2
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        maxHeapify(arr,n,largest)

# parent of last node : (n-2)/2
def buildHeap(arr):
    n = len(arr)
    for i in range((n-2)//2,-1,-1):
        maxHeapify(arr,n,i)
    return arr

# repeatedly swap root with last node and reduce heap size by one and heapify
def heapSort(arr):
    buildHeap(arr)
    n=len(arr)
    for i in range(n-1,0,-1):
        # swap with the first element in max heap with the last element
        arr[i],arr[0] = arr[0],arr[i]
        # redece max heap size by 1 with i, and heapify first position again
        maxHeapify(arr,i,0)
    return arr

arr = [7,6,5,4,3,2,1,8,9,10]
print('heap sort : ',heapSort(arr))