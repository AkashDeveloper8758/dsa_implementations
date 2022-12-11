
memo = [-1 for _ in range(1000)]
# memoization 
def fib_dp(n):
    if memo[n]==-1:
        res = -1
        if n==0 or n==1:
            res= n
        else:
            res = fib_dp(n-1)+fib_dp(n-2)
        memo[n] = res
    return memo[n]

# tabulation
def fib_tabulation(n):
    f = [None]*(n+1)
    f[0] = 0
    f[1] =1
    for i in range(2,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

# lcs using dp - memoization
memo_lcs = [[]]
isMemoUpdated = False
def longestCommonSubsequence(s1,s2,m,n):
    global memo_lcs,isMemoUpdated
    if not isMemoUpdated:
        memo_lcs = [[-1]*(n+1)]*(m+1)
        isMemoUpdated = True
    # if memo is available
    if memo_lcs[m][n] != -1:
        return memo_lcs[m][n]
    if m == 0 or n == 0:
        memo_lcs[m][n]=0
    else:
        if s1[m-1] == s2[n-1]:
            memo_lcs[m][n] = 1+longestCommonSubsequence(s1,s2,m-1,n-1)
        else:
            memo_lcs[m][n] = max(longestCommonSubsequence(s1,s2,m-1,n),
                                    longestCommonSubsequence(s1,s2,m,n-1))
    return memo_lcs[m][n]

# lcs using dp - tabulation
def lcs_using_tabulation(s1,s2,m,n):
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    # first row and column is always 0 as for empty string value is zero
    # initialization for dp table 
    # taking m+1 as total size start from 0 len string to total len
    for k in range(m+1):
        dp[k][0] = 0
    for k in range(n+1):
        dp[0][k] = 0
    # start from 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i][j-1],dp[i-1][j])
    return dp[m][n]

def coinChangeProblem(coins:list,n,sumV):
    # if sum is 0 then ther will be one way to collect coin is to coll. no coin
    if sumV == 0:
        return 1
    if n == 0:
        return 0
    res = coinChangeProblem(coins,n-1,sumV)
    if coins[n-1] <=sumV:
        res+= coinChangeProblem(coins,n,sumV - coins[n-1])
    return res

def coinChangeProblemWithDP(coins:list,n,sumv):
    dp = [[None for _ in range(n+1)] for _ in range(sumv+1)]
    for i in range(n+1):
        dp[0][i] = 1
    for i in range(1,sumv+1):
        dp[i][0] = 0

    for i in range(1,sumv+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i][j-1]
            if coins[j-1] <= i:
                dp[i][j] += dp[i-coins[j-1]][j]
    return dp[sumv][n]

# ------------- edit distance ----------
# min operations required to change s2 into s1 vice versa
def editDistanceProblem(s1,s2,m,n):

    if m==0:
        # if m == 0 then whole n is an inesrt
        return n
    if n==0:
        return m

    if s1[m-1] == s2[n-1]:
        return editDistanceProblem(s1,s2,m-1,n-1)
    # if strings are different then return the min of insert delete replace operation.
    return 1+ min( editDistanceProblem(s1,s2,m-1,n), #delete
                     editDistanceProblem(s1,s2,m,n-1), #insert
                      editDistanceProblem(s1,s2,m-1,n-1), #replace
                       )

def editDistanceProblemDP(s1,s2,m,n):
    dp = [[None for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for i in range(0,n+1):
        dp[0][i] = i

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min( dp[i-1][j-1],dp[i-1][j],dp[i][j-1] )
    return dp[m][n]



    


# print('fib dp : ',fib_dp(900))
# print('fib dp : ',fib_tabulation(900))
str1 = 'cat'
str2 = 'cut'
coins = [1,2,5,10]
# print('lcs is : ',longestCommonSubsequence(str1,str2,len(str1),len(str2)))
# print('lcs is : ',lcs_using_tabulation(str1,str2,len(str1),len(str2)))

# print('coins change value : ',coinChangeProblem(coins,len(coins),100))
# print('coins change value dp: ',coinChangeProblemWithDP(coins,len(coins),100))

# print('edit distance : ',editDistanceProblem(str1,str2,len(str1),len(str2)))
print('edit distance DP: ',editDistanceProblemDP(str1,str2,len(str1),len(str2)))