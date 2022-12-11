# self done
def longestCommonSpanWithSameSumInBinary(arr1,arr2):
    # make new array by subtracting arr2 from arr1
    n = len(arr1)
    arr = []
    for i in range(n):
        arr.append(arr2[i]-arr1[i])
    # find largest subarray with zero sum
    res = 0
    currSum = 0
    hashMap = {}
    for i in range(n):
        currSum += arr[i]
        if currSum == 0:
            res = i
        if currSum in hashMap:
            res = max(res,i-hashMap[currSum])
        else:
            hashMap[currSum] = i
    return res

# there is only 2n lookup : time compx: O(n)
def longestConsicutiveSubsequences(arr):
    hashSet = set(arr)
    n = len(arr)
    res = 0
    for i in range(n):
        if not (arr[i]-1) in hashSet:
            count = 1
            while arr[i]+count in hashSet:
                count+=1
            res = max(res,count)
    return res

# my solution
def countDistinctElementInWindow(arr,k):
    res = 0
    n = len(arr)
    hashMap = {}
    hashSet = set()
    for i in range(n):
        hashSet.add(arr[i])
        hashMap[i] = len(hashSet)
    for i in range(n-k+1):
        diff =hashMap[i+k-1] - hashMap[i] + 1
        res = max(res,diff)
    return res
     
# better solution : time: O(n) and space: O(k)
def countDistinctElementInWindowEff(arr,k):
    res = 0
    n = len(arr)
    hashMap = {i:1 for i in arr}
    for i in range(k):
        hashMap[arr[i]] +=1
    for i in range(k,n):
        if arr[i] in hashMap:
            if hashMap[arr[i]] ==1:
                del hashMap[arr[i]]
            else:
                hashMap[arr[i]]-=1
        else:
            hashMap[arr[i]] = 1
        res = max(res,len(hashMap))
    return res

def moreThanNbyKoccurences(arr,k):
    hashmap = {i:1 for i in arr}
    n = len(arr)
    check = n//k
    for i in arr:
        hashmap[i]+=1
        if hashmap[i] > check:
            print([i,hashmap[i]],end=' ')
    print()

# extention of moore algo, which state max occurance of element, less then k
# is helpfull if n is very large and k is small
def moreThanNbyKoccurencesEff(arr,k):
    hashmap = {}
    n = len(arr)
    check = n//k
    for i in range(n):
        if arr[i] in hashmap:
            hashmap[arr[i]] +=1
        # we are keeping the size of hashmap less then k
        elif len(hashmap) < k:
            hashmap[arr[i]] = 1
        else:
            hashmap = {k:v-1 for k,v in hashmap.items()} 
            hashmap = {k:v for k,v in hashmap.items() if hashmap[k] != 0}
            hashmap[arr[i]] = 1
            print('after: ',hashmap)
    print('hash map : ',hashmap)
    for k,v in hashmap.items():
        if v> check:
            print(k,end=' ')

                
    
    
            

# means it is not the first element of subset, no need to process

# print('longest common span: ',longestCommonSpanWithSameSumInBinary(
#     [0,0,1,0],[1,1,1,1]))

# print('longest subsequence : ',longestConsicutiveSubsequences([1,3,9,2,8,2]))
# print('distinct element with k : ',countDistinctElementInWindowEff([10,20,10,10,30,40],4))
# print('more then n/k occurances :',moreThanNbyKoccurences([10,10,40,20,30,60,30,10,50,30],3))

print('more then n/k occurances eff:',moreThanNbyKoccurencesEff([30,10,20,20,20,10,40,40,40,30,30],4)) 
