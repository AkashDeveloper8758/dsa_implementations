def binarySearchWithFirstIndex(arr,ele):
    n = len(arr)
    high = n-1
    low = 0
    while high >= low:
        mid = (high+low)//2
        if arr[mid] > ele:
            high = mid-1
        elif arr[mid] < ele:
            low = mid +1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid-1
    return -1

def binarySearchWithLastIndex(arr,ele):
    n = len(arr)
    high = n-1
    low = 0
    while high >= low:
        mid = (high+low)//2
        if arr[mid] > ele:
            high = mid-1
        elif arr[mid] < ele:
            low = mid +1
        else:
            if mid == n-1 or arr[mid+1] != arr[mid]:
                return mid
            else:
                low = mid+1
    return -1

def countOccurances(arr,ele):
    n = len(arr)
    high = n-1
    low = 0
    firstIndex = -1
    count = 0
    while high >= low:
        mid = (high+low)//2
        if arr[mid] > ele:
            high = mid-1
        elif arr[mid] < ele:
            low = mid +1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                lastIndex = binarySearchWithLastIndex(arr,ele)
                return lastIndex - mid +1
            else:
                high = mid-1

    if firstIndex> -1:
        while arr[firstIndex] == ele:
            count+=1
            firstIndex +=1
    return count

def binarySearchRecursive(arr,low,high,ele):
    if high <low:
        return -1
    mid = (high+low)//2
    if arr[mid] == ele:
        if mid == 0 or arr[mid-1] != arr[mid]:
            return mid
        else:
            return binarySearchRecursive(arr,low,mid-1,ele)
    if arr[mid] > ele:
        high = mid-1
    else:
        low = mid +1
    return binarySearchRecursive(arr,low,high,ele)


# log(n) time complexity : fastest
def squareRootFloor(num):
    low = 0
    high = num
    ans = -1
    while high>= low:
        mid = (high+low)//2
        square = mid*mid
        if square == num:
            return mid
        if square > num:
            high = mid-1
        else:
            print('mid is: ',mid)
            low = mid+1
            ans = mid
    return ans


def infiniteSearch(arr,ele):
    low = 0
    high = 1
    while arr[high] < ele:
        low = high
        high = high*2
    print('high is : ',high)
    print('low is : ',low)
    while high>= low:
        mid = (high+low)//2
        if arr[mid] == ele:
            return mid

        if arr[mid] > ele:
            high = mid-1
        else:
            low = mid+1
        
    return -1

def searchSmaller(arr,item):
    high = len(arr)
    low = 0
    while high > low:
        mid = (high+low)//2
        if arr[mid] == item:
            return item
        if arr[mid] < item:
            low = mid+1
        else:
            high = mid
    return low-1

# print('search for element : ',binarySearchWithFirstIndex([1,2,5,5,5,6,8,8,9,9,9],5))
# print('search for element : ',countOccurances([1,2,3,3,3,3,4,5,5,5,5,5,5,5,6],5))
# print('square root of number: ',squareRootFloor(24))
myArray = []
for i in range(500):
    myArray.append(i*2)
print('infinite search ',infiniteSearch(myArray,50))
