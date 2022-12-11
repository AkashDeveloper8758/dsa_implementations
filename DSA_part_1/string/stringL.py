from math import factorial

def stringIsRotationOfOther(string,other):
    n = len(string)
    m = len(other)
    if m!= n:
        return False
    for i in range(n):
        string = string[1:]+string[0]
        if string == other:
            return True
    return False

def stringRotationDirectMethod(s:str,o:str):
    if len(s) != len(o):
        return False
    # if we concatinate s with o then if o is persent in s the new string will contain o
    return (s+o).find(o) != -1

# time = O(n^2)
def anagramSearch(string,word):
    n = len(string)
    m = len(word)
    j = 0
    for i in range(n-m+1):
        if string[i] in word:
            j+=1
            while j<m:
                if string[i+j] not in word:
                    break
                j+=1
            if j==m:
                return True
    return False

# create two char arr, and use window sliding to match both array
# time : O(n*char)
def anagramSearchEff(string,patt):
    charL = 256
    n = len(string)
    m = len(patt)
    ct = [0 for _ in range(charL)]
    cp = [0 for _ in range(charL)]
    for i in range(m):
        ct[ord(string[i])] +=1
        cp[ord(patt[i])]+=1
    for i in range(m,n):
        if ct == cp:
            return True
        ct[ord(string[i])]+=1
        ct[ord(string[i-m])] -=1
    return False

# idea: 
# 1. find lexicography smaller elements left to the index, and calculate fact, 
# 2. multiply with the available index with factorial
# 3. add then all + 1
def lexicographicRankOfString(string):
    n = len(string)
    fact = factorial(n)
    char = 256
    charArr = [0 for i in range(char)]
    for i in range(n):
        charArr[ord(string[i])]+=1
    res = 1
    # creating cumulative sum to calculate smaller characters then 
    for i in range(1,char):
        charArr[i] += charArr[i-1]
    for i in range(n):
        fact = fact//(n-i)
        res += fact*charArr[ord(string[i])-1]

        # reduce the count by 1 to every right element from the current.
        # because we have already count current element
        for j in range(ord(string[i]),char):
            charArr[j] -=1
    return res

# brut force n^2
def longestSubstringWithDistinctChar(string):
    n = len(string)
    res = 0
    for i in range(n):
        # temp arr to store visited strings
        visited = [False for i in range(256)]
        for j in range(i,n):
            if visited[ord(string[j])]:
                break
            visited[ord(string[j])] = True
            res = max(res,j-i+1)
    return res

# logic is simple: 
# variable j will increase to the point where we are finding duplicates 
# if we found 2 continous "aa" then second a will change the j position to 
# its own index, which maintain max distinct element count by subtracting
# j from i

# time complexity: O(n)
def longestSubstringDistinctEff(string):
    n = len(string)
    res = 0
    prevStr = [-1 for _ in range(256)]
    j = 0
    for i in range(1,n):
        # prev index of an array, to calcualte starting index
        j = max(j,prevStr[ord(string[i])]+1)
        maxEnd= i-j+1
        res = max(res,maxEnd)
        prevStr[ord(string[i])] = i

    return res

# print('is rotated :',stringRotationDirectMethod('abcd','bcda'))
# print('anagram search :',anagramSearch('geeksforgeeks','frog'))
# print('anagram search :',anagramSearchEff('geeksforgeeks','frogi'))
# print('lexicographic rank  :',lexicographicRankOfString('dcza'))
# print('longest substing with distinct : ',longestSubstringWithDistinctChar('abcaabcde'))
print('longest substing with distinct : ',longestSubstringDistinctEff('abcadbd'))


# akash
# kasha