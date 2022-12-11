from numpy import array


def kmpPatternSearchingNaive(string,n):
    for len in range(n-1,-1,-1):
        flag = True
        for i in range(len):
            if string[i] != string[n-len+i]:
                flag = False
                break
        if flag:
            return len
    return 0
    

def fillLps(string,lpsarr):
    for i in range(len(string)):
        lpsarr.append(kmpPatternSearchingNaive(string,i+1))
    print('lps array : ',lpsarr)

fillLps('ababaabba',[])

# n = 4
# len = 3
# i = 1
# string[i] = string[1]
# string[n-len-i] = string(4-3-1) = string[0]