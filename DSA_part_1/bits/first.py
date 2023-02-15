import math
a = 18
b = 23
# print(bin(a))
# print(bin(a  &(~(1<<2)) ))

# unset the i-th <0-based indexing> bit : a &(~(1<<i))
# set the i-th <0-based indexing> bit : a |(1<<i)

def findSetBits(num):
    count =0 
    while num:
        if num & 1 != 0:
            count +=1
        num = num >> 1
    return count

def diffInBits(a,b):
    # xor make the difference 1, then count total set bits.
    c = a ^ b
    count = 0
    # count set bits, log2(n)+1
    while c:
        if c &1 != 0:
            count +=1
        c = c >> 1
    return count

# time complexity : no of set bits. faster then log2(n)
def findNoOfSetBit(a):
    count = 0
    while a:
        count +=1
        a = a & (a-1)
        # this will unset the last set bit.
    return count

def findNonDuplicateNumber(arr):
    # xor of n ^ n = 0
    # xor of n ^ 0 = n
    res= 0
    for i in range(len(arr)):
        res= arr[i] ^ res
    # duplicate elements will cancle each other xor effect, only
    # non duplicate will remain
    return res

#* xor works as multiplication/division , if you do it with a number it is multi, and do it with same number 
#* again then it will work as division and give you the number before multi.
def findTwoNonDuplicateNumber(arr):
    res = 0
    n = len(arr)
    for i in range(n):
        res = res ^ arr[i]
    # find the first set bit position from the last.
    # because that is the position where the non repeating numbers bit is different (xor is 1, for different).
    pos = 0
    temp = res
    while temp:
        if temp & 1 == 1:
            break
        pos +=1
        temp = temp >> 1
    # xor with elements which are set-at (pos), which will give the one non repeating number. 
    # because other one is non-set at pos.
    mix = res
    for i in range(n):
        if( (arr[i] >> pos) & 1 == 1 ):
            mix = mix ^ arr[i]
    first = res ^ mix
    second = res ^ first
    return [first,second]

def findFirstPosOfSetBit(num):
    pos = 0
    while num:
        if num & 1 == 1:
            break
        pos +=1
        num = num >> 1
    return pos

def nonRepeatingIn3TimeRepeating(arr):
    # create a 32 size array, store the bit positions.
    # numbers which are comming thrice will make set bit multiple of 3.
    # and where reminder is 1, then it is once ocurring.

    intArr = [0] * 32
    n = len(arr)
    for i in range(n):
        x = arr[i]
        pos = 0
        while x:
            if (x & 1 == 1):
                intArr[pos] +=1
            x = x >> 1
            pos+=1
    res =0 
    for i in range(32):
        if(intArr[i] % 3 == 1):
            res += 2**i

    return res


# no of digits<baseType> => log<baseType>(value) + 1
# print('a : ',bin(a))
# print('b : ',bin(15))
# print('no of set bits diff : ',findNoOfSetBit(7))

arr = [5,4,1,4,3,5,1,8,3,3,8,8]
arr2 = [5,4,5,1,1,4,3,4,5,1,8,3,3]
print('non duplicate : ',findTwoNonDuplicateNumber(arr))
# print('non duplicate in 3 repeating : ',nonRepeatingIn3TimeRepeating(arr2))

# print('first set bit: ',[bin(34),findFirstPosOfSetBit(34)])