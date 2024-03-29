def searchInSortedRotatedArray(A : list, l : int, h : int, key : int):
    # Complete this function
    h = len(A)-1
    l = 0
    while l<=h:
        m = (l+h)//2
        if A[m] ==key:
            return m
        # if array is sorted untill mid
        if A[l] < A[m]:
            if A[l] <= key <= A[m]:
                h = m-1
            else:
                l = m+1
        else:
            # from rotated array
            if A[m] <= key <=  A[h]:
                l = m+1
            else:
                h = m-1
    return -1
# A[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}

#  time complexity : O(n)
def findingPeakEle(arr):
    n = len(arr)
    if n ==1:
        return arr[0]
    if arr[1] < arr[0]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    for i in range(1,n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]
    return -1


# time complexity : O(logn)
def efficientPeakFinding(arr):
    n = len(arr)
    if n ==1:
        return arr[0]
    if arr[1] < arr[0]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]

    high,low = n-1,0
    while high >= low:
        mid = (high+low)//2
        if (mid == 0 or arr[mid] >= arr[mid-1]) and ( mid == n-1 or arr[mid] >= arr[mid+1] ):
            return arr[mid]
        if arr[mid] <= arr[mid+1]:
            low = mid+1
        else:
            high = mid-1

    return -1

# with two pointer approach O(n)
def pairSumInSortedArray(arr,sumv):
    n = len(arr)
    start,end = 0,n-1
    while start < end:
        newSum = arr[start]+arr[end]
        if newSum == sumv:
            return True
        else:
            if newSum > sumv:
                end-=1
            else:
                start+=1
    return False

# O(n2)
def findingTripletSum(arr,sum):
    n = len(arr)
    for i in range(n):
        if pairSumInSortedArray(arr[i+1:],sum-arr[i]):
            return True
    return -1

# def pairWithSum(arr,sumv):
#     n = len(arr)
#     for i in range(n):




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

arr = [564,567,571,574,578,583,584,588,591,594,596,604,611,619,622,625,632,637,639,640,642,644,650,652,658,660,663,666,667,668,673,674,678,680,683,686,694,699,709,716,717,719,721,723,727,730,736,761,762,763,775,777,778,784,788,791,794,798,806,814,815,816,821,824,826,828,829,834,840,845,851,852,853,854,857,858,860,861,869,872,876,878,887,889,891,893,899,903,911,913,920,929,931,932,933,934,949,950,953,955,956,957,958,961,963,968,970,971,973,977,978,981,982,983,986,988,990,991,992,998,1000,1,3,9,11,12,16,17,18,20,22,30,31,33,38,40,43,51,53,54,58,63,68,70,72,76,82,84,85,87,88,98,100,101,105,110,113,115,117,123,126,127,128,132,134,135,137,141,142,148,150,153,154,155,156,157,160,161,171,172,173,174,175,180,182,184,185,190,193,196,198,199,200,208,212,217,218,224,225,226,232,239,246,255,264,265,267,270,279,281,282,284,286,287,290,296,297,298,299,301,305,306,309,310,311,314,315,324,326,327,335,338,339,342,344,351,352,353,355,356,359,361,362,365,369,377,378,379,383,384,394,399,400,405,413,416,419,422,425,427,429,434,438,440,446,466,469,470,473,475,476,477,483,484,486,488,490,491,492,495,497,507,512,518,526,529,533,536,538,539,540,542,549,552,553,556,560]
print('searching function: ',searchInSortedRotatedArray(arr,281))
# print('peak element function: ',findingPeakEle([4,4,1,2,3,3,4,5,8]))
# print('peak element function: ',efficientPeakFinding([5,20,40,30,20,50,40]))
# print('pair sum in sorted array: ',findingTripletSum([2,5,8,12,30],43))