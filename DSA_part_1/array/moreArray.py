def leaderInArray(arr):
    leaderList = []
    n= len(arr) -1
    largest = arr[n]
    leaderList.append(largest)
    for i in range(n,-2,-1):
        if arr[i] > largest:
            leaderList.append(arr[i])
            largest = arr[i]
    return leaderList

def maxDiffInArray(arr):
    minV = arr[0]
    res = arr[1] - arr[0]
    for i in range(len(arr)):
        res = max(res,arr[i] - minV)
        minV = min(minV,arr[i])
    return res

def frequencyInSortedArray(arr):
    count =1
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            count +=1
        else:
            print(str(arr[i-1])+' : ',count)
            count = 1
        if i == len(arr)-1:
            print(str(arr[i])+' : ',count)

def stockBuySell(price):
    profit = 0
    for i in range(1,len(price)):
        if price[i] > price[i-1]:
            profit += price[i] - price[i-1]
    return profit

#  efficient in time complexity
#  create two array, lmax & rmax which store max ele from left and right respectively. compare them to find min block from both side
def tappintRainWater(blocks):
    n = len(blocks)
    lMax = [0]*n
    rMax = [0]*n
    lMax[0] = blocks[0]
    rMax[n-1] = blocks[n-1]
    rainWater = 0

    for i in range(1,n):
        lMax[i] = max(blocks[i],lMax[i-1])
    for i in range(n-2,-1,-1):
        rMax[i] = max(blocks[i],rMax[i+1])

    for i in range(1,n-1):
        rainWater += min(lMax[i],rMax[i]) - blocks[i]

    return rainWater

def maxConsicutiveOnes(arr):
    count = 0
    res = 0
    n =len(arr)
    for i in range(n):
        if arr[i] == 0:
            count = 0
        else:
            count +=1
            res =max(res,count)

    return res
def maxSumSubarray(arr):
    n = len(arr)
    res = arr[0]
    curr = arr[0]
    for i in range(1,n):
        curr = max(curr+arr[i],arr[i])
        res = max(res,curr)
    return res



# print('leader list: ',leaderInArray([8,2,6,4,4,5,1,2,3]))
# print('min diff: ',maxDiffInArray([1,3,5,3,6,8,9,5,2]))

frequencyInSortedArray([40,50,50,50])
# print('max profit in stock: ',stockBuySell([1,5,3,8,12]))
# print('rain collected : ',tappintRainWater([3,1,1,5,2,2,8]))
# print('max ones: ',maxConsicutiveOnes([1,1,0,0,1,1,1,0,0,1,1,1,1]))
# print("max sum subarray: ",maxSumSubarray([2,3,-8,9]))
# print("max sum subarray: ",maxSumSubarray([5,8,3]))
