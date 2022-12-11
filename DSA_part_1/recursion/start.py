def tailFact(num,k):
    if num == 0 or num == 1:
        return k
    return tailFact(num-1,k*num)

def nthFibonacci(num):
    if num ==0 or num ==1:
        return num
    return nthFibonacci(num -1) + nthFibonacci(num-2)

def isPalindrome(string,start,end):
    if start >= end:
        return True
    return string[start] == string[end] and isPalindrome(string,start+1,end-1)

def sumOfDigits(digit):
    if digit == 0:
        return 0
    return digit % 10 + sumOfDigits(digit//10)

def ropeCuttingProblem(a,b,c,rope):
    if rope == 0:
        return 0
    if rope < 0:
        return -1
    res = max(ropeCuttingProblem(a,b,c,rope-a),ropeCuttingProblem(a,b,c,rope-b))
    res = max(res,ropeCuttingProblem(a,b,c,rope-c))
    if res == -1:
        return -1
    return res +1

def subsetOfString(string,curr,index):
    if index == len(string):
        print(curr,end=' ')
        return
    subsetOfString(string,curr,index +1)
    subsetOfString(string,curr+string[index],index +1)

def towerOfHanoi(n,a,b,c):
    if n==0:
        return 0
    step1 = towerOfHanoi(n-1,a,c,b) + 1
    # print('move disk ['+str(n)+'] from -> '+str(a)+' to '+str(c))
    step2 = towerOfHanoi(n-1,b,a,c)
    return step1 + step2


def josephusKthKill(n,k):
    if n==1:
        return 0
    return (josephusKthKill(n-1,k) + k) %n

def subsetSumProblem(array,sum,i):
    if i==0:
        return 1 if sum == 0 else 1
    return subsetSumProblem(array,sum,i-1) + subsetSumProblem(array,sum - array[i],i-1)

def swapString(string,s,e):
    lst = list(string)
    lst[s],lst[e] = lst[e],lst[s]
    return ''.join(lst)

def permutationOfString(string,index):
    if index == len(string) -1:
        print(string,end=' ')
        return
    i = index
    while i < len(string):
        # swaping current with index  6
        string = swapString(string,index,i)    
        # print('index : ',string)
        # break
        permutationOfString(string,index+1)
        string = swapString(string,index,i)
        i+=1
        # string = swapString(string,i,index)


        

# print('swap: ',swapString('maurya',1,0))

# print('tailValue: ',tailFact(100,1))
# print('fibValue: ',nthFibonacci(10))
# print('is palindrome: ',isPalindrome('nitin',0,4))
# print('sum of digits: ',sumOfDigits(543))
# print('rope cutting problem: ',ropeCuttingProblem(2,2,2,9))
# subsetOfString('abc','',0)
# print('total steps: ',towerOfHanoi(4,'a','b','c'))
# print('joseph number: ',josephusKthKill(15,18))
# print('subset sum problem: ',subsetSumProblem([10,20,15],25,2))

permutationOfString('abcd',0)

