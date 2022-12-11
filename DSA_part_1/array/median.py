from cmath import inf
import math


def minMergeOperationToMakeArrayPalindrom(arr):
    n= len(arr)
    minV = 0
    i,j = 0,n-1
    while i<=j:
        if arr[i]==arr[j]:
            i+=1
            j-=1
        elif arr[i] > arr[j]:
            #  if j is smaller, then merge arr[j] + arr[j-1]
            arr[j-1] += arr[j]
            j-=1
            minV+=1
        else:
            arr[i+1]+=arr[i]
            i+=1
            minV+=1
    print('array : ',arr[i])
    return minV

def medianInSortedArrayOfSameLength(arr1,arr2):
    n = len(arr1)
    c = 0
    m1,m2= 0,0
    i,j = 0,0
    # travel n times in sorted ways, then we will reach median of 2n full merged array
    while c<n+1:
        c+=1
        # if arr1 reached n, means every elements of arr1 are smaller then arr2[0]
        if i==n:
            m1=m2
            m2 = arr2[0]
            break
        # vice versa
        if j==n:
            m1= m2
            m2 = arr1[0]
            break
        if arr1[i] <= arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i+=1
        else:
            m1 = m2
            m2 = arr2[j]
            j+=1
    return (m1+m2)//2

def getMedian(arr,n):
    if n%2==0:
        return (arr[int(n/2)]+arr[int(n/2)-1])/2
    else:
        return arr[int(n/2)]

def medianInSortedEff(arr1,arr2,n):
    if n==0:
        return -1
    if n==1:
        return (arr1[0] + arr2[0])//2
    if n==2:
        return  (max(arr1[0],arr2[0]) + min(arr1[1],arr2[1]))//2
    
    m1 = getMedian(arr1,n)
    m2 = getMedian(arr2,n)
    if m1 > m2:
         
        if n % 2 == 0:
            return medianInSortedEff(arr1[:int(n / 2) + 1],
                    arr2[int(n / 2) - 1:], int(n / 2) + 1)
        else:
            return medianInSortedEff(arr1[:int(n / 2) + 1],
                    arr2[int(n / 2):], int(n / 2) + 1)
     
    else:
        if n % 2 == 0:
            return medianInSortedEff(arr1[int(n / 2 - 1):],
                    arr2[:int(n / 2 + 1)], int(n / 2) + 1)
        else:
            return medianInSortedEff(arr1[int(n / 2):],
                    arr2[0:int(n / 2) + 1], int(n / 2) + 1)
    
def medianInDiffSizeArray(arr1,arr2):
    n1=len(arr1)
    n2 = len(arr2)
    if n1>n2:
        arr1,arr2 = arr2,arr1
        n1,n2=n2,n1
    print('arr1 ',arr1)
    print('arr2 ',arr2)
    
    low,high = 0,n1
    while low<=high:
        mid1 = (low+high)//2
        mid2 = (n1+n2+1)//2-mid1
        print('mid 2: ',mid2)
        # for arr1
        min1 = math.inf if mid1==n1 else arr1[mid1]
        max1 = -math.inf if mid1 == 0 else arr1[mid1-1]
        # for arr2
        min2 = math.inf if mid2==n2 else arr2[mid2]
        max2 = -math.inf if mid2 == 0 else arr2[mid2-1]

        if max2 <= min1 and max1 <= min2:
            if (n1+n2)%2==0:
                return (max(max1,max2) + min(min1,min2))/2
            else:
                return max(max1,max2)
        elif max1 > min2:
            # go left
            high = mid1-1
        else:
            low = mid1+1

ar1 = [1,3]
ar2 = [2]
print('median of diff size array: ',medianInDiffSizeArray(ar1,ar2))
# print('min merge : ',minMergeOperationToMakeArrayPalindrom([11,14,15,99]))
# print('median of sorted array : ',medianInSortedEff(ar1,ar2,len(ar1)))