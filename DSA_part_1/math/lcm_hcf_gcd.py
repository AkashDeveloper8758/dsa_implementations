import math
def gcdOfNumber(num1,num2):
    minNum = min(num1,num2)
    maxNum = max(num1,num2)
    gcd = 0
    if maxNum % minNum ==0:
        return minNum
    for i in range(1,minNum//2+1):
        print('--',i)
        if num1 %i == 0 and num2 %i ==0:
            gcd = i
    return gcd

def efficientGCD(num1,num2):
    while num1 != num2:
        if num1> num2:
            num1 = num1- num2
        else:
            num2 = num2-num1
    return num1

def moreEfficientGCD(a,b):
    if b ==0:
        return a
    return moreEfficientGCD(b,a%b)
# ---------------------------------------------------------- LCM

def findLCM(a,b):
    return (a*b)//efficientGCD(a,b)

def ifPrime(num):
    if num == 1:
        return False

    if num == 2 or num == 3:
        return True
    if num %2 == 0 or num %3 == 0:
        return False

    i =2
    while i < math.sqrt(num) +1:
        if num %i == 0:
            return False
        i +=1

    return True

def primeFactor(num):
    for i in range(2,math.floor(math.sqrt(num)+1)):
        if ifPrime(i):
            while num %i == 0:
                print(i,end=' ')
                num = num//i
    if num > 1:
        print(num)

    

# primeFactor(57)



# print('gcd : ',moreEfficientGCD(30,10))
# print('lcm : ',findLCM(4,6))
print('is prime : ',ifPrime(49))


