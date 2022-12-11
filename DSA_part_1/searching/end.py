import math

# time : O(n) auxS: O(n)
def repeatingEle(arr):
    n = len(arr)
    visited = [False]*n
    for i in range(n):
        if visited[arr[i]]:
            return arr[i]
        else:
            visited[arr[i]] = True
    return False

# time : O(n) auxS: O(1)
# phase1 : find the cycle
# phase 2 : find the first ele , we are adding 1 everywhere because the array contains 0

def repeatingEleEfficient(arr):
    fast = arr[0] + 1
    slow = arr[0] + 1

    # phase 1, it is do while implementation
    slow= arr[slow]+1
    fast = arr[arr[fast]+1] +1
    while fast != slow:
        slow= arr[slow]+1
        fast = arr[arr[fast]+1] +1

    # phase 2: move slow to begining and move both f and s at same speed
    slow = arr[0] + 1
    while slow != fast:
        slow = arr[slow] + 1
        fast = arr[fast] + 1
    return slow-1

def minPages(arr,n,k):
    if k == 1:
        return sumTo(arr,0,n-1)
    if n==1:
        return arr[0]
    res = math.inf
    for i in range(1,n):
        res = min(res,max(minPages(arr,i,k-1),sumTo(arr,i,n-1)))
    return res

# utility fun for minPages
def sumTo(arr,b,e):
    sumV = 0
    for i in range(b,e+1):
        sumV +=arr[i]
    return sumV

# utility fun for maxPagesEfficient
def isFeasible(arr,n,k,mid):
    req,sumV = 1,0
    for i in range(n):
        if sumV + arr[i] > mid:
            req+=1
            sumV = arr[i]
        else:
            sumV += arr[i]
    return req <=k
        

# efficient : n*Log(n)
def minPagesEfficient(arr,k):
    maxV,sumV = 0,0
    n = len(arr)
    for i in range(n):
        sumV +=arr[i]
        maxV = max(maxV,arr[i])
    
    low,high,res = maxV,sumV,0
    while low <= high:
        mid = (low + high)//2
        if isFeasible(arr,n,k,mid):
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res




print('repeated ele: ',repeatingEleEfficient([2,3,5,2,4,1]))    
# print('min pages : ',minPages([10,12,15,18,25,14,23],7,3))
# print('min pages eff: ',minPagesEfficient([10,12,15,18,25,14,23],3))