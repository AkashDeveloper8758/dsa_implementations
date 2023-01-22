
def lastOccurance(arr,x):
    l = 0
    h = len(arr)-1
    while l <= h:
        m = l + (h-l)//2
        if arr[m] == x:
            if m == len(arr)-1 or arr[m+1] != x:
                return m
            else:
                l = m+1
        elif arr[m] > x :
            h = m-1
        else:
            l = m + 1
    return -1

arr = [1,3,5,5,5,5,67,123,125]
index = lastOccurance(arr,5)
print('res : ',index)
