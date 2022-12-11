def maxLengthOfEvenOdd(arr):
    n = len(arr)
    res = 1
    curr = 1
    isEven = arr[0] %2 == 0
    isEven = not isEven
    for i in range(1,n):
        check = (arr[i] %2 == 0 ) if isEven else (arr[i] %2 !=0)
        if check:
            curr+=1
            res = max(res,curr)
            isEven = not isEven
        else:
            curr = 1
        if i == n-1:
            res = max(res,curr)
    return res

#  idea: 1. find the max simple array subarray
#        2. find the min from simple array subarray and subtract from the total array sum to get max subarray sum in circular array 
#        3. return the max
# helper 

def maxSumSubarray(arr):
    n = len(arr)
    res = arr[0]
    curr = arr[0]
    for i in range(1,n):
        curr = max(curr+arr[i],arr[i])
        res = max(res,curr)
    return res


def maxCircularSubarraySum(arr):
    n = len(arr)
    maxRes = arr[0]
    circularRes = arr[0]
    total = 0

    # finding max
    maxRes = maxSumSubarray(arr)

    # if max res is neg: mean every items are -neg
    if maxRes < 0:
        return maxRes

    # finding total and invert the array with -neg and adding it to total gives the circular max 
    for i in range(n):
        total+=arr[i]
        arr[i] = -arr[i]
    circularRes = total + maxSumSubarray(arr)

    return max(maxRes,circularRes)

def majorityElement(arr):
    majEle = 0
    maxEle = 0
    hashMap = {}
    n = len(arr)
    for i in range(n):
        if arr[i] not in hashMap:
            hashMap[arr[i]] = 1
        else:
            hashMap[arr[i]] +=1
    for k,v in hashMap.items():
        if v > maxEle:
            maxEle = v
            majEle = k
    print('majEle : ',majEle)
    print('quantity : ',maxEle)
    return arr.index(majEle) if maxEle > n//2 else -1

# efficient with O(1) aux space
# logic behind is: 
#                   first loop find the possible majority element, if the count of the curr majority is not more then n//2
#                   then none of the element has more count then n//2
def majorityElementEff(arr):
    n = len(arr)
    res,count = 0,1
    for i in range(1,n):
        if arr[i] == arr[res]:
            count +=1
        else:
            count -=1
        if count == 0:
            res = i
            count =1
    count = 0
    print('current maj : ',arr[res])
    for i in range(n):
        if arr[i] == arr[res]:
            count +=1
    if count > n//2:
        return arr[res]
    else: 
        return -1

def minConsicutiveFlip(arr):
    zeros = 0
    ones = 0
    n = len(arr)
    prev = arr[0]
    for i in range(n):
        if arr[i] != prev:
            if arr[i] == 0:
                ones +=1
                prev = 0
                # print('index : ',i)
            else:
                zeros +=1
                prev = 1
                # print('pin : ',i)
        if i == n-1:
            if arr[i] == 0:
                zeros +=1
            else:
                ones +=1
    minCount = min(zeros,ones)
    for i in range(n):
        if arr[i] ==0 and minCount == zeros:
            print('flip at: ',i)
            arr[i] = 1
        elif arr[i] ==1 and minCount == ones:
            arr[i] = 0
            print('flip at: ',i)
    print('zeros : ',zeros)
    print('ones : ',ones)
    print('array: ',arr)


# more efficient
# second group will be equal or less then the first group, so we flip only second group element whatever it is 0 or 1
def minConsicutiveFlipEff(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i-1] != arr[i]:
            # arr[i] is not equal to first element
            if arr[i] != arr[0]:
                print('from '+str(i)+' to ',end=' ')
            else:
                print('to ',i-1)
    if arr[n-1] != arr[0]:
        print(n-1)
    print('arr : ',arr)
            

# print('max even odd subsequence: ',maxLengthOfEvenOdd([7,10,13]) )
# print('max circular subarray: ',maxCircularSubarraySum([8,-4,3,-5,4]))
# print('maj element is: ',majorityElementEff([8,8,8,1,2,3,8,5]))

# print('min consicutive flips: ',minConsicutiveFlip([1,1,0,0,0,1,0,1,1,0,1]))
print('min consicutive flips: ',minConsicutiveFlipEff([0,1,0,0,0,1,0,1,1,0,1]))