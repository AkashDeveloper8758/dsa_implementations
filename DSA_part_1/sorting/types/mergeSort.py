# space = O(n) time = O(n)
def mergeFunc(arr,low,mid,high):
    m = mid-low+1
    n = high-mid
    left = [0]*m
    right = [0]*n
    
    # filling two arrays with left and right values
    for i in range(m):
        left[i] = arr[i+low]
    for j in range(n):
        right[j] = arr[j+mid+1]


# k will be = low, because we have to sort array from low which may not be zero in middle cases
# res will count no of inversions
    l,r,k,res = 0,0,low,0
    while l <m and r < n:
        if left[l] <= right[r]:
            arr[k] = left[l]
            l+=1
        else:
            arr[k] = right[r]
            r+=1
            # if left is greater then right then elements after (l) up to (m) are also greater,
            # because left and right are sorted so we increase by difference m-l
            res += m-l
        k+=1

    # taking elements from the largest array 
    while l<m:
        arr[k] = left[l]
        k+=1
        l+=1
    while r<n:
        arr[k] = right[r]
        k+=1
        r+=1
    return res

# space : O(1) time : O(nlogn)
def mergeArrayUsingShellSort(arr,low,mid,high):
    gap = high-low+1
    gap = gap//2
    while gap > 0:
        i = low
        while i+gap <= high:
            j = gap+i
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            i+=1
        gap = gap//2    

# space O(1) time : O(n)  ** most efficient ** 
def mergeArrayUsingMod(arr,low,mid,high):
    N = max(arr[mid],arr[high]) +1
    i = low
    j = mid+1
    k = low
    while i <= mid and j <= high:
        e1 = arr[i] % N
        e2 = arr[j] % N
        if e1 <= e2:
            arr[k] += e1*N
            i+=1
            k+=1
        else:
            arr[k] += e2*N
            j+=1
            k+=1
    while i <= mid:
        el = arr[i] % N
        arr[k] += el*N
        k+=1
        i+=1
    while j <= high:
        el = arr[j] % N
        arr[k] += el*N
        k+=1
        j+=1
    for i in range(low,high+1):
        arr[i] //= N

def mergeSort(arr,l,r):
    res = 0
    if r > l:
        m = l+(r-l)//2
        res += mergeSort(arr,l,m)
        res += mergeSort(arr,m+1,r)
        res += mergeFunc(arr,l,m,r)
    return res

# merging different arrays INPLACE. extention of above code.
def merge(arr1,arr2,n,m):
    maxv = max(arr1[-1],arr2[-1])+1
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        e1 = arr1[i] % maxv
        e2 = arr2[j] % maxv

        if e1 <= e2:
            if k >= n:
                arr2[k-n] += e1*maxv
            else:
                arr1[k] += e1*maxv
            k+=1
            i+=1
        else:
            if k >= n:
                arr2[k-n] += e2*maxv
            else:
                arr1[k] += e2*maxv
            k+=1
            j+=1
            
    while i < n:
        e1 = arr1[i] % maxv
        if k >= n:
            arr2[k-n] += e1*maxv
        else:
            arr1[k] += e1*maxv
        k+=1
        i+=1
    while j < m:
        e2 = arr2[j] % maxv
        if k >= n:
            arr2[k-n] += e2*maxv
        else:
            arr1[k] += e2*maxv
        k += 1
        j += 1

    for i in range(n):
        arr1[i] = arr1[i]//maxv
    for i in range(m):
        arr2[i] = arr2[i]//maxv
    

# mergeFunc([3,4,5,6,7,1,2,3],0,4,7)
arr = [2,4,1,3,5]
n= len(arr)
print('no of inversions : ',mergeSort(arr,0,n-1))
print('array : ',arr)
