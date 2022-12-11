def windowSlidingProblem(arr,k):
    n = len(arr)
    if k > n:
        return -1
    preSum,maxSum = 0,0
    for i in range(n):
        if i > k-1:
            maxSum = max(maxSum,preSum)
            preSum = preSum - arr[i-k] + arr[i]
        else:
            preSum += arr[i]
    maxSum = max(maxSum,preSum)
    print("max sum is: ",maxSum)

def ifSubarrayContainSum(arr,sumValue):
    n = len(arr)
    currSum =0
    prefix = 0
    postfix= 0
    while currSum > sumValue or postfix < n:
        # print('postfix',postfix)
        # print('prefix',prefix)
        print('sum is: ',currSum)
        if currSum < sumValue:
            currSum += arr[postfix]
            postfix +=1
        elif currSum > sumValue:
            currSum -= arr[prefix]
            prefix +=1
        if currSum == sumValue:
            print('from index : '+str(prefix)+' to ',postfix-1)
            return True

    return currSum == sumValue

def nBonnachiNumbers(n,m):
    arr = []
    currSum = 1
    for _ in range(n-1):
        arr.append(0)
        print('0')
    arr.append(1)
    arr.append(1)
    print('1')
    print('1')
    for i in range(m-n):
        currSum = currSum*2 - arr[i]
        arr.append(currSum)
        print(currSum)
    return arr

def prefixSum(arr,queries):
    n = len(arr)
    prefixSum = []
    sumV = 0
    for i in range(n):
        sumV += arr[i]
        prefixSum.append(sumV)
    for query in queries:
        l = query[0]
        r = query[1]
        leftSub = 0
        if l> 0:
            leftSub = prefixSum[l-1]

        querySum = prefixSum[r] -leftSub
        print('query sum : ',querySum)

def isContainEquilibriumPoint(arr):
    sumV = 0
    n = len(arr)
    for i in range(n):
        sumV += arr[i]
    l_sum = 0
    for i in range(n):
        if l_sum == sumV - arr[i] - l_sum:
            return arr[i]
        l_sum +=arr[i]
        print('sum v : ',sumV)
    return False



arr = [135,101,170,125,79,159,163,65,106,146,82,28,162,92,196,143,28,37,192,5,103,154,93,183,22,117,119,96,48,127,172,139,70,113,68,100,36,95,104,12,123,134]
# windowSlidingProblem([1,8,30,-5,20,7],3)
print("is contain sum: ",ifSubarrayContainSum(arr,468))
# print('n bonnachi: ',nBonnachiNumbers(4,10))
# prefixSum([2,-2,4],[])
# print('contian equilibrium at: ',isContainEquilibriumPoint([3,5,8,4,4]))