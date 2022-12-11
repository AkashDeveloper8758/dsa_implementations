# hashing generally optimize searching with O(1) time complexity


from sys import prefix


def countDistinctElements(arr):
    dataMap = set(arr)
    return len(dataMap)

def countFrequency(arr):
    freqMap = {i:0 for i in arr}
    for i in arr:
        freqMap[i]+=1
    print(freqMap)

def intersectionOfUnsortedArr(arr1,arr2):
    freqMap = {i:1 for i in arr1}
    for i in arr2:
        if i in freqMap:
            freqMap[i]+=1
    count =0
    for i in freqMap.values():
        if i > 1:
            count+=1
    return count

def unionOfUnsortedArrays(arr1,arr2):
    mainSet = set(arr1)
    mainSet = mainSet.union(arr2)
    return len(mainSet)

def pairWithGivenSum(arr,sumV):
    hashSet = set()
    for i in arr:
        # checking if the difference is in the hashset yet or not
        if sumV - i in hashSet:
            return True
        else:
            hashSet.add(i)
    return False

# https://practice.geeksforgeeks.org/tracks/DSASP-Hashing/?batchId=154&tab=1
# hashing generally optimize searching with O(1) time complexity
# prefixSum and hashing

def subarrayWithZeroSum(arr):
    hashSumSet = set()
    currSum = 0
    for i in range(len(arr)):
        currSum += arr[i]
        # if current sum is already in set means, there is a subarray whose sum is 0
        if currSum in hashSumSet:  # O(1) operation in hashmap
            print('i is: ',arr[i])
            return True
        if currSum == 0:
            return True
        hashSumSet.add(currSum)
    return False

# similar to zero sum
def subarrayWithSum(arr,sumV):
    hasSet = set()
    currSum = 0
    for i in range(len(arr)):
        currSum += arr[i]
        if currSum -sumV in hasSet:
            return True
        else:
            hasSet.add(currSum)
        if currSum == sumV:
            return True
    return False

def longestSubarrayWithSum(arr,sumV):
    hasSet = {}
    currSum = 0
    res = 0
    for i in range(len(arr)):
        currSum += arr[i]

        if currSum == sumV:
            res = i+1
        if currSum -sumV in hasSet:
            res = max(res,i-hasSet[currSum-sumV])

        # check if currSum in not in hashSet, we want to keep the first index for longest subarray
        elif not currSum in hasSet:
            hasSet[currSum] = i
    return res

    # we will convert 0 to -1
    # then find max subarray sum with 0 sum, similar to previous questions
def longestSubarrayOfequalZeroAndOne(arr):
    currSum, res = 0,0
    newArr = arr[::]
    hashSet = {}
    n = len(arr)
    for i in range(n):
        if newArr[i] == 0:
            newArr[i] = -1
    
    for i in range(n):
        currSum+=newArr[i]
        if currSum == 0:
            res = i+1
        if currSum in hashSet:
            res = max(res,hashSet[currSum])
        else:
            hashSet[currSum] = i
    return res




# print('distinct elements : ',countDistinctElements([1,3,2,5,3,4,3,6,7,5,8,8,5]))
# print('count freq : ',countFrequency([1,4,2,3,5,4,3,6,4,7,3,5,2,8,5,8,5]))
# print('count intersection of arrs : ',intersectionOfUnsortedArr([1,2,3,4,5,6],[4,5,5,6,1,9,8,7]))
# print('union of arrs : ',unionOfUnsortedArrays([1,2,3,4,5,6,5,6,2],[4,5,5,6,1,1,4,5,9,8,7]))
# print('pair with given sum: ',pairWithGivenSum([8,3,4,2,5],6))
# print('subarray with zero sum: ',subarrayWithZeroSum([8,-8,3,2,1,3,4]))
# print('subarray with sum: ',subarrayWithSum([8,-8,3,2,1,3,4],6))
# print('subarray with longest sum: ',longestSubarrayWithSum([8,3,1,5,-6,6,2,2],4))
print('subarray with longest zero and one: ',
longestSubarrayOfequalZeroAndOne([0,0,1,1,1,1,0]))
