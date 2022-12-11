def secondLargest(array):
    largest = array[0]
    secondLargest = -1
    for i in range(len(array)):

        if array[i] > largest:
            secondLargest = largest
            largest = array[i]
        elif array[i] < largest:
            if array[i] > secondLargest:
                secondLargest = array[i]


    return secondLargest

# check sorted or not in both order
def checkIfArrayIsSorted(arr):
    prev = None
    isAsc = None
    for a in arr:
        if prev == None:
            prev = a
        else:
            if isAsc == None:
                if a > prev:
                    isAsc = False
                elif a < prev:
                    isAsc = True
                else:
                    prev = a
            else:
                if isAsc and a > prev:
                    return False
                if not isAsc and a < prev:
                    return False
                prev = a

    return True

def reverseArray(arr):
    start = 0
    end = len(arr) -1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end -=1
    return arr

# efficient
def removeDuplicate(arr):
    res = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[res-1]:
            arr[res] = arr[i]
            res +=1
    print('arr : ',arr)
    return res

# most efficient
def moveZeroToEnd(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[count] = arr[count],arr[i]
            count +=1
    return arr

# 1 1 1 1 0 0 0
# count = 4

# left rotate with aux O(d)
def leftRotateByN(arr,d):
    firstArr = []
    n = len(arr)
    for i in range(d):
        firstArr.append(arr[i])
    for i in range(d,n):
        arr[i-d] = arr[i]
    for i in range(0,d):
        arr[n-d+i] = firstArr[i]
    return arr

def reverseBw(arr,low,high):
    while low<high:
        arr[low],arr[high] = arr[high],arr[low]
        low+=1
        high-=1

# left rotate with aux O(1) with reversal
def leftRotateEfficient(arr,d):
    n = len(arr) -1
    reverseBw(arr,0,d-1)
    reverseBw(arr,d,n)
    reverseBw(arr,0,n)
    return arr

# print('second largest: ',secondLargest([10,10,10,9]))
# print('reverse : ',reverseArray([1,2,3,4,5,6]))
# print('remove duplicate: ',removeDuplicate([1,2,3,3,4,4,4,5,5,5,9,9]))
# print('move zeros to end: ',moveZeroToEnd([1,5,0,0,2,0,4,5,0,1]))
# print('left move: ',leftRotateByN([1,2,3,4,5,6],3))
print('left move: ',leftRotateEfficient([1,2,3,4,5,6],3))
