import math

def sortStringByLettersAndFrequency(string):
    str_arr= [0 for _ in range(26)]
    for i in string:
        str_arr[ord(i)-ord('a')]+=1
    # print(': ',str_arr)
    for i in range(26):
        if str_arr[i] > 0:
            print(chr(i+ord('a')),end=' ')
            print(': ',str_arr[i])

def palindromeCheck(string):
    n = len(string)
    for i in range(n//2):
        if string[i] != string[n-i-1]:
            return False
    return True
        
def checkStringSubsequence(string,subseq):
    n = len(string)
    m = len(subseq)
    j = 0
    for i in range(n):
        if string[i]==subseq[j]:
            j+=1
            if j == m:
                break
    return m== j

def anagramOfEachOther(str1,str2):
    new1 = str1
    new2 = list(str2)
    if len(str1) != len(str2):
        return False
    for i in range(len(new1)):
        if new1[i] in new2:
            index = new2.index(new1[i])
            new2[index] = ''
        else:
            return False
    return True

# use count arr to store count of occurances 
def anagramOfEachOtherEff(str1,str2):
    charLen = 256
    countArr = [0 for _ in range(charLen)]
    if len(str1) != len(str2):
        return False
    n = len(str1)
    for i in range(n):
        countArr[ord(str1[i])] +=1
        countArr[ord(str2[i])] -=1
    for i in range(charLen):
        if countArr[i] != 0:
            return False
    return True

def leftMostRepeatingChar(string):
    n = len(string)
    charLen = 256
    charArr = [-1 for _ in range(charLen)]
    res = math.inf
    for i in range(n):
        fi = charArr[ord(string[i])]
        if fi == -1:
            # put the index if it is -1
            charArr[ord(string[i])] = i
        else:
            # check for the min index if second element founc
            res = min(res,fi)
    return -1 if res == math.inf else res

def leftMostRepeatingCharMoreEff(string):
    n =len(string)
    charLen = 256
    visited = [False for _ in range(charLen)]
    res = -1
    for i in range(n-1,-1,-1):
        ind = ord(string[i])
        if visited[ind]:
            res = i
        else:
            visited[ind] = True
    return res

# eff solution with one traversal of string
def leftmostNonRepeatingChar(string):
    n = len(string)
    charLen = 256
    visited = [-1 for _ in range(charLen)]
    res = math.inf
    for i in range(n-1,-1,-1):
        index = ord(string[i])
        if visited[index] == -1:
            visited[index] = i
        else:
            visited[index] = -2

    for i in range(charLen):
        if visited[i] >=0:
            res = min(res,visited[i])
    return -1 if res == math.inf else res
        

# [-1,-1,-1,-1,34,-1,36,-1,-1,-1,-1,-1]

# sortStringByLettersAndFrequency('akash')
# print('is palindrome : ',palindromeCheck('nitin'))
# print('check str subsequence : ',checkStringSubsequence('akashmaurya','amhr'))
# print('anagram of each other: ',anagramOfEachOtherEff('aaacb','acbaa'))
# print('left most repeating char: ',leftMostRepeatingCharMoreEff('aabccbd'))
print('left most not repeating char: ',leftmostNonRepeatingChar('naabmccbd'))

