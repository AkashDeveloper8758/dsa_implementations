# time : big O(n*(m-n)), self
def naivePatternSearching(string,pattern):
    n = len(string)
    m = len(pattern)
    resArr = []
    for i in range(n-m+1):
        j = 0
        while j<m:
            if pattern[j] != string[i+j]:
                break
            j+=1
        if j ==m:
            resArr.append(i)
    return resArr

# improved naive for distinct elements.
# we increment i = i+j if matched, time : O(n)
def naivePatternSearchingForDistinct(string,pattern):
    n = len(string)
    m = len(pattern)
    resArr = []
    i=0
    while i <=n-m:
        print('i : ',i)
        j = 0
        while j<m:
            if pattern[j] != string[i+j]:
                break
            j+=1
        if j ==m:
            print('matched L ')
            resArr.append(i)
        if j==0:
            i+=1
        else:
            # if j is greater then 0, means some of the pattern is in the
            # string which may be complete pattern or not
            # so to save outer loop iteration we increase the i by j
            i+=j
    return resArr

# Rabin karp algorithm: work much better on average case then naive
# we use rolling hash function, remove previous hash and add next hash 
# to compute the current window hash

# it only go inside inner loop when hash match

def rabinKarpAlgorithm(string,pattern):
    d = 256 #hash multiplier
    q = 101 # nearest prime number

    n = len(string)
    m = len(pattern)
    pArr = []
    h = 1

    if m>n:
        return
    for i in range(m-1):
        h = (h*d)%q

# pattern hash
    pHash = 0
    currentHash = 0
    for i in range(m):
        pHash = (ord(pattern[i]) + pHash*d)%q
        # s[0]*d + s[1]*d^2 + s[2]*d^3 + ...
        currentHash= (ord(string[i]) + currentHash*d)%q

    for i in range(n-m+1):
        if currentHash == pHash:
            j=0
            print('in loop from ',i)
            while j<m:
                if string[i+j] != pattern[j]:
                    break
                j+=1
            if j==m:
                pArr.append(i)
        if i < n-m:
            # subtract the previous letter hash and add next one
            currentHash = (d*(currentHash - ord(string[i])*h) + ord(string[i+m]))%q
        if currentHash<0:
            currentHash +=  q
    return pArr



# print('pattern searching : naive : ',naivePatternSearchingForDistinct('abcabcabcdabcd','abcd'))
print('pattern searching : rabin karp : ',rabinKarpAlgorithm('hellhellohellohelhello','hello'))
