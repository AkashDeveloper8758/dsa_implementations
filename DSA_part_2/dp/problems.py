import math

# n^2
def findLis(arr:list):
    n = len(arr)
    lis = [1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i],lis[j]+1)
    res = 0
    for j in range(n):
        res = max(res,lis[j])
    print('lis arr : ',lis)
    print('lis : ',res)

# nlogn
def ceilIdx(tail:list,s,e,value):
    while s < e:
        m = s + (e-s)//2
        if tail[m] >= value:
            e = m
        else:
            s = m+1
    return e


def findLisEff(arr):
    n = len(arr)
    # initialize tail first with array first element
    tail = [arr[0]]

    for i in range(n):
        if arr[i] > tail[-1]:
            tail.append(arr[i])
        else:
            idx = ceilIdx(tail,0,len(tail)-1,arr[i])
            tail[idx] = arr[i]
    return len(tail)

def maxCustRecursive(n,a,b,c):
    if n < 0:
        return -1
    if n==0:
        return 0

    res = max(  
        maxCustRecursive(n-a,a,b,c),
        maxCustRecursive(n-b,a,b,c),
        maxCustRecursive(n-c,a,b,c),)
    if res == -1:
        return res
    else:
        return res+1

def maxCutsWithDP(n,a,b,c):
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0

    for i in range(1,n+1):
        if i-a >=0:
            dp[i] = max(dp[i-a],dp[i])
        if i-b >=0:
            dp[i] = max(dp[i-b],dp[i])
        if i-c >=0:
            dp[i] = max(dp[i-c],dp[i])
        if dp[i] != -1:
            dp[i] +=1
    return dp[n]

def minCoinToMakeaValue(coins,value,n):

    if value == 0:
        return 0
    res = math.inf
    for i in range(n):
        if value-coins[i] > 0:
            sub_result = minCoinToMakeaValue(coins,value-coins[i],n)
            if sub_result != math.inf:
                res = min(res,sub_result+1)
    return res

def minCoinToMakeValueUsingDP(coins,value,n):
    valueDP = [math.inf for _ in range(value+1)]
    valueDP[0] = 0
    for i in range(1,value+1):
        for j in range(n):
            if coins[j] <= i:
                subResult = valueDP[i-coins[j]]
                if subResult != -1:
                    valueDP[i] = min(valueDP[i],subResult + 1)
    return valueDP[value]
# 7 8
# 1 2 3 4 7 8 9 11
# ------------ min jump to reach end ------------

def minJumpToReachEnd(arr,n):
    if n==1:
        return 0 
    res = math.inf
    for i in range(n-1):
        if i + arr[i] >= n-1:
            sub_result = minJumpToReachEnd(arr,i+1)
            if sub_result != math.inf:
                res = min(sub_result+1,res)
    return res

def minJumpWithDP(arr,n):
    valueDP = [math.inf for _ in range(n)]
    valueDP[0] = 0
    for i in range(n):
        for j in range(i):
            if arr[j] + j >= i:
                if arr[j] != math.inf:
                    valueDP[i] = min(valueDP[i],valueDP[j]+1)
    return valueDP[n-1]

# ----------------------- knapsack ----------
def binaryKnapsack(weight,value,n,w):
    if n==0 or w<=0:
        return 0

    if weight[n-1] > w:
        return binaryKnapsack(weight,value,n-1,w)
    # either include or not
    res = max(binaryKnapsack(weight,value,n-1,w),
          value[n-1]+ binaryKnapsack(weight,value,n-1,w-weight[n-1]))
    return res

def binaryKnapsackDP(weight,value,n,w):
    dp = [[None for _ in range(w+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(w+1):
        dp[0][i] = 0
    for i in range(1,n+1):
        for j in range(1,w+1):
            if weight[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], value[i-1] + dp[i-1][j-weight[i-1]] )
    return dp[n][w]



sa = [44,42,38,21,15,22,13,27]


arr= [3,4,2,8,10,5,1]
# findLis(arr)
# print('lis value eff : ',findLisEff(arr))
# print('max cut : dp',maxCutsWithDP(100,2,3,5))
# print('max cut recursive: ',maxCustRecursive(10,2,3,5))

coins = [1,2,3,4,7,8,9,11]
# print('min coin to make a value : ',minCoinToMakeaValue(coins,20,len(coins)))
# print('min coin to make a value : dp ',minCoinToMakeValueUsingDP(coins,7,len(coins)))

# print('min jump to reach end : ',minJumpToReachEnd(arr,len(arr)))
# print('min jump to reach end DP: ',minJumpWithDP(arr,len(arr)))

# weights = [5,4,6,3,7,9,8,1]
# value = [10,40,30,50,20,60,45,25]
# print('max value of b-knapsack dp : ',binaryKnapsackDP(weights,value,len(weights),10))
# print('max value of b-knapsack : ',binaryKnapsack(weights,value,len(weights),10))



