from audioop import reverse


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        isSwaped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                isSwaped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not isSwaped:
            # the array is already sorted because no swap happen
            print('breakpoint - --------',arr[i])
            break
    print(arr)

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minV = arr[i]
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < minV:
                minV = arr[j]
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    print(arr)

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        # shifting element to correct place in sorted subarray
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    
# most minimum writes on memory with O(n2)
def cycleSort(arr):
    n= len(arr)
    count = 0
    for cs in range(n):
        item = arr[cs]
        pos = cs
        # check no of values less then the item
        for i in range(cs+1,n):
            if arr[i] < item:
                pos+=1

        if pos != cs:
            count+=1
        else: continue

        while item==arr[pos]:
            pos+=1

        arr[pos],item = item,arr[pos]

        # check for other items positions untill it come to [cs] again and complete a cycle
        # if item is already at its correct position then pos will still be equal to cs 
        while pos !=cs:
            pos = cs
            for i in range(cs+1,n):
                if arr[i] < item:
                    pos+=1
            if pos != cs:
                count+=1
            if item == arr[pos]:
                pos +=1
            arr[pos],item = item,arr[pos]
    print('required swaps : ',count)
    return arr


#  time : O(n+k) space : O(n+k)  stable
# if we know the range of the arr is k
def countSort(arr,k):
    count = [0]*k
    n = len(arr)
    # count the no of occurance of item in array and store in count arr at its index
    for i in range(n):
        count[arr[i]] +=1
    # conunt no of element equal to or less then item
    for i in range(1,k):
        count[i] += count[i-1]
    
    output = [0]*(n)
    for i in range(n-1,-1,-1):
        # take the count of item in count[] arr and subtrace by 1 after 
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]]-=1
    for i in range(n):
        arr[i] = output[i]
    return arr

def bucketSort(arr,k):
    n = len(arr)
    maxV = arr[0]
    for i  in range(n):
        if arr[i] > maxV:
            maxV = arr[i]
    maxV+=1
    bucket = [[] for i in range(k)]
    for i in range(n):
        index = (arr[i] * k )//maxV
        bucket[index].append(arr[i])
    for i in range(k):
        bucket[i].sort()
    ind = 0
    for i in range(k):
        for j in range(len(bucket[i])):
            arr[ind] = bucket[i][j]
            ind+=1
    print(arr)
        

    
    

# bubbleSort([3,5,4,2,7,1,5])
# selectionSort([90,80,90,25])
# insertionSort([3,5,4,2,7,1,5])
# print('cycle sort : ',cycleSort([1,5,3,4,8,6,6,3,3,4,3,5]))
# print('count sort : ',countSort([1,5,2,4,3,1,5],6))
bucketSort([1,2,6,4,3,2],3)



