import math

def optimalGameStrategy(arr,i,j):

    if i+1 == j:
        return max(arr[i],arr[j])

    res = max( arr[i] + min( optimalGameStrategy(arr,i+2,j),
                            optimalGameStrategy(arr,i+1,j-1) ),
                arr[j] + min(optimalGameStrategy(arr,i+1,j-1),
                            optimalGameStrategy(arr,i,j-2)))
    return res

def optimalGameStrategyDP(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    # fill diagonal data 
    for i in range(n-1):
        dp[i][i+1] = max(arr[i+1],arr[i])
    for gap in range(3,n,2):
        i=0
        while i+gap < n:
            j = i+gap
            dp[i][j] = max(
                 arr[i] + min(dp[i+2][j],dp[i+1][j-1]),
                 arr[j] + min(dp[i+1][j-1],dp[i][j-2]))
            i+=1
    return dp[0][n-1]

# --------- egg dropping problem ------------
def eggDroppingProblem(f,e):
    dp = [[None for _ in range(e+1)] for _ in range(f+1)]
    for i in range(e+1):
        dp[0][i] = 0
        dp[1][i] = 1

    for i in range(1,f+1):
        dp[i][1] = i
    for i in range(2,f+1):
        for j in range(2,e+1):
            dp[i][j] = math.inf
            for x in range(1,i+1):
                res = max(dp[x-1][j-1],dp[i-x][j])+1
                dp[i][j] = min(dp[i][j],res)

    return dp[f][e]

def countBStWithDP(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-j-1]
    return dp[n]

def maxSumWithNoConsicutive(arr,n):
    if n==1:
        return arr[0]
    if n == 2:
        return max(arr[0],arr[1])
    # include or not include
    return max( maxSumWithNoConsicutive(arr,n-1) , maxSumWithNoConsicutive(arr,n-2) + arr[n-1] ) 

def maxSumWithDP(arr,n):
    dp = [0 for _ in range(n+1)]
    dp[1] = arr[0]
    dp[2] = max(arr[0],arr[1])
    for i in range(3,n+1):
        dp[i] = max(dp[i-1],dp[i-2]+arr[i-1])
    return dp[n]

# -------------- matrix chain multiplication ------------------
def mChain(arr,i,j):
    # if only two items left then there is only one matrix, so 0 mutiplications
    if i+1 == j:
        return 0
    res = math.inf
    for k in range(i+1,j):
        res = min(res, mChain(arr,i,k) + mChain(arr,k,j) + arr[i]*arr[k]*arr[j]  )
    return res

def mChainDP(arr):
    n = len(arr)
    dp = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = 0
    for gap in range(2,n):
        for i in range(n-gap):
            j = gap+i
            dp[i][j] = math.inf
            for k in range(i+1,j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[i]*arr[j]*arr[k])
    return dp[0][n-1]

# ---------- palindrome partationing -------
def isPalindrome(string,i,j):
    while i<j:
        if string[i] != string[j]:
            return False
        i+=1
        j-=1
    return True

def palindromeMinCuts(string,i,j):
    if isPalindrome(string,i,j):
        return 0
    res = math.inf
    for k in range(i,j):
       res = min(res, palindromeMinCuts(string,i,k) + palindromeMinCuts(string,k+1,j) + 1 ) 
    return res

# n^4
def palindromeMinCutsDP(string):
    n = len(string)
    dp = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    # we start iterating gaps from 1 to n-1
    for gap in range(1,n):
        for i in range(n-gap):
            j = i+gap
            dp[i][j] = math.inf
            if isPalindrome(string,i,j):
                dp[i][j] = 0
            else:
                for k in range(i,j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1 )
    return dp[0][n-1]

# n^3
def palindromeMinCutsDP_efficient( string):
    n = len(string)
    dp = [[math.inf for _ in range(n)]for _ in range(n)]
    pali_dp = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
        pali_dp[i][i] = True
    for g in range(1,n):
        for i in range(n-g):
            j = i+g
            # for two string, we can directly check
            if j-i < 2:
                pali_dp[i][j] = string[i]==string[j]
            else:
                pali_dp[i][j] = string[i]==string[j] and pali_dp[i+1][j-1]
                
            if pali_dp[i][j]:
                dp[i][j] =0
            else:
                for k in range(i,j):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+1)
    # print(dp[0])
    return dp[0][n-1]

# n^2
def palindromicPartition_mostEfficient(string):
    n = len(string)
    # dp = [[math.inf for _ in range(n)]for _ in range(n)]
    c = [math.inf for _ in range(n)]
    pali_dp = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        # dp[i][i] = 0
        pali_dp[i][i] = True
    for g in range(1,n):
        for i in range(n-g):
            j = i+g
            # for two string, we can directly check
            if j-i < 2:
                pali_dp[i][j] = string[i]==string[j]
            else:
                pali_dp[i][j] = string[i]==string[j] and pali_dp[i+1][j-1]
                
    for i in range(n):
        if pali_dp[0][i]:
            c[i] = 0
        else:
            for j in range(i):
                if pali_dp[j+1][i]:
                    c[i] = min(c[i], c[j]+1 )
    return c[n-1]
                

# -------------- min pages -------------------
def findSum(arr,i,j):
    res = 0
    for k in range(i,j+1):
        res += arr[k]
    return res

# n = no of books
# k = no of childrens
def minPages(arr,n,k):

    if k == 1:
        return findSum(arr,0,n-1)
    if n == 1:
        return arr[0]
    
    res = math.inf
    for i in range(n):
        res = min(res , max( minPages(arr,i,k-1) , findSum(arr,i,n-1) ))
    return res

def minPagesDP(arr,n,k): 
    dp = [[math.inf for _ in range(n+1)] for _ in range(k+1)]
    currSum = 0
    for i in range(1,n+1):
        currSum+= arr[i-1]
        dp[1][i] = currSum

    for i in range(1,k+1):
        dp[i][1] = arr[0]

    for i in range(2,k+1):
        for j in range(2,n+1):
            for p in range(1,j):
                dp[i][j] = min(dp[i][j], max(dp[i-1][p], findSum(arr,p,j-1)))

    return dp[k][n]

arr = [10,30,5,60]
# print('optimal game strategy point : ',optimalGameStrategy(arr,0,len(arr)-1))
# print('optimal game strategy point dp: ',optimalGameStrategyDP(arr))

# print('egg drop problem : ',eggDroppingProblem(10,2))

# print('count bst : ',countBStWithDP(4))

# print('max non consicutive sum : ',maxSumWithNoConsicutive(arr,len(arr)))
# print('max non consicutive sum dp: ',maxSumWithDP(arr,len(arr)))

# print('m chain result dp: ',mChainDP(arr))
# print('m chain result : ',mChain(arr,0,len(arr)-1))

string = 'skjdflaaasdfffddaabbb '
# print('palindrome min cuts : ',palindromeMinCuts(string,0,len(string)-1))
print('palindrome min cuts : dp ',palindromeMinCutsDP(string))

# print('min pages : ',minPages(arr,len(arr),2))
# print('min pages dp : ',minPagesDP(arr,len(arr),2))
