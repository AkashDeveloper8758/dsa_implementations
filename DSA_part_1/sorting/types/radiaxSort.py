
def countSort(arr,n,exp):
    count = [0]*10
    n = len(arr)
    for i in range(n):
        count[(arr[i]//exp)%10] +=1  # if exp is 1 it will give last element, and if 10 it will give second last and so on.
    for i in range(1,10):
        count[i] += count[i-1]
    
    output = [0]*(n)
    for i in range(n-1,-1,-1):
        output[count[(arr[i]//exp)%10]-1] = arr[i]
        count[(arr[i]//exp)%10]-=1
    for i in range(n):
        arr[i] = output[i]
    return arr

# count sort is done on item places like for 432 is 2 -> 3 -> 4
def radiaxSort(arr):
    maxV = arr[0]
    n = len(arr) 

    for i in range(n):
        if arr[i] > maxV:
            maxV = arr[i]

    exp = 1
    while (maxV//exp) > 0:
        countSort(arr,n,exp)
        exp*=10
    return arr

print('radiax sort : ',radiaxSort([81,4,1,19,50,22,35,45,76,12,90]))