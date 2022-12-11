import math

# time complexity O(root(n))
def allDivisors(num):
    # first print smaller up to root(n)
    for i in range(1,math.floor(math.sqrt(num)+1)):
        if num %i == 0:
            print(i,end=' ')

    # then print bigger second multipel by reverse traversing from root(n) to 1
    for i in range(math.floor(math.sqrt(num)),0,-1):
        if num %i == 0:
            print(num//i,end=' ')


# number up to which, print all prime number
def sieveOfEratosthenes(num):
    primeArray = [True for i in range(num +1)]

    for i in range(2,num):
        if primeArray[i]:
            print(i,end=' ')
            for j in range(i*i,num,i):
                primeArray[j] = False

def powerOfNumber(number,power):
    res = 1
    for i in range(1,power+1):
        res *= number
    print(res)

# auxilaury space is: O(logn)
def powerOfNumberEfficient(n,power):
    if power==0:
        return 1
    res = powerOfNumberEfficient(n,power//2)
    if power %2 == 0:
        return res * res
    else:
        return res*res*n


# space required is: O(1) with logn time complexity - bit expontiation
def iterativePower(n,power):
    res = 1
    while power > 0:
        if power %2 != 0:
            res *= n
        n *= n
        power = power//2
    print('result: ',res)

iterativePower(2,5)

# powerOfNumber(2,5)
# print(powerOfNumberEfficient(2,5))


# sieveOfEratosthenes(100)
# allDivisors(45)