def countdigits(digit):
    count = 0
    while digit != 0:
        digit = digit //10
        count +=1
    return count

def countRecursive(digit):
    if digit == 0:
        return 0
    return 1 + countRecursive(digit//10)

def findingPalindrome(digit):
    original = digit
    newDigit = 0
    while digit != 0:
        rem = digit % 10
        newDigit = newDigit * 10 + rem
        digit = digit // 10
    return newDigit == original

def trailingZeroInFactorial(number):
    if number < 0:
        print('invalid number')
        return
    zeroCount,fNum =0, 1
    for i in range(1,number+1):
        fNum *= i
    fact = fNum
    while fNum % 10 ==0:
        zeroCount +=1
        fNum = fNum //10
    # print('factorial: ',fact)
    print('zeros are: ',zeroCount)

def efficientTrailingZeroFinder(number):
    zeros = 0
    i =5
    # at 25,125,625, there is one extra 5, that's why we are multiplying i*=5
    while i< number:
        zeros += number//i
        i *= 5
    print('efficient zero : ',zeros)

# print('is number is palindrome: ',findingPalindrome(60061)) 
# print('count is : ',countRecursive(346584293437))

number = 30
trailingZeroInFactorial(number)
print('--------------------------')
efficientTrailingZeroFinder(number)