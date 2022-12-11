from functools import cmp_to_key
def quickPartationLomuto(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def kthSmallestElement(arr,k):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        p = quickPartationLomuto(arr,low,high)
        if p==k-1:
            return arr[p]
        elif p > k-1:
            high = p-1
        else:
            low = p+1
    return -1

def chocolateDistributionProblem(arr,m):
    n = len(arr)
    if m>n:
        return -1
    arr.sort()
    res = arr[m-1] -arr[0]
    i=0
    while i+m-1 < n:
        res = min(res,arr[i+m-1]-arr[i])
        i+=1
    return res

def segregateNegetives(arr):
    j,i=0,0
    n = len(arr)
    for i in range(n):
        if arr[i] < 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr

# by hoares partation around 1
# Dutch national flag
# we will maintain three window for 0,1,2
# before low : 0
# before mid : 1
# after high : 2
# between mid and high is : unknown -> which is to be compared
def sort012(arr):
    n=len(arr)
    low = 0
    mid = 0
    high = n-1
    while mid<=high:
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[high],arr[mid] = arr[mid],arr[high]
            high-=1
    return arr
    
def minDifference(arr):
    n = len(arr)
    if n==1:
        return float('inf')
    arr.sort()
    minV = float('inf')
    for i in range(n-1):
        subValue =  arr[i+1] - arr[i]
        if subValue < minV:
            minV = subValue
    return minV

# O(nLog(n))
def mergeOverlappingIntervals(arr):
    n = len(arr)
    arr.sort(key=cmp_to_key(lambda a,b: 1 if a[0] >= b[0] else -1 ))
    res = 0
    for i in range(1,n):
        if arr[res][1] >= arr[i][0] :
            arr[res][0] = min(arr[i-1][0],arr[i][0])
            arr[res][1] = max(arr[i-1][1],arr[i][1])
        else:
            res+=1
            arr[res] = arr[i]
    return arr[:res+1]

def meetingMaximumGuest(arr,dep):
    n = len(arr)
    arr.sort()
    dep.sort()
    curr,maxG=1,1
    i,j=1,0
    startTime = arr[0]
    endTime = dep[0]
    while i < n and j < n:
        if arr[i] <= dep[j]:
            curr +=1
            i+=1
        else:
            curr -=1
            j+=1
        if maxG < curr:
            startTime = arr[i-1]
            endTime = dep[j]
            maxG = curr
    print('from : '+str(startTime)+' to : '+str(endTime))
    return maxG

# print('kth smallest element : ',kthSmallestElement([2,4,5,1,3,8],7))
# print('chocolate dist. problem : ',chocolateDistributionProblem([2,4,5,1,7,8],3))
# print('seggerate negetives : ',segregateNegetives([2,-2,3,-4,5,6,-7,8,-1]))
# print('sort 012 : ',sort012([0,2,0,1,0,2,2,0,0,1,1,0]))
# print('min diff: ',minDifference([1,4,3,5,9,23,6]))
# print('overlapping diff : ',overlappingIntervals([[7,9],[6,10],[4,5],[1,3],[2,4]]))
# print('overlapping diff : ',mergeOverlappingIntervals([[5,10],[3,5],[18,30],[2,7]]))
print('max guiest at a time : ', meetingMaximumGuest([800,700,600,500],[840,820,830,530]))