# time : O(n) space : O(n)  stable
def quickPartationNaive(arr,l,h,p):
    ele = arr[p]
    tempArr = [0]*(h-l+1)
    index = 0
    # smaller elements
    for i in range(l,h+1):
        if arr[i] < ele:
            tempArr[index] = arr[i]
            index +=1
    # equal elments
    for i in range(l,h+1):
        if arr[i] == ele:
            tempArr[index] = arr[i]
            index +=1
    res = l + index -1

    # greater elements
    for i in range(l,h+1):
        if arr[i] > ele:
            tempArr[index] = arr[i]
            index +=1
    for i in range(l,h+1):
        arr[i] = tempArr[i-l]
    return res

# lomuto and hoare are not stable

# lomuto : i and j both move in same direction
def quickPartationLomuto(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

# Hoare : i and j both move in opposite direction
# pivot is not placed at its right index in hoare
def quickPartationHoare(arr,low,high):
    i = low-1
    j = high+1
    pivot = arr[low]
    while True:
        i+=1
        j-=1
        while arr[i] < pivot:
            i+=1
        while arr[j] > pivot:
            j-=1
        if j <=i:
            return j
        arr[i],arr[j] = arr[j],arr[i]
        

def quickSortLomuto(arr,low,high):
    if low <high:
        # we will not take pivot because pi is already at its correct position 
        pi = quickPartationLomuto(arr,low,high)
        quickSortLomuto(arr,low,pi-1)
        quickSortLomuto(arr,pi+1,high)
    return arr

# little faster then lomuto
def quickSortHoare(arr,low,high):
    if low <high:
        # we will (take) pivot because pi is not at its correct position 
        pi = quickPartationHoare(arr,low,high)
        quickSortHoare(arr,low,pi)
        quickSortHoare(arr,pi+1,high)
    return arr

# print('partation new index ',quickPartationNaive([2,4,7,5,6,4,8,1],1,7,5))
# print('quick partation ',quickSortLomuto([1,4,2,6,7,5,3],0,6))
print('quick partation ',quickSortHoare([1,4,2,6,7,5,3],0,6))